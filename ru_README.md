<div align="center">
<img src="images/mt-logo.ico" alt="logo" width="100"/>

# Stable Diffusion WebUI Multi Tool

[Русский](https://github.com/wiered/sd-multi-tool/blob/master/ru_README.md) | [English](https://github.com/wiered/sd-multi-tool/blob/master/README.md)

Почти самостоятельное дополнение для Stable Diffusion WebUI.

<img src="images/screenshoot.png" alt="screenshoot" width ="800"/>

<div align="left">

## Инструменты

<div align="center">

|              | Current features:  |              |
|--------------|--------------------|--------------|
| [Run WebUI](#run-webui) | [Styles Editor](#styles-editor) | [SD Prompt Reader](#sd-prompt-reader) |

<div align="left">

## Run WebUI

Нельзя использовать в самостоятельном режиме.

### Установка оптимальных настроек нажатием одной кнопки!

С этим инструментом вы можете легко настроить батник для запуска WebUI, добавив
    часто используемые настройки в него и запустить WebUI.

Батник создаётся из текста в окне `Result`, так что вы легко можете добавить свои настройки туда
    и программа их подхватит.

Программа автоматически сохраняет и загружает ваши настройки после выхода и запуска.

Это так же главное окно программы.

## Styles Editor

Можно использовать в самостоятельном режиме.

Инструмент для любителей создания своих стилей.

Пока что он очень прост, но с следующим апдейтом, что-то прикольное может случится.

## SD Prompt Reader

Lite версию можно использовать в самостоятельном режиме.

Простой инструмент для просмотра промта картинок сгенерированных с помошью Stable Diffusion.

Весь бэкэнд нагло сворован с [этого репозитория](https://github.com/receyuki/stable-diffusion-prompt-reader).

Большое им спасибо!

## Установка

Приложение можно использовать самостоятельно или вместе с `SD WebUI by Automatic1111` или `SD Prompt Viewer by receyuki`.

_Styles editor_ и _SD Prompt Reader Lite_ могут быть использованны самостоятельно.

### Установка без коннекта

1) Просто скачайте и откройте SDMT из [Releases](https://github.com/wiered/sd-multi-tool/releases).

### Установка под Stable Diffusion WebUI

1) Cкачайте SDMT отсюда [Releases](https://github.com/wiered/sd-multi-tool/releases).
2) Переместите `SDMT.exe` в корень SD WebUI ( туда, где лежит ваша папка с моделями, но не в неё ).
3) Запустите `SDMT.exe`.
4) Дополнительный шаг: Вы можете создать ярылык SDMT на рабочем столе запускать с него как SDMT, так и Stable Diffusion WebUI.

### Установка SD Prompt Reader

1) Cкачайте SDMT отсюда [Releases](https://github.com/wiered/sd-multi-tool/releases).
2) Скачайте SD Prompt Viewer отсюда [Releases](https://github.com/receyuki/stable-diffusion-prompt-reader/releases).
3) Переместите `SD Prompt Reader.exe` в туже папку, где находится `SDMT.exe` (Не переименовывайте SD Prompt Viewer).

## FAQ

### Если у вас ругается антивирус

The false positive reported by some anti-malwares is caused by the packaging tool _`pyinstaller`_ which is a common issue for _`pyinstaller`_ users. 

## Credits

+ Спасибо [Stable Diffusion webUI](https://github.com/AUTOMATIC1111/stable-diffusion-webui/) за то, что открыли мне мир генерации картинок.
+ Вдохновлён [SD Prompt reader](https://github.com/receyuki/stable-diffusion-prompt-reader).
+ Иконки кнопочек [Google Material Symbols](https://fonts.google.com/icons), thanks!
+ Спасибо JetBrains за их супер крутой [JetBrainsMono](https://github.com/JetBrains/JetBrainsMono/tree/master) шрифт.
