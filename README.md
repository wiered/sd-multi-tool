<div align="center">
<img src="images/mt-logo.ico" alt="logo" width="100"/>

# Stable Diffusion WebUI Multi Tool

[Русский](https://github.com/wiered/sd-multi-tool/blob/master/ru_README.md) | [English](https://github.com/wiered/sd-multi-tool/blob/master/README.md)

A half standalone feature-rich tool for a Stable Diffusion WebUI.

<img src="images/screenshoot.png" alt="screenshoot" width ="800"/>

<div align="left">

## Features

|              | Current features:  |              |
|--------------|--------------------|--------------|
| [Run WebUI](#run-webui) | [Styles Editor](#styles-editor) | [SD Prompt Reader](#sd-prompt-reader) |


## Run WebUI

Can't be used in standalone mode.

### Setup optimal settings with one button!

With this tool you can easily set up your bat file, add most common settings to it
    and run the Stable Diffusion web UI.

Bat file creating from Result's widget plain text, so you can add your own settings to it
    and it will add them to file.

Programm autosaves all your settings, and will load it automatically.

Also this is main window of program.

## Styles Editor

Can be used in standalone mode

This tool created for these who love create and edit styles.

For now it's very simple, but with next update, something very cool will happen.

## SD Prompt Reader

Lite version can be used in standalone mode. 

Just easy to use Prompt Reader for images generated with Stable Diffusion.

All backend code for this tool taken form this [Github repository](https://github.com/receyuki/stable-diffusion-prompt-reader).
Massive thanks!

## Installation

App can be used standalone or connected with `SD WebUI by Automatic1111` or `SD Prompt Viewer by receyuki`

Styles editor and SD Prompt Reader Lite can be used in standalone mode.

### Standalone installation

Just download SDMT from [Releases](https://github.com/wiered/sd-multi-tool/releases) and open it.

### Connecting to SD WebUI by Automatic1111

1) Download SDMT from [Releases](https://github.com/wiered/sd-multi-tool/releases)
2) Move `SDMT.exe` to the root folder of SD WebUI ( where models folder is located )
3) Run `SDMT.exe`
4) Additional step: You can create SDMT shortcut on your Desktop and run SDMT and WebUI with this shortcut

### Connecting with SD Prompt Viewer by receyuki

1) Download SDMT from [Releases](https://github.com/wiered/sd-multi-tool/releases)
2) Download SD Prompt Viewer from [Releases](https://github.com/receyuki/stable-diffusion-prompt-reader/releases)
3) Move `SD Prompt Reader.exe` to same directory `SDMT.exe` file located. (Don't rename SD Prompt Viewer)

## FAQ

### Malware Alert

The false positive reported by some anti-malwares is caused by the packaging tool _`pyinstaller`_ which is a common issue for _`pyinstaller`_ users. 

## Credits

+ Big thanks for [Stable Diffusion webUI](https://github.com/AUTOMATIC1111/stable-diffusion-webui/) for introducing me to the world of AI Generated images.
+ Inspired by [SD Prompt reader](https://github.com/receyuki/stable-diffusion-prompt-reader).
+ Inapp icons from [Google Material Symbols](https://fonts.google.com/icons), thanks!
+ Thanks JetBrains for creating their [JetBrainsMono](https://github.com/JetBrains/JetBrainsMono/tree/master) font.
