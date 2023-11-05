# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QLabel,
    QMainWindow, QPlainTextEdit, QPushButton, QSizePolicy,
    QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1022, 721)
        MainWindow.setMinimumSize(QSize(1022, 721))
        MainWindow.setMaximumSize(QSize(1022, 721))
        font = QFont()
        font.setFamilies([u"JetBrains Mono"])
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgba(30, 30, 40, 1);\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QPlainTextEdit, QListView, QListWidget {\n"
"	background-color: rgba(50, 50, 70, 1);\n"
"	color: rgba(200, 200, 200, 1);\n"
"	border: 0px solid rgba(255, 255, 255, 0.3);\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QPlainTextEdit {\n"
"	padding: 10px;\n"
"}\n"
"\n"
"QPlainTextEdit#style_name, QPlainTextEdit#search_bar {\n"
"	padding: 0px 10px;\n"
"	padding-top: 3px;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: #6464A0;\n"
"	border: 0px solid rgba(255, 255, 255, 0.3);\n"
"	border-radius: 5px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:pressed  { \n"
"	background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QFrame { /*also Line, this is for PySide6*/\n"
"	border: 1px;\n"
"	border-radius: 5px;\n"
"	background-color: #6464A0;\n"
"	background-color: rgba(50, 50, 70, 1);\n"
"}\n"
"\n"
"QLabel {\n"
"	background-color: rgba(50, 50, 70, 1);\n"
"	border-radius: 7px;\n"
"	color: rgba(200, 200, 200, 1);\n"
"}\n"
"\n"
"QC"
                        "heckBox {\n"
"	border: 0px solid;\n"
"	background-color: rgba(50, 50, 70, 0);\n"
"	border-radius: 7px;\n"
"	color: rgba(200, 200, 200, 1);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 13px;\n"
"    height: 13px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"	background-color: rgba(50, 50, 70, 0);\n"
"	border-radius: 7px;\n"
"	border: 1px solid rgba(30, 30, 40, 1);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	background-color: #6464A0;\n"
"	border-radius: 7px;\n"
"	border: 1px solid rgba(30, 30, 40, 1);\n"
"	image: url(:/icons/icons/done.svg);\n"
"	border: 1px solid #6464A0;\n"
"}\n"
"\n"
"QLabel#name, QPlainTextEdit#command_editor {\n"
"	color: rgba(200, 200, 200, 1);\n"
"	background-color: rgba(30, 30, 40, 1);\n"
"	border-radius: 5px;\n"
"}\n"
"")
        self.name = QLabel(self.centralwidget)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(20, 10, 431, 41))
        font1 = QFont()
        font1.setFamilies([u"JetBrains Mono NL"])
        font1.setPointSize(16)
        self.name.setFont(font1)
        self.tools_label = QLabel(self.centralwidget)
        self.tools_label.setObjectName(u"tools_label")
        self.tools_label.setGeometry(QRect(620, 70, 71, 41))
        self.tools_label.setFont(font1)
        self.settings = QLabel(self.centralwidget)
        self.settings.setObjectName(u"settings")
        self.settings.setGeometry(QRect(20, 60, 561, 641))
        self.settings.setStyleSheet(u"")
        self.tools = QLabel(self.centralwidget)
        self.tools.setObjectName(u"tools")
        self.tools.setGeometry(QRect(600, 60, 401, 641))
        self.optimizations_label = QLabel(self.centralwidget)
        self.optimizations_label.setObjectName(u"optimizations_label")
        self.optimizations_label.setGeometry(QRect(30, 70, 171, 41))
        self.optimizations_label.setFont(font1)
        self.cache_chbox = QCheckBox(self.centralwidget)
        self.cache_chbox.setObjectName(u"cache_chbox")
        self.cache_chbox.setGeometry(QRect(310, 110, 121, 20))
        self.cache_chbox.setFont(font)
        self.pytorch_chbox = QCheckBox(self.centralwidget)
        self.pytorch_chbox.setObjectName(u"pytorch_chbox")
        self.pytorch_chbox.setGeometry(QRect(310, 130, 191, 20))
        self.pytorch_chbox.setFont(font)
        self.xformers_chbox = QCheckBox(self.centralwidget)
        self.xformers_chbox.setObjectName(u"xformers_chbox")
        self.xformers_chbox.setGeometry(QRect(40, 110, 121, 20))
        self.xformers_chbox.setFont(font)
        self.xformers_chbox.setStyleSheet(u"")
        self.opt_sdp_chbox = QCheckBox(self.centralwidget)
        self.opt_sdp_chbox.setObjectName(u"opt_sdp_chbox")
        self.opt_sdp_chbox.setGeometry(QRect(40, 130, 121, 20))
        self.opt_sdp_chbox.setFont(font)
        self.vram_med_sdxl_chbox = QCheckBox(self.centralwidget)
        self.vram_med_sdxl_chbox.setObjectName(u"vram_med_sdxl_chbox")
        self.vram_med_sdxl_chbox.setGeometry(QRect(170, 150, 111, 20))
        self.vram_med_sdxl_chbox.setFont(font)
        self.vram_med_chbox = QCheckBox(self.centralwidget)
        self.vram_med_chbox.setObjectName(u"vram_med_chbox")
        self.vram_med_chbox.setGeometry(QRect(170, 130, 81, 20))
        self.vram_med_chbox.setFont(font)
        self.vram_low_chbox = QCheckBox(self.centralwidget)
        self.vram_low_chbox.setObjectName(u"vram_low_chbox")
        self.vram_low_chbox.setGeometry(QRect(170, 110, 100, 20))
        self.vram_low_chbox.setFont(font)
        self.no_half_chbox = QCheckBox(self.centralwidget)
        self.no_half_chbox.setObjectName(u"no_half_chbox")
        self.no_half_chbox.setGeometry(QRect(40, 170, 71, 20))
        self.no_half_chbox.setFont(font)
        self.no_half_vae_chbox = QCheckBox(self.centralwidget)
        self.no_half_vae_chbox.setObjectName(u"no_half_vae_chbox")
        self.no_half_vae_chbox.setGeometry(QRect(40, 190, 101, 20))
        self.no_half_vae_chbox.setFont(font)
        self.optimizations_label_2 = QLabel(self.centralwidget)
        self.optimizations_label_2.setObjectName(u"optimizations_label_2")
        self.optimizations_label_2.setGeometry(QRect(30, 210, 171, 41))
        self.optimizations_label_2.setFont(font1)
        self.autoupdate_chbox = QCheckBox(self.centralwidget)
        self.autoupdate_chbox.setObjectName(u"autoupdate_chbox")
        self.autoupdate_chbox.setGeometry(QRect(40, 250, 101, 20))
        self.autoupdate_chbox.setFont(font)
        self.dark_theme_chbox = QCheckBox(self.centralwidget)
        self.dark_theme_chbox.setObjectName(u"dark_theme_chbox")
        self.dark_theme_chbox.setGeometry(QRect(170, 250, 91, 20))
        self.dark_theme_chbox.setFont(font)
        self.autolaunch_chbox = QCheckBox(self.centralwidget)
        self.autolaunch_chbox.setObjectName(u"autolaunch_chbox")
        self.autolaunch_chbox.setGeometry(QRect(40, 270, 101, 20))
        self.autolaunch_chbox.setFont(font)
        self.listen_chbox = QCheckBox(self.centralwidget)
        self.listen_chbox.setObjectName(u"listen_chbox")
        self.listen_chbox.setGeometry(QRect(170, 270, 91, 20))
        self.listen_chbox.setFont(font)
        self.result_label = QLabel(self.centralwidget)
        self.result_label.setObjectName(u"result_label")
        self.result_label.setGeometry(QRect(30, 300, 171, 41))
        self.result_label.setFont(font1)
        self.command_editor = QPlainTextEdit(self.centralwidget)
        self.command_editor.setObjectName(u"command_editor")
        self.command_editor.setGeometry(QRect(30, 340, 541, 281))
        self.command_editor.setFont(font)
        self.command_editor.setStyleSheet(u"QAbstractScrollArea {\n"
"	padding: 5px 6px 5px 0;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::vertical {\n"
"    border: 0px solid rgba(50, 50, 70, 1);\n"
"    background: rgba(30, 30, 40, 1);\n"
"    width: 10px;\n"
"	border-radius: 3px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #6464A0;\n"
"    border-radius: 2px;\n"
"    min-height: 0px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: 0px solid grey;\n"
"    background: rgba(50, 50, 70, 1);\n"
"    height: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: 0px solid grey;\n"
"    background: rgba(50, 50, 70, 1);\n"
"    height: 0px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    border: 0px solid grey;\n"
"    width: 0px;\n"
"    height: 0px;\n"
"    background: rgba(50, 50, 70, 1);\n"
"}\n"
"\n"
"QScrollBar::add-page:ve"
                        "rtical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}")
        self.command_editor.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.start_button = QPushButton(self.centralwidget)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setGeometry(QRect(30, 630, 371, 61))
        self.start_button.setFont(font1)
        self.set_recommended_button = QPushButton(self.centralwidget)
        self.set_recommended_button.setObjectName(u"set_recommended_button")
        self.set_recommended_button.setGeometry(QRect(410, 630, 161, 61))
        font2 = QFont()
        font2.setFamilies([u"JetBrains Mono NL"])
        self.set_recommended_button.setFont(font2)
        self.styles_editor_button = QPushButton(self.centralwidget)
        self.styles_editor_button.setObjectName(u"styles_editor_button")
        self.styles_editor_button.setGeometry(QRect(610, 110, 181, 61))
        font3 = QFont()
        font3.setFamilies([u"JetBrains Mono NL"])
        font3.setPointSize(10)
        self.styles_editor_button.setFont(font3)
        self.start_button_3 = QPushButton(self.centralwidget)
        self.start_button_3.setObjectName(u"start_button_3")
        self.start_button_3.setGeometry(QRect(800, 140, 191, 61))
        self.start_button_3.setFont(font3)
        self.prompt_reader_button = QPushButton(self.centralwidget)
        self.prompt_reader_button.setObjectName(u"prompt_reader_button")
        self.prompt_reader_button.setGeometry(QRect(800, 210, 191, 61))
        self.prompt_reader_button.setFont(font3)
        self.prompt_reader_lite_button = QPushButton(self.centralwidget)
        self.prompt_reader_lite_button.setObjectName(u"prompt_reader_lite_button")
        self.prompt_reader_lite_button.setGeometry(QRect(610, 180, 181, 61))
        self.prompt_reader_lite_button.setFont(font3)
        self.cuda_visible_devices_chox = QCheckBox(self.centralwidget)
        self.cuda_visible_devices_chox.setObjectName(u"cuda_visible_devices_chox")
        self.cuda_visible_devices_chox.setGeometry(QRect(310, 170, 171, 20))
        self.cuda_visible_devices_chox.setFont(font)
        self.safetensors_chbox = QCheckBox(self.centralwidget)
        self.safetensors_chbox.setObjectName(u"safetensors_chbox")
        self.safetensors_chbox.setGeometry(QRect(310, 190, 171, 20))
        self.safetensors_chbox.setFont(font)
        self.lazy_loading_chbox = QCheckBox(self.centralwidget)
        self.lazy_loading_chbox.setObjectName(u"lazy_loading_chbox")
        self.lazy_loading_chbox.setGeometry(QRect(310, 150, 171, 20))
        self.lazy_loading_chbox.setFont(font)
        self.about = QPushButton(self.centralwidget)
        self.about.setObjectName(u"about")
        self.about.setGeometry(QRect(810, 630, 181, 61))
        self.about.setFont(font3)
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(30, 110, 16, 40))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(30, 170, 16, 40))
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(160, 110, 16, 61))
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.line_4 = QFrame(self.centralwidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(300, 150, 20, 61))
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.line_5 = QFrame(self.centralwidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(300, 110, 20, 41))
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)
        self.line_6 = QFrame(self.centralwidget)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setGeometry(QRect(30, 250, 16, 40))
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)
        self.line_7 = QFrame(self.centralwidget)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setGeometry(QRect(160, 250, 16, 40))
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)
        MainWindow.setCentralWidget(self.centralwidget)
        self.tools.raise_()
        self.name.raise_()
        self.tools_label.raise_()
        self.settings.raise_()
        self.optimizations_label.raise_()
        self.optimizations_label_2.raise_()
        self.result_label.raise_()
        self.command_editor.raise_()
        self.start_button.raise_()
        self.set_recommended_button.raise_()
        self.styles_editor_button.raise_()
        self.start_button_3.raise_()
        self.prompt_reader_button.raise_()
        self.prompt_reader_lite_button.raise_()
        self.about.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.no_half_vae_chbox.raise_()
        self.no_half_chbox.raise_()
        self.opt_sdp_chbox.raise_()
        self.xformers_chbox.raise_()
        self.line_3.raise_()
        self.vram_low_chbox.raise_()
        self.vram_med_sdxl_chbox.raise_()
        self.vram_med_chbox.raise_()
        self.line_4.raise_()
        self.cuda_visible_devices_chox.raise_()
        self.safetensors_chbox.raise_()
        self.lazy_loading_chbox.raise_()
        self.line_5.raise_()
        self.cache_chbox.raise_()
        self.pytorch_chbox.raise_()
        self.line_6.raise_()
        self.line_7.raise_()
        self.autolaunch_chbox.raise_()
        self.listen_chbox.raise_()
        self.autoupdate_chbox.raise_()
        self.dark_theme_chbox.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Stable Diffusion webUI Multi Tool by Wiered", None))
        self.name.setText(QCoreApplication.translate("MainWindow", u"Stable Diffusion webUI multi tool", None))
        self.tools_label.setText(QCoreApplication.translate("MainWindow", u"Tools", None))
        self.settings.setText("")
        self.tools.setText("")
        self.optimizations_label.setText(QCoreApplication.translate("MainWindow", u"Optimizations", None))
        self.cache_chbox.setText(QCoreApplication.translate("MainWindow", u"cache cleaner", None))
        self.pytorch_chbox.setText(QCoreApplication.translate("MainWindow", u"pytorch cuda alloc conf", None))
        self.xformers_chbox.setText(QCoreApplication.translate("MainWindow", u"xformers(Nvid)", None))
        self.opt_sdp_chbox.setText(QCoreApplication.translate("MainWindow", u"opt-sdp(AMD)", None))
        self.vram_med_sdxl_chbox.setText(QCoreApplication.translate("MainWindow", u"medvram-sdxl", None))
        self.vram_med_chbox.setText(QCoreApplication.translate("MainWindow", u"medvram", None))
        self.vram_low_chbox.setText(QCoreApplication.translate("MainWindow", u"lowvram", None))
        self.no_half_chbox.setText(QCoreApplication.translate("MainWindow", u"no half", None))
        self.no_half_vae_chbox.setText(QCoreApplication.translate("MainWindow", u"no half vae", None))
        self.optimizations_label_2.setText(QCoreApplication.translate("MainWindow", u"Other", None))
        self.autoupdate_chbox.setText(QCoreApplication.translate("MainWindow", u"auto update", None))
        self.dark_theme_chbox.setText(QCoreApplication.translate("MainWindow", u"dark theme", None))
        self.autolaunch_chbox.setText(QCoreApplication.translate("MainWindow", u"auto launch", None))
        self.listen_chbox.setText(QCoreApplication.translate("MainWindow", u"listen", None))
        self.result_label.setText(QCoreApplication.translate("MainWindow", u"Result", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"Launch", None))
        self.set_recommended_button.setText(QCoreApplication.translate("MainWindow", u"Set recommended", None))
        self.styles_editor_button.setText(QCoreApplication.translate("MainWindow", u"Styles Editor", None))
        self.start_button_3.setText(QCoreApplication.translate("MainWindow", u"(WIP)", None))
        self.prompt_reader_button.setText(QCoreApplication.translate("MainWindow", u"SD Prompt reader", None))
        self.prompt_reader_lite_button.setText(QCoreApplication.translate("MainWindow", u"SD prompt reader lite", None))
        self.cuda_visible_devices_chox.setText(QCoreApplication.translate("MainWindow", u"cuda visible devices", None))
        self.safetensors_chbox.setText(QCoreApplication.translate("MainWindow", u"safetensors fast gpu", None))
        self.lazy_loading_chbox.setText(QCoreApplication.translate("MainWindow", u"lazy loading", None))
        self.about.setText(QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

