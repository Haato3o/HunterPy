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
        self.TotalHP = None
        self.CurrentHP = None
        self.isTarget = False

class Game:
    baseAddress = 0x140000000 # MonsterHunterWorld.exe base address
    LevelOffset = 0x3B5FEC8    # Level offset
    levelAddress = 0xFFFFFF     # Level address used to get name
    ZoneOffset = 0x04852910  # Zone ID offset
    MonsterOffset = 0x04852610 # monster offset
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
            self.getFirstMonsterTotalHP()
            self.getSecondMonsterTotalHP()
            self.getThirtiaryMonsterTotalHP()
            time.sleep(0.3)

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
        sValue = self.MemoryReader.readInteger(Address)
        offsets = [0x78, 0x440, 0x8, 0x70]
        for offset in offsets:
            sValue = self.MemoryReader.readInteger(sValue + offset)
        self.PlayerInfo.ZoneID = self.MemoryReader.readInteger(sValue + 0x2B0)
        if self.PlayerInfo.ZoneID == 23 and self.ThirtiaryMonster.TotalHP != 0.0: # Checks if there's a monster in the map, if so then it's an arena
            self.PlayerInfo.ZoneID = 23.1
        self.getPlayerZoneNameByID()
        Log(f'{self.PlayerInfo.ZoneName} | ZONE ID: {self.PlayerInfo.ZoneID} ({hex(sValue + 0x2B0)})')
        
    def getPlayerZoneNameByID(self):
        self.PlayerInfo.ZoneName = IDS.Zones.get(self.PlayerInfo.ZoneID)

    ## Get 1st monster hp
    def getFirstMonsterTotalHP(self):
        Address = Game.baseAddress + Game.MonsterOffset
        offsets = [0x6B8, 0x10, 0x120, 0x160]
        aValue = self.MemoryReader.readInteger(Address)
        for offset in offsets:
            aValue = self.MemoryReader.readInteger(aValue + offset)
        TotalHP = self.MemoryReader.readFloat(aValue + 0x290)
        self.PrimaryMonster.TotalHP = TotalHP if TotalHP > 0 else 0.0
        self.getPrimaryMonsterCurrentHP(aValue+0x290)
        Log(f'Primary monster: {self.PrimaryMonster.Name} | HP: {self.PrimaryMonster.CurrentHP}/{self.PrimaryMonster.TotalHP} ({hex(aValue + 0x290)})')

    def getPrimaryMonsterCurrentHP(self, totalHPAddress):
        TotalHP = self.MemoryReader.readFloat(totalHPAddress)
        self.PrimaryMonster.CurrentHP = self.MemoryReader.readFloat(totalHPAddress + 0x4) if TotalHP > 0 else 0.0

    ## Get 2nd monster hp
    def getSecondMonsterTotalHP(self):
        Address = Game.baseAddress + Game.MonsterOffset
        offsets = [0x6B8, 0x8, 0xB8, 0x120]
        aValue = self.MemoryReader.readInteger(Address)
        for offset in offsets:
            aValue = self.MemoryReader.readInteger(aValue + offset)
        TotalHP = self.MemoryReader.readFloat(aValue + 0x1E0)
        self.SecondaryMonster.TotalHP = TotalHP if TotalHP > 0 else 0.0
        self.getSecondaryMonsterCurrentHP(aValue+0x1E0)
        Log(f'Secondary monster: {self.SecondaryMonster.Name} | HP: {self.SecondaryMonster.CurrentHP}/{self.SecondaryMonster.TotalHP} ({hex(aValue + 0x1E0)})')

    def getSecondaryMonsterCurrentHP(self, totalHPAddress):
        TotalHP = self.MemoryReader.readFloat(totalHPAddress)
        self.SecondaryMonster.CurrentHP = self.MemoryReader.readFloat(totalHPAddress + 0x4) if TotalHP > 0 else 0.0

    ## Get 3rd monster hp
    def getThirtiaryMonsterTotalHP(self):
        Address = Game.baseAddress + Game.MonsterOffset
        offsets = [0x650, 0x120, 0x108, 0x370]
        aValue = self.MemoryReader.readInteger(Address)
        for offset in offsets:
            aValue = self.MemoryReader.readInteger(aValue + offset)
        TotalHP = self.MemoryReader.readFloat(aValue + 0xB0)
        self.ThirtiaryMonster.TotalHP = TotalHP if TotalHP > 0 else 0.0
        self.getThirtiaryMonsterCurrentHP(aValue + 0xB0)
        Log(f'Thirtiary monster: {self.ThirtiaryMonster.Name} | HP: {self.ThirtiaryMonster.CurrentHP}/{self.ThirtiaryMonster.TotalHP} ({hex(aValue + 0xB0)})')

    def getThirtiaryMonsterCurrentHP(self, totalHPAddress):
        TotalHP = self.MemoryReader.readFloat(totalHPAddress)
        self.ThirtiaryMonster.CurrentHP = self.MemoryReader.readFloat(totalHPAddress + 0x4) if TotalHP > 0 else 0.0

    # Session ID
    def getSessionID(self):
        Address = Game.baseAddress + Game.SessionOffset
        offsets = [0xA0, 0x20, 0x80, 0x9C]
        sValue = self.MemoryReader.readInteger(Address)
        for offset in offsets:
            sValue = self.MemoryReader.readInteger(sValue + offset)
        SessionID = self.MemoryReader.readString(sValue+0x3C8, 12)
        self.PlayerInfo.SessionID = SessionID.decode()
        Log(f'Session ID: {self.PlayerInfo.SessionID} ({hex(sValue+0x3C8)})')