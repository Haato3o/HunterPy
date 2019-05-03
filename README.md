[![pypresence](https://img.shields.io/badge/using-pypresence-00bb88.svg?style=for-the-badge&logo=discord&logoWidth=20)](https://github.com/qwertyquerty/pypresence)
# Hunter Py
HunterPy is a software that reads the game memory (only reads, it doesn't write anything to it) to find the necessary data for the discord rich presence and to update the overlay with useful stuff.

# Installation
You can download the version 2.0.84 [here](https://github.com/Haato3o/HunterPy/releases/tag/v2.0.84), then run the HunterPy.exe and it'll check for updates automatically and download all latest files available.

# How to use
## Rich presence
The discord integration is enabled by default, you just need to open your game and let HunterPy running in the background, however it can be disabled anytime by opening the `config.json` and setting the `RichPresence` from `true` to `false`.

## Overlay
**THE OVERLAY ONLY WORKS WHEN THE GAME IS IN BORDERLESS FULLSCREEN OR WINDOWED!**
HunterPy has a overlay that can be toggled on/off in the `config.json`. You can also disable any of the widgets in the overlay separately in case you don't like one of them as well as change the widgets position.
### Monster health
Shows monsters name, current health, total health and has a health bar.

### Harvest Box
Shows the fertilizer names and the amount you have active, total items in harvest box. It only appears when in no monster areas such as Astera, Gathering Hub, etc.

### Mantles Cooldown (Not done yet)
Shows the mantles cooldown and timer when wearing one, this widget only appears when the cooldown and timer are actually running.

### More widgets and info to be added soon...

## Credits
+ [R00telement](https://github.com/r00telement) for his [SmartHunter](https://github.com/r00telement/SmartHunter) application that helped me finding the monsters health
+ [Ezekial711](https://github.com/Ezekial711) for his [modding guide](https://github.com/Ezekial711/MonsterHunterWorldModding) that helped me find and map all mantles