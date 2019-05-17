from Memory import *
import time, os
from threading import Thread
import psutil

class IDS: # Countains every id for stuff in the game, might remake it later to support translations and stuff
    NoMonstersZones = [3.1, 5, 7, 11, 15, 21, 23, 24, 31, 33]
    Mantles = { # Credits to https://github.com/Ezekial711/MonsterHunterWorldModding/wiki/Specialized-Tools-IDs
        0 : "Ghillie Mantle",
        1 : "Temporal Mantle",
        2 : "Health Booster",
        3 : "Rocksteady Mantle",
        4 : "Challenger Mantle",
        5 : "Vitality Mantle",
        6 : "Fireproof Mantle",
        7 : "Waterproof Mantle",
        8 : "Iceproof Mantle",
        9 : "Thunderproof Mantle",
        10 : "Dragonproof Mantle",
        11 : "Cleanser Booster", 
        12 : "Glider Mantle",
        13 : "Evasion Mantle",
        14 : "Impact Mantle",
        15 : "Apothecary Mantle",
        16 : "Immunity Mantle",
        17 : "Affinity Booster",
        18 : "Bandit Mantle",
        19 : "Assassin's Hood"
    }
    Fertilizers = {
        8 : "Growth Up (L)",
        7 : "Growth Up (S)",
        6 : "Bug/Honey Harvest Up (L)",
        5 : "Bug/Honey Harvest Up (S)",
        4 : "Fungi Harvest Up (L)",
        3 : "Fungi Harvest Up (S)",
        2 : "Plant Harvest Up (L)",
        1 : "Plant Harvest Up (S)",
        0 : "Empty"
    }
    Zones = {
        3 : "Great Ravine",
        3.1 : "Main Menu",
        5 : "Main Menu",
        7 : "Main Menu",
        17 : "Main Menu",
        8 : "Special Arena",
        10 : "Confluence of Fates",
        11 : "Gathering Hub",
        12 : "Caverns of El Dorado",
        15 : "Private Suite",
        16 : "Private Quarters",
        5 : "Living Quarters",
        18 : "Elder's Recess",
        21 : "Gathering Hub", # During blossom event
        23 : "Training area",
        23.1 : "Arena",
        24 : "Research Base",
        31 : "Astera",
        33 : "Astera", # During blossom event
        37 : "Rotten Vale",
        58 : "Coral Highlands",
        64 : "Wildspire Waste",
        94 : "Ancient Forest",
    }
    Monsters = {
        "em100_00" : "Anjanath",
        "em101_00" : "Great Jagras",
        "em002_01" : "Azure Rathalos",
        "em044_00" : "Barroth",
        "em118_00" : "Bazelgeuse",
        "em121_00" : "Behemoth",
        "em007_01" : "Black Diablos",
        "em043_00" : "Deviljho",
        "em007_00" : "Diablos",
        "em116_00" : "Dodogama",
        "em112_00" : "Great Girros",
        "em108_00" : "Jyuratodus",
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
        "em120_00" : "Tzitzi-Ya-Ku",
        "em045_00" : "Uragaan",
        "em115_00" : "Vaal Hazak",
        "em105_00" : "Xeno'Jiiva",
        "em106_00" : "Zorah Magdaros",
        "em127_00" : "Leshen", # The witcher 3: Wild Hunt event
        "em127_01" : "Ancient Leshen" # The witcher 3: Wild Hunt event p2
    }
    Weapons = {
        0 : "Greatsword",
        1 : "Sword and Shield",
        2 : "Dual Blades",
        3 : "Long Sword",
        4 : "Hammer",
        5 : "Hunting Horn",
        6 : "Lance",
        7 : "GunLance",
        8 : "Switch Axe",
        9 : "Charge Blade",
        10 : "Insect Glaive",
        11 : "Bow",
        12 : "Heavy Bowgun",
        13 : "Light Bowgun"
    }


class Player: # player class
    def __init__(self):
        self.Name = "" # Player Name (only support player slot 1)
        self.Level = 0 # Player level
        self.ZoneID = 0 # Player zone
        self.LastZoneID = 0 # player last zone
        self.Weapon_id = None # Weapon id
        self.Weapon_name = "" # Weapon name
        self.ZoneName = "" # zone name
        self.SessionID = "" # session id (the one you use to invite friends to your session)
        self.HarvestedItemsCounter = 0 # amount of items in harvest box
        self.HarvestBox = [] # each slot in harvest box
        self.HarvestBoxFertilizers = [] # the 4 fertilizers amount
        self.PrimaryMantle = 0 # primary mantle player has equipped
        self.PrimaryMantleInfo = [0.0, 0.0, 0.0, 0.0] # first number is fixed cooldown, 2nd is dynamic cooldown, 3rd is fixed timer, 4th is dynamic timer
        self.SecondaryMantle = 0 # secondary mantle player has equipped
        self.SecondaryMantleInfo = [0.0, 0.0, 0.0, 0.0] # first number is fixed cooldown, 2nd is dynamic cooldown, 3rd is fixed timer, 4th is dynamic timer
        self.PartyMembers = []

class Monster: # Monster class, each monster will initialize one
    def __init__(self):
        self.Name = "UNKNOWN" # Monster Name
        self.Id = "" # Monster ID
        self.TotalHP = 0 # Monster total HP
        self.CurrentHP = 0 # Monster current HP
        self.isTarget = False # True if it's the player's target, false if not
        self.Address = 0x0 # Monster address in memory

class Game:
    BASE_ADDRESS = 0x140000000 # MonsterHunterWorld.exe base address
    LEVEL_OFFSET = 0x03B3D2F8    # Level offset
    LEVEL_ADDRESS = 0xFFFFFF     # Level address used to get name
    PARTY_OFFSET = 0x03C01D40 # Party member names
    ZONE_OFFSET = 0x048E3EA0  # Zone ID offset
    MONSTER_OFFSET = 0x48D1710 # monster offset
    SESSION_OFFSET = 0x048D95E0 # Session id offset
    EQUIPMENT_OFFSET = 0x03B416A8 # Equipment container offset
    WEAPON_OFFSET = 0x03BDEE98 # Weapon offset
    cooldownFixed = 0x9EC
    cooldownDynamic = 0x99C
    timerFixed = 0xADC
    timerDynamic = 0xA8C

    def __init__(self, pid):
        # Scanner stuff
        self.pid = pid
        self.MemoryReader = Memory(self.pid)
        self.Scanner = False
        # Player info
        self.PlayerInfo = Player()
        # Monsters info
        self.PrimaryMonster = Monster()
        self.SecondaryMonster = Monster()
        self.ThirtiaryMonster = Monster()
        self.EquipmentAddress = None
        self.Logger = []
    
    def scanUntilDone(self):
        while psutil.pid_exists(self.pid):
            self.Logger = []
            self.Log(f'"MonsterHunterWorld.exe" -> PID: {self.pid}')
            self.getPlayerLevel()
            self.getPlayerName()
            self.getSessionID()
            self.GetPlayerWeapon()
            self.GetPartyMembers()
            self.getFertilizerCount()
            self.GetEquipmentAddress()
            self.GetEquippedMantlesIDs()
            self.getMantlesTimer()
            self.GetAllMonstersAddress()
            self.GetAllMonstersInfo()
            self.getPlayerZoneID()
            self.PredictTarget()
            time.sleep(0.2)
        self.Logger = []

    def MultiThreadScan(self):
        self.Scanner = Thread(target=self.scanUntilDone)
        self.Scanner.daemon = True
        self.Scanner.start()

    def init(self):
        self.Log(f"BASE ADDRESS: {hex(Game.BASE_ADDRESS)}")
        self.MultiThreadScan()
    
    def Log(self, string, i=-1):
        if i == -1:
            self.Logger.append("[HunterPy] "+string+"\n")
        else:
            self.Logger.insert(i, "[HunterPy] "+string+"\n")

    def getPlayerName(self):
        self.PlayerInfo.Name = self.MemoryReader.READ_STRING(Game.LEVEL_ADDRESS-64, 20).decode().strip('\x00')
        self.Log(f"PLAYER NAME: {self.PlayerInfo.Name} ({hex(Game.LEVEL_ADDRESS-64)})")

    def getPlayerLevel(self):
        Address = Game.BASE_ADDRESS + Game.LEVEL_OFFSET
        offsets = [0x70, 0x58, 0x20, 0x58]
        fValue = self.MemoryReader.READ_MULTILEVEL_PTR(Address, offsets)
        levelValue = self.MemoryReader.READ_INTEGER(fValue + 0x108)
        Game.LEVEL_ADDRESS = fValue + 0x108
        self.PlayerInfo.Level = levelValue
        self.Log(f'HUNTER RANK: {self.PlayerInfo.Level} ({hex(fValue + 0x108)})')

    def getPlayerZoneID(self):
        Address = Game.BASE_ADDRESS + Game.ZONE_OFFSET
        offsets = [0x3F0, 0x18, 0x8, 0x70]
        sValue = self.MemoryReader.READ_MULTILEVEL_PTR(Address, offsets)
        ZoneID = self.MemoryReader.READ_INTEGER(sValue + 0x2B0)
        if ZoneID == 23 and self.ThirtiaryMonster.TotalHP > 100: # Checks if there's a monster in the map, if so then it's an arena
            ZoneID = 23.1
        if ZoneID == 3 and self.SecondaryMonster.TotalHP == 0:
            ZoneID = 3.1
        if self.PlayerInfo.ZoneID != ZoneID:
            self.UpdateLastZoneID()
            self.PlayerInfo.ZoneID = ZoneID
        self.getPlayerZoneNameByID()
        self.Log(f'ZONE NAME: {self.PlayerInfo.ZoneName} | ZONE ID: {self.PlayerInfo.ZoneID} ({hex(sValue + 0x2B0)})')
        
    def getPlayerZoneNameByID(self):
        self.PlayerInfo.ZoneName = IDS.Zones.get(self.PlayerInfo.ZoneID)

    def GetAllMonstersAddress(self):
        AddressBase = Game.BASE_ADDRESS + Game.MONSTER_OFFSET
        offsets = [0xAF738, 0x47CDE0]
        thirdMonsterAddress = self.MemoryReader.READ_MULTILEVEL_PTR(AddressBase, offsets)
        thirdMonsterAddress = self.MemoryReader.READ_LONGLONG(thirdMonsterAddress + 0x0)
        thirdMonsterAddress = thirdMonsterAddress + 0x0
        secondMonsterAddress = thirdMonsterAddress + 0x28
        firstMonsterAddress = self.MemoryReader.READ_LONGLONG(secondMonsterAddress) + 0x28
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
        Address = self.MemoryReader.READ_LONGLONG(Address)
        namePointer = self.MemoryReader.READ_LONGLONG(Address + 0x290)
        Id = self.MemoryReader.READ_STRING(namePointer + 0x0c, 64).decode().split('\\')[4].strip('\x00')
        self.PrimaryMonster.Id = Id

    def getFirstMonsterTotalHP(self):
        Address = self.PrimaryMonster.Address
        Address = self.MemoryReader.READ_LONGLONG(Address)
        monsterHPComponent = self.MemoryReader.READ_LONGLONG(Address+0x129D8+0x48)
        monsterTotalHpAddress = monsterHPComponent + 0x60
        monsterTotalHP = self.MemoryReader.READ_FLOAT(monsterTotalHpAddress)
        if self.PrimaryMonster.Id != None and self.PrimaryMonster.Id.startswith('ems'):
            self.PrimaryMonster.TotalHP = 0
        else:
            self.PrimaryMonster.TotalHP = monsterTotalHP
        self.getPrimaryMonsterCurrentHP(monsterTotalHpAddress)
        self.Log(f'NAME: {self.PrimaryMonster.Name} | ID: {self.PrimaryMonster.Id} | HP: {int(self.PrimaryMonster.CurrentHP)}/{int(self.PrimaryMonster.TotalHP)} ({hex(monsterTotalHpAddress)})')
        self.Log(f"Target: {self.PrimaryMonster.isTarget}\n")

    def getPrimaryMonsterCurrentHP(self, totalHPAddress):
        TotalHP = self.MemoryReader.READ_FLOAT(totalHPAddress)
        currentHP = self.MemoryReader.READ_FLOAT(totalHPAddress + 0x4)
        self.PrimaryMonster.CurrentHP = currentHP if currentHP <= self.PrimaryMonster.TotalHP else 0

    ## Get 2nd info
    def GetSecondMonsterID(self):
        Address = self.SecondaryMonster.Address
        Address = self.MemoryReader.READ_LONGLONG(Address)
        namePointer = self.MemoryReader.READ_LONGLONG(Address + 0x290)
        Id = self.MemoryReader.READ_STRING(namePointer + 0x0c, 64).decode().split('\\')[4].strip('\x00')
        self.SecondaryMonster.Id = Id

    def getSecondMonsterTotalHP(self):
        Address = self.SecondaryMonster.Address
        Address = self.MemoryReader.READ_LONGLONG(Address)
        monsterHPComponent = self.MemoryReader.READ_LONGLONG(Address+0x129D8+0x48)
        monsterTotalHPAddress = monsterHPComponent + 0x60
        monsterTotalHP = self.MemoryReader.READ_FLOAT(monsterTotalHPAddress)
        if self.SecondaryMonster.Id != None and self.SecondaryMonster.Id.startswith('ems'):
            self.SecondaryMonster.TotalHP = 0
        else:
            self.SecondaryMonster.TotalHP = monsterTotalHP
        self.getSecondaryMonsterCurrentHP(monsterTotalHPAddress)
        self.Log(f'NAME: {self.SecondaryMonster.Name} | ID: {self.SecondaryMonster.Id} | HP: {int(self.SecondaryMonster.CurrentHP)}/{int(self.SecondaryMonster.TotalHP)} ({hex(monsterTotalHPAddress)})')
        self.Log(f"Target: {self.SecondaryMonster.isTarget}\n")

    def getSecondaryMonsterCurrentHP(self, totalHPAddress):
        TotalHP = self.MemoryReader.READ_FLOAT(totalHPAddress)
        currentHp = self.MemoryReader.READ_FLOAT(totalHPAddress + 0x4)
        self.SecondaryMonster.CurrentHP = currentHp if currentHp <= self.SecondaryMonster.TotalHP else 0

    ## Get 3rd info
    def GetThirdMonsterID(self):
        Address = self.ThirtiaryMonster.Address
        namePointer = self.MemoryReader.READ_LONGLONG(Address + 0x290)
        Id = self.MemoryReader.READ_STRING(namePointer + 0x0c, 64).decode().split('\\')[4].strip('\x00')
        self.ThirtiaryMonster.Id = Id

    def getThirtiaryMonsterTotalHP(self):
        Address = self.ThirtiaryMonster.Address
        monsterHPComponent = self.MemoryReader.READ_LONGLONG(Address+0x129D8+0x48)
        monsterTotalHPAddress = monsterHPComponent + 0x60
        monsterTotalHP = self.MemoryReader.READ_FLOAT(monsterTotalHPAddress)
        self.getThirtiaryMonsterCurrentHP(monsterTotalHPAddress)
        self.ThirtiaryMonster.TotalHP = int(monsterTotalHP)
        self.Log(f'NAME: {self.ThirtiaryMonster.Name} | ID: {self.ThirtiaryMonster.Id} | HP: {int(self.ThirtiaryMonster.CurrentHP)}/{int(self.ThirtiaryMonster.TotalHP)} ({hex(monsterTotalHPAddress)})')
        self.Log(f"Target: {self.ThirtiaryMonster.isTarget}\n")

    def getThirtiaryMonsterCurrentHP(self, totalHPAddress):
        TotalHP = self.MemoryReader.READ_FLOAT(totalHPAddress)
        currentHP = self.MemoryReader.READ_FLOAT(totalHPAddress + 0x4)
        self.ThirtiaryMonster.CurrentHP =  int(currentHP) if TotalHP >= int(currentHP) else 0

    # Session ID
    def getSessionID(self):
        Address = Game.BASE_ADDRESS + Game.SESSION_OFFSET
        offsets = [0xA0, 0x20, 0x80, 0x9C]
        sValue = self.MemoryReader.READ_MULTILEVEL_PTR(Address, offsets)
        SessionID = self.MemoryReader.READ_STRING(sValue+0x3C8, 12)
        self.PlayerInfo.SessionID = SessionID.decode()
        self.Log(f'Session ID: {self.PlayerInfo.SessionID} ({hex(sValue+0x3C8)})')

    def getFertilizerCount(self):
        self.PlayerInfo.HarvestBoxFertilizers = []
        Address = Game.LEVEL_ADDRESS
        firstFertilizerAddress = Address+0x6740c
        secondFertilizerAddress = firstFertilizerAddress+0x10
        thirdFertilizerAddress = secondFertilizerAddress+0x10
        fourthFertilizerAddress = thirdFertilizerAddress+0x10
        self.Log(f"FIRST FERTILIZER ADDRESS: {hex(firstFertilizerAddress)}")
        self.PlayerInfo.HarvestBoxFertilizers.append({"name":IDS.Fertilizers[self.MemoryReader.READ_INTEGER(firstFertilizerAddress-0x4)],"count":self.MemoryReader.READ_INTEGER(firstFertilizerAddress)})
        self.PlayerInfo.HarvestBoxFertilizers.append({"name":IDS.Fertilizers[self.MemoryReader.READ_INTEGER(secondFertilizerAddress-0x4)],"count":self.MemoryReader.READ_INTEGER(secondFertilizerAddress)})
        self.PlayerInfo.HarvestBoxFertilizers.append({"name":IDS.Fertilizers[self.MemoryReader.READ_INTEGER(thirdFertilizerAddress-0x4)],"count":self.MemoryReader.READ_INTEGER(thirdFertilizerAddress)})
        self.PlayerInfo.HarvestBoxFertilizers.append({"name":IDS.Fertilizers[self.MemoryReader.READ_INTEGER(fourthFertilizerAddress-0x4)],"count":self.MemoryReader.READ_INTEGER(fourthFertilizerAddress)})
        self.getHarvestInBox(fourthFertilizerAddress)

    def getHarvestInBox(self, fourthFertilizerAddress):
        Address = fourthFertilizerAddress + 0x10
        self.PlayerInfo.HarvestedItemsCounter = 0
        self.PlayerInfo.HarvestBox = []
        for address in range(Address, Address+0x1f0, 0x10):
            memoryValue = self.MemoryReader.READ_INTEGER(address)
            self.PlayerInfo.HarvestBox.append(memoryValue)
            if memoryValue > 0:
                self.PlayerInfo.HarvestedItemsCounter += 1
            
    ## Zones
    def UpdateLastZoneID(self):
        self.PlayerInfo.LastZoneID = self.PlayerInfo.ZoneID 

    # Since I have no idea how to detect which monster is being targetted
    # I'm gonna just make this "algorithm".
    def PredictTarget(self):
        if self.PlayerInfo.ZoneID in IDS.NoMonstersZones:
            self.PrimaryMonster.isTarget = False
            self.SecondaryMonster.isTarget = False
            self.ThirtiaryMonster.isTarget = False
            return
        if self.ThirtiaryMonster.TotalHP > 0:
            tMonsterPercentage = self.ThirtiaryMonster.CurrentHP / self.ThirtiaryMonster.TotalHP if (self.ThirtiaryMonster.CurrentHP / self.ThirtiaryMonster.TotalHP) > 0 else 1
        else:
            tMonsterPercentage = 1
        if self.SecondaryMonster.TotalHP > 0:
            sMonsterPercentage = self.SecondaryMonster.CurrentHP / self.SecondaryMonster.TotalHP if (self.SecondaryMonster.CurrentHP / self.SecondaryMonster.TotalHP) > 0 else 1
        else:
            sMonsterPercentage = 1
        if self.PrimaryMonster.TotalHP > 0:
            fMonsterPercentage = self.PrimaryMonster.CurrentHP / self.PrimaryMonster.TotalHP if (self.PrimaryMonster.CurrentHP / self.PrimaryMonster.TotalHP) > 0 else 1
        else:
            fMonsterPercentage = 1
        monsterHealthPercentage = [tMonsterPercentage, sMonsterPercentage, fMonsterPercentage]
        for health in sorted(monsterHealthPercentage):
            if health < 1:
                if health == tMonsterPercentage:
                    self.PrimaryMonster.isTarget = False
                    self.SecondaryMonster.isTarget = False
                    self.ThirtiaryMonster.isTarget = True
                    return
                elif health == sMonsterPercentage:
                    self.PrimaryMonster.isTarget = False
                    self.SecondaryMonster.isTarget = True
                    self.ThirtiaryMonster.isTarget = False
                    return
                elif health == fMonsterPercentage:
                    self.PrimaryMonster.isTarget = True
                    self.SecondaryMonster.isTarget = False
                    self.ThirtiaryMonster.isTarget = False
                    return
                else:
                    self.PrimaryMonster.isTarget = False
                    self.SecondaryMonster.isTarget = False
                    self.ThirtiaryMonster.isTarget = False
                    return
            elif health == 1:
                self.PrimaryMonster.isTarget = False
                self.SecondaryMonster.isTarget = False
                self.ThirtiaryMonster.isTarget = False
                continue

    def GetEquippedMantlesIDs(self):
        # Function that gets the current equipped mantles
        MantleAddress = Game.LEVEL_ADDRESS + 0x34 # Mantle address is really close to the level address
        self.GetPrimaryMantle(MantleAddress)
        self.GetSecondaryMantle(MantleAddress+0x4) # Secondary mantle is 4 bytes ahead first mantle

    def GetPrimaryMantle(self, address):
        mantleid = self.MemoryReader.READ_INTEGER(address)
        self.PlayerInfo.PrimaryMantle = mantleid
        self.Log(f"Primary mantle: {IDS.Mantles.get(mantleid)} id: {mantleid} ({hex(address)})")

    def GetSecondaryMantle(self, address):
        mantleid = self.MemoryReader.READ_INTEGER(address)
        self.PlayerInfo.SecondaryMantle = mantleid
        self.Log(f"Secondary mantle: {IDS.Mantles.get(mantleid)} id: {mantleid} ({hex(address)})\n")

    def GetEquipmentAddress(self):
        Address = Game.BASE_ADDRESS + Game.EQUIPMENT_OFFSET
        offsets = [0x90, 0x40, 0x470, 0x18]
        self.EquipmentAddress = self.MemoryReader.READ_MULTILEVEL_PTR(Address, offsets)
        self.Log(f"Equipment address: {hex(self.EquipmentAddress)}")
    
    def getMantlesTimer(self):
        self.getPrimaryMantleTimer()
        self.getSecondaryMantleTimer()

    def getPrimaryMantleTimer(self):
        primaryMantleTimerFixed = (self.PlayerInfo.PrimaryMantle * 4) + Game.timerFixed # This is the offset for the fixed timer
        primaryMantleTimer = (self.PlayerInfo.PrimaryMantle * 4) + Game.timerDynamic # This is the offset for the actual mantle timer
        primaryMantleCdFixed = (self.PlayerInfo.PrimaryMantle * 4) + Game.cooldownFixed # This is the offset for the fixed cooldown
        primaryMantleCd = (self.PlayerInfo.PrimaryMantle * 4) + Game.cooldownDynamic # this is the offset for the actual cooldown
        self.PlayerInfo.PrimaryMantleInfo[0] = self.MemoryReader.READ_FLOAT(self.EquipmentAddress + primaryMantleCdFixed)
        self.PlayerInfo.PrimaryMantleInfo[1] = self.MemoryReader.READ_FLOAT(self.EquipmentAddress + primaryMantleCd)
        self.PlayerInfo.PrimaryMantleInfo[2] = self.MemoryReader.READ_FLOAT(self.EquipmentAddress + primaryMantleTimerFixed)
        self.PlayerInfo.PrimaryMantleInfo[3] = self.MemoryReader.READ_FLOAT(self.EquipmentAddress + primaryMantleTimer)
        
    def getSecondaryMantleTimer(self):
        secondaryMantleTimerFixed = (self.PlayerInfo.SecondaryMantle * 4) + Game.timerFixed
        secondaryMantleTimer = (self.PlayerInfo.SecondaryMantle * 4) + Game.timerDynamic
        secondaryMantleCdFixed = (self.PlayerInfo.SecondaryMantle * 4) + Game.cooldownFixed
        secondaryMantleCd = (self.PlayerInfo.SecondaryMantle * 4) + Game.cooldownDynamic
        self.PlayerInfo.SecondaryMantleInfo[0] = self.MemoryReader.READ_FLOAT(self.EquipmentAddress + secondaryMantleCdFixed)
        self.PlayerInfo.SecondaryMantleInfo[1] = self.MemoryReader.READ_FLOAT(self.EquipmentAddress + secondaryMantleCd)
        self.PlayerInfo.SecondaryMantleInfo[2] = self.MemoryReader.READ_FLOAT(self.EquipmentAddress + secondaryMantleTimerFixed)
        self.PlayerInfo.SecondaryMantleInfo[3] = self.MemoryReader.READ_FLOAT(self.EquipmentAddress + secondaryMantleTimer)

    def GetPlayerWeapon(self):
        Address = Game.BASE_ADDRESS + Game.WEAPON_OFFSET
        offsets = [0x60, 0x20, 0x1C0, 0xB8]
        WeaponIdAddress = self.MemoryReader.READ_MULTILEVEL_PTR(Address, offsets)
        WeaponId = self.MemoryReader.READ_INTEGER(WeaponIdAddress+0x2B8)
        WeaponName = IDS.Weapons.get(WeaponId)
        self.PlayerInfo.Weapon_id= WeaponId
        self.PlayerInfo.Weapon_name = WeaponName
        self.Log(f"Weapon type: {WeaponName} | id: {WeaponId}\n")

    def GetPartyMembers(self):
        Address = Game.BASE_ADDRESS + Game.PARTY_OFFSET
        offsets = [0x80, 0x88, 0x30, 0xF8]
        PartyContainer = self.MemoryReader.READ_MULTILEVEL_PTR(Address, offsets) + 0x54AE5
        PartyMax = 4 # Max players a party can have
        self.PlayerInfo.PartyMembers = []
        for member in range(PartyMax):
            PartyMemberAddress = PartyContainer + (member * 0x21)
            Name = self.GetPartyMemberName(PartyMemberAddress)
            if Name[0] == "\x00": 
                # if the first byte of the name is null then that party space is empty, 
                # this happens when you're in a non-monster area after hunting, 
                # the game erases only the first byte not the whole name space
                continue
            else:
                self.PlayerInfo.PartyMembers.append(Name.strip("\x00"))
    
    def GetPartyMemberName(self, address):
        try:
            PartyMemberName = self.MemoryReader.READ_STRING(address, 32).decode()
        except:
            PartyMemberName = "\x00"
        return PartyMemberName