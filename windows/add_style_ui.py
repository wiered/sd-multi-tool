# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_style.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QPlainTextEdit, QPushButton,
    QSizePolicy, QWidget)
import res_rc

class Ui_NewStyleDialog(object):
    def setupUi(self, NewStyleDialog):
        if not NewStyleDialog.objectName():
            NewStyleDialog.setObjectName(u"NewStyleDialog")
        NewStyleDialog.resize(624, 532)
        NewStyleDialog.setStyleSheet(u"QDialog {\n"
"background-color: rgba(30, 30, 40, 1);\n"
"}\n"
"\n"
"QLabel {\n"
"	color: rgba(200, 200, 200, 1);\n"
"}\n"
"\n"
"QPlainTextEdit, QListView, QListWidget {\n"
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
"QPlainTextEdit#style_name {\n"
"	padding: 0px 10px;\n"
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
"")
        self.negative_prompt = QPlainTextEdit(NewStyleDialog)
        self.negative_prompt.setObjectName(u"negative_prompt")
        self.negative_prompt.setGeometry(QRect(10, 270, 601, 211))
        font = QFont()
        font.setFamilies([u"JetBrains Mono"])
        self.negative_prompt.setFont(font)
        self.prompt = QPlainTextEdit(NewStyleDialog)
        self.prompt.setObjectName(u"prompt")
        self.prompt.setGeometry(QRect(10, 40, 601, 221))
        self.prompt.setFont(font)
        self.style_name = QPlainTextEdit(NewStyleDialog)
        self.style_name.setObjectName(u"style_name")
        self.style_name.setGeometry(QRect(10, 10, 601, 21))
        self.style_name.setFont(font)
        self.style_name.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.style_name.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.save_button = QPushButton(NewStyleDialog)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setGeometry(QRect(10, 490, 601, 31))
        self.save_button.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.save_button.setIcon(icon)
        self.save_button.setCheckable(False)

        self.retranslateUi(NewStyleDialog)

        QMetaObject.connectSlotsByName(NewStyleDialog)
    # setupUi

    def retranslateUi(self, NewStyleDialog):
        NewStyleDialog.setWindowTitle(QCoreApplication.translate("NewStyleDialog", u"New Style", None))
        self.negative_prompt.setPlaceholderText(QCoreApplication.translate("NewStyleDialog", u"Negative Prompt", None))
        self.prompt.setPlaceholderText(QCoreApplication.translate("NewStyleDialog", u"Prompt", None))
        self.style_name.setPlaceholderText(QCoreApplication.translate("NewStyleDialog", u"Style name", None))
        self.save_button.setText("")
    # retranslateUi

