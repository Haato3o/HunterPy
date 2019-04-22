import psutil
import HunterPy
from presence import DiscordPresence
import time, sys
from threading import Thread

class MHWPresence:
    def __init__(self):
        self.Scanning = False
        self.GamePID = None
        #self.waitGameOpen()
        self.ThreadScanGamePID()
        self.Player = None
        self.PlayerInfo = None
        self.Presence = DiscordPresence()
        self.Target = None
        self.MonstersIds = HunterPy.IDS.Monsters
        self.ConsoleMessage = []

    def Log(self, string):
        self.ConsoleMessage = []
        self.ConsoleMessage.append(string)

    def ScanPIDs(self):
        for process in psutil.process_iter():
            if process.name() == 'MonsterHunterWorld.exe':
                self.GamePID = process.pid
                self.Log(f'MonsterHunterWorld.exe found! PID: {process.pid}')
                return
        self.Log('"MonsterHunterWorld.exe" not found!')
        self.GamePID = None

    def waitGameOpen(self):
        while self.GamePID == None:
            self.ScanPIDs()
            if self.GamePID != None:
                self.Start()
            time.sleep(1.5)

    def ThreadScanGamePID(self):
        scanner = Thread(target=self.waitGameOpen)
        scanner.daemon = True
        scanner.start()

    def getLocationImage(self):
        if self.PlayerInfo.ZoneName == None:
            return
        return self.PlayerInfo.ZoneName.lower().replace(' ', '-').replace("'", "")

    def formatAndGetDetails(self):
        noMonsterZones = HunterPy.IDS.NoMonstersZones
        if self.Player.PlayerInfo.ZoneID == 0:
            return None
        if self.PlayerInfo.ZoneName == "Main Menu" or self.PlayerInfo.ZoneID in noMonsterZones:
            return "Idle"
        if self.Player.PrimaryMonster.isTarget:
            return f"Hunting {self.Player.PrimaryMonster.Name}".replace("None", "Monster")
        elif self.Player.SecondaryMonster.isTarget:
            return f"Hunting {self.Player.SecondaryMonster.Name}".replace("None", "Monster")
        elif self.Player.ThirtiaryMonster.isTarget:
            return f"Hunting {self.Player.ThirtiaryMonster.Name}".replace("None", "Monster")
        else:
            return f"Exploring"
        

    def getTargetHP(self):
        noMonsterZones = HunterPy.IDS.NoMonstersZones
        if self.Player.PlayerInfo.ZoneID in noMonsterZones:
            return None
        if self.Player.PrimaryMonster.isTarget:
            curHP = self.Player.PrimaryMonster.CurrentHP
            totalHp = self.Player.PrimaryMonster.TotalHP
        elif self.Player.SecondaryMonster.isTarget:
            curHP = self.Player.SecondaryMonster.CurrentHP
            totalHp = self.Player.SecondaryMonster.TotalHP
        elif self.Player.ThirtiaryMonster.isTarget:
            curHP = self.Player.ThirtiaryMonster.CurrentHP
            totalHp = self.Player.ThirtiaryMonster.TotalHP
        else:
            return None
        try:
            return f'HP: {int(curHP/totalHp*100)}%'
        except:
            return None


    def presenceUpdate(self):
        if self.PlayerInfo.Name == "":
            return
        self.Presence.changePresence(
            pid = self.GamePID,
            details = self.formatAndGetDetails(),
            state = self.getTargetHP(),
            large_text = self.PlayerInfo.ZoneName,
            large_image = self.getLocationImage() if self.PlayerInfo.ZoneID in HunterPy.IDS.Zones else "main-menu",
            small_image = 'hunter-rank',
            small_text = f'{self.PlayerInfo.Name} | Hunter Rank: {self.PlayerInfo.Level}'
        )

    def GetMessageFromHunterPy(self):
        while self.Scanning:
            self.ConsoleMessage = []
            self.ConsoleMessage.append("".join(self.Player.Logger))
            time.sleep(0.5)

    def ScannerConsole(self):
        s = Thread(target=self.GetMessageFromHunterPy)
        s.daemon = True
        s.start()

    def Start(self):
        try:
            while True:
                
                if self.GamePID == None or psutil.pid_exists(self.GamePID) == False:
                    self.ScanPIDs()
                    self.Presence.clearPresence()
                    self.Scanning = False
                    time.sleep(1.5)
                    continue
                elif self.GamePID != None and self.Scanning == False:
                    self.Player = HunterPy.Game(self.GamePID)
                    self.PlayerInfo = self.Player.PlayerInfo
                    self.Player.init()
                    self.Presence.connect()
                    self.Scanning = True
                    self.ScannerConsole()
                self.presenceUpdate()
                time.sleep(10)
        except KeyboardInterrupt:
            print("Exiting...")