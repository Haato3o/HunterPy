import pypresence

class DiscordPresence:
    ClientID = '567152028070051859'

    def __init__(self):
        self.Connected = False
        self.Discord = pypresence.Presence(DiscordPresence.ClientID)

    def connect(self):
        if self.Connected == False:
            self.Discord.connect()
            self.Connected = True

    def disconnect(self):
        if self.Connected:
            self.Discord.close()
            self.Connected = False

    def clearPresence(self):
        self.Discord.clear()

    def changePresence(self, **kwargs):
        self.Discord.update(**kwargs)

    def start(self):
        self.connect()