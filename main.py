import psutil
import HunterPy
from presence import DiscordPresence
import time

class MHWPresence:
    def __init__(self):
        self.Scanning = False
        self.GamePID = None
        self.waitGameOpen()
        self.Player = None
        self.Presence = DiscordPresence()

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
        if self.Player.pZoneName == None:
            return
        return self.Player.pZoneName.lower().replace(' ', '-').replace("'", "")

    def presenceUpdate(self):
        self.Presence.changePresence(
            large_text = self.Player.pZoneName,
            large_image = self.getLocationImage() if self.Player.pZoneID in HunterPy.Zones.ID else "main-menu",
            small_image = 'hunter-rank',
            small_text = f'{self.Player.pName} | Hunter Rank: {self.Player.pLevel}'
        )

    def Start(self):
        while True:
            if self.GamePID == None or psutil.pid_exists(self.GamePID) == False:
                self.ScanPIDs()
            if self.GamePID != None and self.Scanning == False:
                self.Player = HunterPy.Game(self.GamePID)
                self.Player.init()
                self.Presence.connect()
                self.Scanning = True
            elif self.GamePID == None:
                self.Presence.clearPresence()
                self.Scanning = False
                continue
            self.presenceUpdate()
            time.sleep(10)
if __name__ == "__main__":
    Presence = MHWPresence()
    Presence.Start()