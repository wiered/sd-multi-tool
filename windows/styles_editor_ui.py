# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'styles_editor.ui'
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

class Ui_StylesEditor(object):
    def setupUi(self, StylesEditor):
        if not StylesEditor.objectName():
            StylesEditor.setObjectName(u"StylesEditor")
        StylesEditor.resize(1258, 741)
        font = QFont()
        font.setFamilies([u"JetBrains Mono"])
        StylesEditor.setFont(font)
        StylesEditor.setStyleSheet(u"background-color: rgba(30, 30, 40, 1);\n"
"")
        self.widget = QWidget(StylesEditor)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 20, 1231, 711))
        self.widget.setStyleSheet(u"QLabel {\n"
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
"QPlainTextEdit#style_name, QPlainTextEdit#search_bar {\n"
"	padding: 0px 10px;\n"
"	padding-top: 3px;\n"
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
        self.search_bar = QPlainTextEdit(self.widget)
        self.search_bar.setObjectName(u"search_bar")
        self.search_bar.setGeometry(QRect(0, 0, 291, 31))
        self.search_bar.setFont(font)
        self.search_bar.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.search_bar.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.delete_button = QPushButton(self.widget)
        self.delete_button.setObjectName(u"delete_button")
        self.delete_button.setGeometry(QRect(90, 680, 31, 21))
        self.delete_button.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/delete.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.delete_button.setIcon(icon)
        self.delete_button.setCheckable(False)
        self.add_button = QPushButton(self.widget)
        self.add_button.setObjectName(u"add_button")
        self.add_button.setGeometry(QRect(10, 680, 31, 21))
        self.add_button.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/addbox.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.add_button.setIcon(icon1)
        self.add_button.setCheckable(False)
        self.save_button = QPushButton(self.widget)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setGeometry(QRect(1120, 680, 91, 31))
        self.save_button.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.save_button.setIcon(icon2)
        self.save_button.setCheckable(False)
        self.copy_button = QPushButton(self.widget)
        self.copy_button.setObjectName(u"copy_button")
        self.copy_button.setGeometry(QRect(50, 680, 31, 21))
        self.copy_button.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/copy.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.copy_button.setIcon(icon3)
        self.copy_button.setCheckable(False)
        self.prompt = QPlainTextEdit(self.widget)
        self.prompt.setObjectName(u"prompt")
        self.prompt.setGeometry(QRect(300, 40, 921, 311))
        self.prompt.setFont(font)
        self.negative_prompt = QPlainTextEdit(self.widget)
        self.negative_prompt.setObjectName(u"negative_prompt")
        self.negative_prompt.setGeometry(QRect(300, 360, 921, 311))
        self.negative_prompt.setFont(font)
        self.style_name = QPlainTextEdit(self.widget)
        self.style_name.setObjectName(u"style_name")
        self.style_name.setGeometry(QRect(300, 0, 921, 31))
        self.style_name.setFont(font)
        self.refresh_button = QPushButton(self.widget)
        self.refresh_button.setObjectName(u"refresh_button")
        self.refresh_button.setGeometry(QRect(250, 680, 31, 21))
        self.refresh_button.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/refresh.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.refresh_button.setIcon(icon4)
        self.refresh_button.setCheckable(False)
        self.styles_widget = QWidget(self.widget)
        self.styles_widget.setObjectName(u"styles_widget")
        self.styles_widget.setGeometry(QRect(0, 40, 291, 631))

        self.retranslateUi(StylesEditor)

        QMetaObject.connectSlotsByName(StylesEditor)
    # setupUi

    def retranslateUi(self, StylesEditor):
        StylesEditor.setWindowTitle(QCoreApplication.translate("StylesEditor", u"SD Multi Tool by Wiered - Styles Editor", None))
        self.search_bar.setPlaceholderText(QCoreApplication.translate("StylesEditor", u"Search", None))
        self.delete_button.setText("")
        self.add_button.setText("")
        self.save_button.setText("")
        self.copy_button.setText("")
        self.prompt.setPlaceholderText(QCoreApplication.translate("StylesEditor", u"Prompt", None))
        self.negative_prompt.setPlaceholderText(QCoreApplication.translate("StylesEditor", u"Negative Prompt", None))
        self.style_name.setPlaceholderText(QCoreApplication.translate("StylesEditor", u"Style name", None))
        self.refresh_button.setText("")
    # retranslateUi

