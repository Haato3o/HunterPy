from Memory import *
from logger import Log
import time
from threading import Thread
import psutil

class Zones:
    ID = {
        5 : "Starting the game",
        11 : "Main menu",
        # Training area
        24 : "Training area",
        # Gathering HUB
        25 : "Gathering HUB",
        26 : "Gathering HUB",
        27 : "Gathering HUB",
        # My room
        28 : "My room",
        29 : "My room",
        30 : "My room",
        31 : "My room",
        32 : "My room",
        # Research Base
        35: "Research base",
        # Astera
        54 : "Astera",
        66 : "Astera",
        67 : "Astera",
        69 : "Astera",
        70 : "Astera",
        # Wildspire Waste

        # Ancient Forest
        197 : "Ancient Forest",
        198 : "Ancient Forest",
        199 : "Ancient Forest",
        200 : "Ancient Forest"
    }

class Game:
    baseAddress = 0x140000000   # MonsterHunterWorld.exe
    mainVariable = 0x3B5FEC8    # Level offset
    levelAddress = 0xFFFFFF     # Level address used to get name
    regionAddress = 0x3B76808   # Zone ID offset
    
    def __init__(self, pid):
        # Scanner stuff
        self.pid = pid
        self.MemoryReader = Memory(self.pid)
        self.Scanner = None
        # Player info
        self.pName = None
        self.pLevel = None
        self.pZoneID = None
        self.pZoneName = None
        
    def scanUntilDone(self):
        while psutil.pid_exists(self.pid):
            self.getPlayerLevel()
            self.getPlayerName()
            self.getPlayerZoneID()
            print('\n')
            time.sleep(1)

    def MultiThreadScan(self):
        self.Scanner = Thread(target=self.scanUntilDone)
        self.Scanner.daemon = True
        self.Scanner.start()

    def init(self):
        self.MultiThreadScan()
            
    def getPlayerName(self):
        self.pName = self.MemoryReader.readString(Game.levelAddress-64, 20).decode().strip('\x00')
        Log(f"PLAYER NAME: {self.pName} ({hex(Game.levelAddress-64)})")

    def getPlayerLevel(self):
        Address = Game.baseAddress + Game.mainVariable
        fValue = self.MemoryReader.readInteger(Address)
        ptrAddress = fValue + 144
        ptrValue = self.MemoryReader.readInteger(ptrAddress)
        Game.levelAddress = ptrValue + 0x68
        self.pLevel = self.MemoryReader.readInteger(ptrValue + 0x68)
        Log(f'HUNTER RANK: {self.pLevel} ({hex(ptrValue+0x68)})')

    def getPlayerZoneID(self):
        Address = Game.baseAddress + Game.regionAddress
        sValue = self.MemoryReader.readInteger(Address)
        offset = 0xC0
        self.pZoneID = self.MemoryReader.readInteger(sValue+offset)
        self.getPlayerZoneNameByID()
        Log(f'{self.pZoneName} | ZONE ID: {self.pZoneID} ({hex(sValue+offset)})')
        
    def getPlayerZoneNameByID(self):
        self.pZoneName = Zones.ID.get(self.pZoneID)

