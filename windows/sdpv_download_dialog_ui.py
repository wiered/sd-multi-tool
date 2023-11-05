# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sdpv_download_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QProgressBar,
    QPushButton, QSizePolicy, QWidget)

class Ui_SDPromptReaderDownloader(object):
    def setupUi(self, SDPromptReaderDownloader):
        if not SDPromptReaderDownloader.objectName():
            SDPromptReaderDownloader.setObjectName(u"SDPromptReaderDownloader")
        SDPromptReaderDownloader.resize(400, 300)
        SDPromptReaderDownloader.setStyleSheet(u"QDialog {\n"
"	background-color: rgba(30, 30, 40, 1);\n"
"}\n"
"\n"
"QLabel {\n"
"	color: rgba(200, 200, 200, 1);\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: #6464A0;\n"
"	border: 0px solid rgba(255, 255, 255, 0.3);\n"
"	border-radius: 7px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:pressed  { \n"
"	background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QProgressBar {\n"
"	background-color: rgba(50, 50, 70, 1);;\n"
"    color: rgba(200, 200, 200, 1);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgba(50, 50, 70, 1);;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"	background-color: #6464A0;\n"
"	border-radius: 5px;\n"
"}")
        self.label = QLabel(SDPromptReaderDownloader)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 381, 211))
        font = QFont()
        font.setFamilies([u"JetBrains Mono NL"])
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.download_button = QPushButton(SDPromptReaderDownloader)
        self.download_button.setObjectName(u"download_button")
        self.download_button.setEnabled(True)
        self.download_button.setGeometry(QRect(20, 260, 171, 31))
        self.download_button.setFont(font)
        self.download_button.setAutoDefault(True)
        self.download_button.setFlat(False)
        self.github_button = QPushButton(SDPromptReaderDownloader)
        self.github_button.setObjectName(u"github_button")
        self.github_button.setGeometry(QRect(210, 260, 171, 31))
        self.github_button.setFont(font)
        self.progressBar = QProgressBar(SDPromptReaderDownloader)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setEnabled(False)
        self.progressBar.setGeometry(QRect(20, 230, 361, 23))
        self.progressBar.setToolTipDuration(-1)
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QProgressBar.TopToBottom)

        self.retranslateUi(SDPromptReaderDownloader)

        QMetaObject.connectSlotsByName(SDPromptReaderDownloader)
    # setupUi

    def retranslateUi(self, SDPromptReaderDownloader):
        SDPromptReaderDownloader.setWindowTitle(QCoreApplication.translate("SDPromptReaderDownloader", u"SD Prompt Reader Downloader", None))
        self.label.setText(QCoreApplication.translate("SDPromptReaderDownloader", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Stable Diffusion Prompt Reader</span></p><p><span style=\" font-size:12pt;\">Consider downloading </span><a href=\"https://github.com/receyuki/stable-diffusion-prompt-reader\"><span style=\" font-size:12pt; font-weight:700; text-decoration: underline; color:#00d7d7;\">Stable Diffusion Prompt Reader</span></a><span style=\" font-size:12pt;\">, if you want more advanced use of this tool.</span></p></body></html>", None))
        self.download_button.setText(QCoreApplication.translate("SDPromptReaderDownloader", u"Download", None))
        self.github_button.setText(QCoreApplication.translate("SDPromptReaderDownloader", u"GitHub", None))
#if QT_CONFIG(tooltip)
        self.progressBar.setToolTip("")
#endif // QT_CONFIG(tooltip)
    # retranslateUi

