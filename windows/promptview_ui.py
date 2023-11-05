# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'promptview.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGraphicsView, QPlainTextEdit,
    QSizePolicy, QWidget)

class Ui_PromptView(object):
    def setupUi(self, PromptView):
        if not PromptView.objectName():
            PromptView.setObjectName(u"PromptView")
        PromptView.resize(1231, 530)
        PromptView.setStyleSheet(u"QDialog {\n"
"background-color: rgba(30, 30, 40, 1);\n"
"}\n"
"\n"
"QGraphicsView {\n"
"	background-color: rgba(50, 50, 70, 1);\n"
"	border: 0px;\n"
"	border-radius: 7px;\n"
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
        self.graphicsView = QGraphicsView(PromptView)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setEnabled(True)
        self.graphicsView.setGeometry(QRect(10, 10, 512, 512))
        self.prompt = QPlainTextEdit(PromptView)
        self.prompt.setObjectName(u"prompt")
        self.prompt.setGeometry(QRect(530, 10, 451, 251))
        font = QFont()
        font.setFamilies([u"JetBrains Mono"])
        self.prompt.setFont(font)
        self.prompt.setReadOnly(True)
        self.negative_prompt = QPlainTextEdit(PromptView)
        self.negative_prompt.setObjectName(u"negative_prompt")
        self.negative_prompt.setGeometry(QRect(530, 270, 451, 251))
        self.negative_prompt.setFont(font)
        self.negative_prompt.setReadOnly(True)
        self.settings = QPlainTextEdit(PromptView)
        self.settings.setObjectName(u"settings")
        self.settings.setGeometry(QRect(990, 10, 231, 511))
        self.settings.setFont(font)
        self.settings.setReadOnly(True)

        self.retranslateUi(PromptView)

        QMetaObject.connectSlotsByName(PromptView)
    # setupUi

    def retranslateUi(self, PromptView):
        PromptView.setWindowTitle(QCoreApplication.translate("PromptView", u"SD Multi Tool by Wiered - Prompt Reader lite", None))
        self.prompt.setPlaceholderText(QCoreApplication.translate("PromptView", u"Prompt", None))
        self.negative_prompt.setPlaceholderText(QCoreApplication.translate("PromptView", u"Negative Prompt", None))
        self.settings.setPlaceholderText(QCoreApplication.translate("PromptView", u"Settings", None))
    # retranslateUi

