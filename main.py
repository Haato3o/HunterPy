import psutil
import HunterPy
from presence import DiscordPresence
import time, sys

class MHWPresence:
    def __init__(self):
        self.Scanning = False
        self.GamePID = None
        self.waitGameOpen()
        self.Player = None
        self.PlayerInfo = None
        self.Presence = DiscordPresence()
        self.elpsedTime = None

    def ScanPIDs(self):
        for process in psutil.process_iter():
            if process.name() == 'MonsterHunterWorld.exe':
                self.GamePID = process.pid
                print(f'MonsterHunterWorld.exe found! PID: {process.pid}')
                return
        print('Game not found!')
        self.GamePID = None

    def waitGameOpen(self):
        while self.GamePID == None:
            self.ScanPIDs()
    
    def getLocationImage(self):
        if self.PlayerInfo.ZoneName == None:
            return
        return self.PlayerInfo.ZoneName.lower().replace(' ', '-').replace("'", "")

    def formatAndGetDetails(self):
        return "Hunting: {MONSTER NAME HERE}"

    def getTargetHP(self):
        if self.Player.PrimaryMonster.isTarget:
            curHP = self.Player.PrimaryMonster.CurrentHP
            totalHp = self.Player.PrimaryMonster.TotalHP
        elif self.Player.SecondaryMonster.isTarget:
            curHP = self.Player.SecondaryMonster.CurrentHP
            totalHp = self.Player.SecondaryMonster.TotalHP
        elif self.Player.ThirtiaryMonster.isTarget:
            curHP = self.Player.ThirtiaryMonster.CurrentHP
            totalHp = self.Player.ThirtiaryMonster.TotalHP
        try:
            return f'{int(curHP)}/{int(totalHp)}'
        except:
            return None

    def getElapsedTime(self):
        self.elpsedTime = time.time()

    def presenceUpdate(self):
        self.Presence.changePresence(
            details = self.formatAndGetDetails(),
            state = self.getTargetHP(),
            large_text = self.PlayerInfo.ZoneName,
            large_image = self.getLocationImage() if self.PlayerInfo.ZoneID in HunterPy.IDS.Zones else "main-menu",
            small_image = 'hunter-rank',
            small_text = f'{self.PlayerInfo.Name} | Hunter Rank: {self.PlayerInfo.Level}'
        )

    def Start(self):
        try:
            while True:
                if self.GamePID == None or psutil.pid_exists(self.GamePID) == False:
                    self.GamePID = None
                    self.Presence.clearPresence()
                    self.Scanning = False
                    self.ScanPIDs()
                if self.GamePID != None and self.Scanning == False:
                    self.Player = HunterPy.Game(self.GamePID)
                    self.PlayerInfo = self.Player.PlayerInfo
                    self.Player.init()
                    self.Presence.connect()
                    self.Scanning = True
                elif self.GamePID == None:
                    self.Presence.clearPresence()
                    self.Scanning = False
                    continue
                self.presenceUpdate()
                time.sleep(10)
        except KeyboardInterrupt:
            print("Exiting...")

if __name__ == "__main__":
    Presence = MHWPresence()
    Presence.Start()