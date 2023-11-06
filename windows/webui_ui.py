# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'webui.ui'
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
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QDialog, QSizePolicy, QWidget)

class Ui_WebUI(object):
    def setupUi(self, WebUI):
        if not WebUI.objectName():
            WebUI.setObjectName(u"WebUI")
        WebUI.resize(1920, 1080)
        WebUI.setStyleSheet(u"background-color: #0b0f19;\n"
"background: #0b0f19;")
        self.webEngineView = QWebEngineView(WebUI)
        self.webEngineView.setObjectName(u"webEngineView")
        self.webEngineView.setGeometry(QRect(10, 10, 1900, 1068))
        self.webEngineView.setStyleSheet(u"QAbstractScrollArea {\n"
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
        self.webEngineView.setUrl(QUrl(u"about:blank"))

        self.retranslateUi(WebUI)

        QMetaObject.connectSlotsByName(WebUI)
    # setupUi

    def retranslateUi(self, WebUI):
        WebUI.setWindowTitle(QCoreApplication.translate("WebUI", u"SD MultiTool - WebUI", None))
    # retranslateUi

