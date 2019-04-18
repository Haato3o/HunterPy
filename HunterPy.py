from Memory import *
from logger import Log
import time, os
from threading import Thread
import psutil

class IDS:
    Zones = {
        7 : "Main Menu",
        8 : "Special Arena",
        10 : "Confluence of Fates",
        11 : "Gathering HUB",
        15 : "My Room",
        18 : "Elder's Recess",
        23 : "Training area",
        23.1 : "Arena",
        24 : "Research Base",
        31 : "Astera",
        37 : "Rotten Vale",
        58 : "Coral Highlands",
        64 : "Wildspire Waste",
        94 : "Ancient Forest",
    }
    Monsters = {
        "em100_00" : "Anjanath",
        "em002_01" : "Azure Rathalos",
        "em044_00" : "Barroth",
        "em118_00" : "Bazelgeuse",
        "em121_00" : "Behemoth",
        "em007_01" : "Black Diablos",
        "em043_00" : "Deviljho",
        "em007_00" : "Diablos",
        "em116_00" : "Dodogama",
        "em112_00" : "Great Girros",
        "em101_00" : "Jyuratodus",
        "em011_00" : "Kirin",
        "em107_00" : "Kulu Ya Ku",
        "em117_00" : "Kulve Taroth",
        "em024_00" : "Kushala Daora",
        "em036_00" : "Lavasioth",
        "em111_00" : "Legiana",
        "em026_00" : "Lunastra",
        "em103_00" : "Nergigante",
        "em113_00" : "Odogaron",
        "em110_00" : "Paolumu",
        "em001_01" : "Pink Rathian",
        "em102_00" : "Pukei Pukei",
        "em114_00" : "Radobaan",
        "em002_00" : "Rathalos",
        "em001_00" : "Rathian",
        "em027_00" : "Teostra",
        "em109_00" : "Tobi Kadachi",
        "em120_00" : "TziTzi Ya Ku",
        "em045_00" : "Uragaan",
        "em115_00" : "Vaal Hazak",
        "em105_00" : "Xeno'Jiiva",
        "em106_00" : "Zorah Magdaros"
    }


class Player:
    def __init__(self):
        self.Name = None
        self.Level = None
        self.ZoneID = None
        self.ZoneName = None
        self.SessionID = None
        

class Monster:
    def __init__(self):
        self.Name = "UNKNOWN"
        self.Id = None
        self.TotalHP = None
        self.CurrentHP = None
        self.isTarget = False
        self.Address = 0xFFFFFF

class Game:
    baseAddress = 0x140000000 # MonsterHunterWorld.exe base address
    LevelOffset = 0x3B5FEC8    # Level offset
    levelAddress = 0xFFFFFF     # Level address used to get name
    ZoneOffset = 0x04852910  # Zone ID offset
    MonsterOffset = 0x48525D0 # monster offset
    SessionOffset = 0x0485A430 # Session id offset
    
    def __init__(self, pid):
        # Scanner stuff
        self.pid = pid
        self.MemoryReader = Memory(self.pid)
        self.Scanner = None
        # Player info
        self.PlayerInfo = Player()
        # Monsters info
        self.PrimaryMonster = Monster()
        self.SecondaryMonster = Monster()
        self.ThirtiaryMonster = Monster()
        
    def scanUntilDone(self):
        while psutil.pid_exists(self.pid):
            os.system('cls')
            self.getPlayerLevel()
            self.getPlayerName()
            self.getSessionID()
            self.getPlayerZoneID()
            self.GetAllMonstersAddress()
            self.GetAllMonstersInfo()
            time.sleep(0.2)

    def MultiThreadScan(self):
        self.Scanner = Thread(target=self.scanUntilDone)
        self.Scanner.daemon = True
        self.Scanner.start()

    def init(self):
        Log(f"BASE ADDRESS: {hex(Game.baseAddress)}")
        self.MultiThreadScan()
            
    def getPlayerName(self):
        self.PlayerInfo.Name = self.MemoryReader.readString(Game.levelAddress-64, 20).decode().strip('\x00')
        Log(f"PLAYER NAME: {self.PlayerInfo.Name} ({hex(Game.levelAddress-64)})")

    def getPlayerLevel(self):
        Address = Game.baseAddress + Game.LevelOffset
        fValue = self.MemoryReader.readInteger(Address)
        ptrAddress = fValue + 144
        ptrValue = self.MemoryReader.readInteger(ptrAddress)
        Game.levelAddress = ptrValue + 0x68
        self.PlayerInfo.Level = self.MemoryReader.readInteger(ptrValue + 0x68)
        Log(f'HUNTER RANK: {self.PlayerInfo.Level} ({hex(ptrValue+0x68)})')

    def getPlayerZoneID(self):
        Address = Game.baseAddress + Game.ZoneOffset
        offsets = [0x78, 0x440, 0x8, 0x70]
        sValue = self.MemoryReader.GetMultilevelPtr(Address, offsets)
        self.PlayerInfo.ZoneID = self.MemoryReader.readInteger(sValue + 0x2B0)
        if self.PlayerInfo.ZoneID == 23 and self.ThirtiaryMonster.TotalHP != 0.0: # Checks if there's a monster in the map, if so then it's an arena
            self.PlayerInfo.ZoneID = 23.1
        self.getPlayerZoneNameByID()
        Log(f'{self.PlayerInfo.ZoneName} | ZONE ID: {self.PlayerInfo.ZoneID} ({hex(sValue + 0x2B0)})')
        
    def getPlayerZoneNameByID(self):
        self.PlayerInfo.ZoneName = IDS.Zones.get(self.PlayerInfo.ZoneID)

    def GetAllMonstersAddress(self):
        AddressBase = Game.baseAddress + Game.MonsterOffset
        offsets = [0xAF738, 0x47CDE0]
        thirdMonsterAddress = self.MemoryReader.GetMultilevelPtr(AddressBase, offsets)
        thirdMonsterAddress = self.MemoryReader.readInteger(thirdMonsterAddress + 0x0)
        thirdMonsterAddress = thirdMonsterAddress + 0x0
        secondMonsterAddress = thirdMonsterAddress + 0x28
        firstMonsterAddress = self.MemoryReader.readInteger(secondMonsterAddress) + 0x28
        self.PrimaryMonster.Address = firstMonsterAddress
        self.SecondaryMonster.Address = secondMonsterAddress
        self.ThirtiaryMonster.Address = thirdMonsterAddress

    # GET ALL MONSTER INFO
    def GetAllMonstersInfo(self):
        self.GetAllMonstersName()
        self.GetAllMonstersID()
        self.GetAllMonstersHP()

    ## GET ALL MONSTERS NAME
    def GetAllMonstersName(self):
        self.PrimaryMonster.Name = IDS.Monsters.get(self.PrimaryMonster.Id)
        self.SecondaryMonster.Name = IDS.Monsters.get(self.SecondaryMonster.Id)
        self.ThirtiaryMonster.Name = IDS.Monsters.get(self.ThirtiaryMonster.Id)

    ## GET ALL MONSTERS HP
    def GetAllMonstersHP(self):
        try:
            self.getFirstMonsterTotalHP()
        except:
            pass
        try:
            self.getSecondMonsterTotalHP()
        except:
            pass
        try:
            self.getThirtiaryMonsterTotalHP()
        except:
            pass
        

    ## GET ALL MONSTERS ID
    def GetAllMonstersID(self):
        try:
            self.GetFirstMonsterID()
        except:
            self.PrimaryMonster.Id = None
            pass
        try:
            self.GetSecondMonsterID()
        except:
            self.SecondaryMonster.Id = None
            pass
        try:
            self.GetThirdMonsterID()
        except:
            self.ThirtiaryMonster.Id = None
            pass
        
    ## Get 1st info
    def GetFirstMonsterID(self):
        Address = self.PrimaryMonster.Address
        Address = self.MemoryReader.readInteger(Address)
        namePointer = self.MemoryReader.readInteger(Address + 0x290)
        Id = self.MemoryReader.readString(namePointer + 0x0c, 64).decode().split('\\')[4].strip('\x00')
        self.PrimaryMonster.Id = Id

    def getFirstMonsterTotalHP(self):
        Address = self.PrimaryMonster.Address
        Address = self.MemoryReader.readInteger(Address)
        monsterHPComponent = self.MemoryReader.readInteger(Address+0x129D8+0x48)
        monsterTotalHpAddress = monsterHPComponent + 0x60
        monsterTotalHP = self.MemoryReader.readFloat(monsterTotalHpAddress)
        self.getPrimaryMonsterCurrentHP(monsterTotalHpAddress)
        self.PrimaryMonster.TotalHP = monsterTotalHP
        Log(f'NAME: {self.PrimaryMonster.Name} | ID: {self.PrimaryMonster.Id} | HP: {int(self.PrimaryMonster.CurrentHP)}/{int(self.PrimaryMonster.TotalHP)} ({hex(monsterTotalHpAddress)})')
        
    def getPrimaryMonsterCurrentHP(self, totalHPAddress):
        TotalHP = self.MemoryReader.readFloat(totalHPAddress)
        self.PrimaryMonster.CurrentHP = self.MemoryReader.readFloat(totalHPAddress + 0x4)

    ## Get 2nd info
    def GetSecondMonsterID(self):
        Address = self.SecondaryMonster.Address
        Address = self.MemoryReader.readInteger(Address)
        namePointer = self.MemoryReader.readInteger(Address + 0x290)
        Id = self.MemoryReader.readString(namePointer + 0x0c, 64).decode().split('\\')[4].strip('\x00')
        self.SecondaryMonster.Id = Id

    def getSecondMonsterTotalHP(self):
        Address = self.SecondaryMonster.Address
        Address = self.MemoryReader.readInteger(Address)
        monsterHPComponent = self.MemoryReader.readInteger(Address+0x129D8+0x48)
        monsterTotalHPAddress = monsterHPComponent + 0x60
        monsterTotalHP = self.MemoryReader.readFloat(monsterTotalHPAddress)
        self.getSecondaryMonsterCurrentHP(monsterTotalHPAddress)
        self.SecondaryMonster.TotalHP = monsterTotalHP
        Log(f'NAME: {self.SecondaryMonster.Name} | ID: {self.SecondaryMonster.Id} | HP: {int(self.SecondaryMonster.CurrentHP)}/{int(self.SecondaryMonster.TotalHP)} ({hex(monsterTotalHPAddress)})')

    def getSecondaryMonsterCurrentHP(self, totalHPAddress):
        TotalHP = self.MemoryReader.readFloat(totalHPAddress)
        self.SecondaryMonster.CurrentHP = self.MemoryReader.readFloat(totalHPAddress + 0x4) if TotalHP > 0 else 0.0

    ## Get 3rd info
    def GetThirdMonsterID(self):
        Address = self.ThirtiaryMonster.Address
        namePointer = self.MemoryReader.readInteger(Address + 0x290)
        Id = self.MemoryReader.readString(namePointer + 0x0c, 64).decode().split('\\')[4].strip('\x00')
        self.ThirtiaryMonster.Id = Id

    def getThirtiaryMonsterTotalHP(self):
        Address = self.ThirtiaryMonster.Address
        monsterHPComponent = self.MemoryReader.readInteger(Address+0x129D8+0x48)
        monsterTotalHPAddress = monsterHPComponent + 0x60
        monsterTotalHP = self.MemoryReader.readFloat(monsterTotalHPAddress)
        self.getThirtiaryMonsterCurrentHP(monsterTotalHPAddress)
        self.ThirtiaryMonster.TotalHP = monsterTotalHP
        Log(f'NAME: {self.ThirtiaryMonster.Name} | ID: {self.ThirtiaryMonster.Id} | HP: {int(self.ThirtiaryMonster.CurrentHP)}/{int(self.ThirtiaryMonster.TotalHP)} ({hex(monsterTotalHPAddress)})')

    def getThirtiaryMonsterCurrentHP(self, totalHPAddress):
        TotalHP = self.MemoryReader.readFloat(totalHPAddress)
        self.ThirtiaryMonster.CurrentHP = self.MemoryReader.readFloat(totalHPAddress + 0x4) if TotalHP > 0 else 0.0

    # Session ID
    def getSessionID(self):
        Address = Game.baseAddress + Game.SessionOffset
        offsets = [0xA0, 0x20, 0x80, 0x9C]
        sValue = self.MemoryReader.GetMultilevelPtr(Address, offsets)
        SessionID = self.MemoryReader.readString(sValue+0x3C8, 12)
        self.PlayerInfo.SessionID = SessionID.decode()
        Log(f'Session ID: {self.PlayerInfo.SessionID} ({hex(sValue+0x3C8)})')