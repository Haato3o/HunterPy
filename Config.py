# Module to load and make config whenever needed

import json

class Config:
    Path = "config.json"
    Layout = {
        "Overlay" : {
            "Enabled" : False,
            "Position": [0, 0],
            "MonstersComponent" : {
                "Enabled" : True,
                "Position": [0, 0]
            },
            "HarvestBoxComponent" : {
                "Enabled" : True,
                "Position" : [1160, 30]
            },
            "PrimaryMantle" : {
                "Enabled" : True,
                "Position" : [1170, 500]
            },
            "SecondaryMantle" : {
                "Enabled" : True,
                "Position" : [1170, 540]
            }
        },
        "RichPresence" : {
            "Enabled" : True
        }
    }
    def __init__(self):
        self.ValidateJson()
        self.Config = None
        
    
    def ValidateJson(self):
        self.LoadConfig()
        for key in Config.Layout:
            if key not in self.Config:
                self.Config[key] = {}
            for subkey in Config.Layout[key]:
                if subkey not in self.Config[key]:
                    self.Config[key][subkey] = Config.Layout[key][subkey]
        self.SaveConfig()

    def LoadConfig(self):
        try:
            file = open(Config.Path, 'r')
            self.Config = json.load(file)
            file.close()
        except FileNotFoundError:
            self.MakeConfig()
            self.LoadConfig()
        except json.decoder.JSONDecodeError:
            pass
    
    def MakeConfig(self):
        file = open(Config.Path, 'w')
        json.dump(Config.Layout, file, indent=4)
        file.close()

    def SaveConfig(self):
        file = open(Config.Path, 'w')
        json.dump(self.Config, file, indent=4)
        file.close()