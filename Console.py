# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'console.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from threading import Thread
import HunterPresence
from Overlay import Ui_OverlayWindow
import os
import subprocess
import sys
import mainResources_rc
from Config import *

Version = "2.0.90"



class Ui_Console(object):
    def __init__(self):
        self.MHWPresence = HunterPresence.MHWPresence()
        self.LastMessage = None
        self.ConsolePrint = ["\n\n====== CONSOLE =====\n"]
        self.GetTheConsoleText()
        self.JustUpdated = False
        self.closedWindow = False
        self.ConfigModule = Config()
        self.Config = self.ConfigModule.Config

    def setupUi(self, Console):
        Console.setObjectName("Console")
        Console.setWindowModality(QtCore.Qt.NonModal)
        Console.resize(700, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Console.sizePolicy().hasHeightForWidth())
        Console.setSizePolicy(sizePolicy)
        Console.setMinimumSize(QtCore.QSize(700, 400))
        Console.setMaximumSize(QtCore.QSize(700, 400))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        Console.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        Console.setFont(font)
        Console.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Console.setWindowIcon(icon)
        Console.setWindowOpacity(1.0)
        Console.setStyleSheet("")
        Console.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        Console.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(Console)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        self.centralwidget.setFont(font)
        self.centralwidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.ConsoleBox = QtWidgets.QScrollArea(self.centralwidget)
        self.ConsoleBox.setEnabled(True)
        self.ConsoleBox.setGeometry(QtCore.QRect(10, 60, 681, 331))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(226, 226, 226))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(49, 49, 49))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(73, 73, 73))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 61, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 24, 24))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 32, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 58, 58))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(49, 49, 49))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 24, 24))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(226, 226, 226))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(49, 49, 49))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(73, 73, 73))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 61, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 24, 24))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 32, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 58, 58))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(49, 49, 49))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 24, 24))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 24, 24))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(49, 49, 49))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(73, 73, 73))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 61, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 24, 24))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 32, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 24, 24))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 24, 24))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(49, 49, 49))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(49, 49, 49))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(49, 49, 49))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.ConsoleBox.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        self.ConsoleBox.setFont(font)
        self.ConsoleBox.setAutoFillBackground(True)
        self.ConsoleBox.setStyleSheet("QScrollBar:vertical {\n"
        "    border-width: 1px;\n"
        "    background-color: rgb(65, 65, 65);\n"
        "    width: 10px;\n"
        "    padding-right: 2px;\n"
        "    border-radius: 3px;\n"
        "    padding-top: 2px;\n"
        "    padding-bottom: 2px;\n"
        "}\n"
        "QScrollBar::handle:vertical {\n"
        "    background-color: rgb(45, 45, 45);\n"
        "    min-width: 5px;\n"
        "    border-radius: 3px;\n"
        "}\n"
        "QScrollBar::add-page:vertical {\n"
        "    background-color: none;\n"
        "}\n"
        "QScrollBar::sub-page:vertical {\n"
        "    background-color: none;\n"
        "}\n"
        "QScrollBar::add-line:vertical {\n"
        "    border: none;\n"
        "    background-color: none;\n"
        "}\n"
        "QScrollBar::sub-line:vertical {\n"
        "    border: none;\n"
        "    background-color: none;\n"
        "}\n"
        "QScrollBar::handle:vertical:hover {\n"
        "    background-color: rgb(55, 55, 55)\n"
        "}")
        self.ConsoleBox.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ConsoleBox.setFrameShadow(QtWidgets.QFrame.Plain)
        self.ConsoleBox.setLineWidth(-1)
        self.ConsoleBox.setMidLineWidth(-1)
        self.ConsoleBox.setWidgetResizable(True)
        self.ConsoleBox.setObjectName("ConsoleBox")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 681, 331))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.scrollAreaWidgetContents.setFont(font)
        self.scrollAreaWidgetContents.setAutoFillBackground(True)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.TextBox = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.TextBox.setGeometry(QtCore.QRect(0, 0, 681, 331))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.TextBox.setFont(font)
        self.TextBox.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.TextBox.setAutoFillBackground(False)
        self.TextBox.setStyleSheet("QTextBrowser {\n"
        "    background-color: rgb(65, 65, 65);\n"
        "    color: white;\n"
        "}")
        self.TextBox.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.TextBox.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.TextBox.setReadOnly(True)
        self.TextBox.setPlaceholderText("")
        self.TextBox.setObjectName("TextBox")
        self.ConsoleBox.setWidget(self.scrollAreaWidgetContents)
        self.enableOverlay = QtWidgets.QCheckBox(self.centralwidget)
        self.enableOverlay.setGeometry(QtCore.QRect(460, 0, 231, 31))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(12)
        self.enableOverlay.setFont(font)
        self.enableOverlay.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.enableOverlay.setObjectName("enableOverlay")
        self.enableRichPresence = QtWidgets.QCheckBox(self.centralwidget)
        self.enableRichPresence.setGeometry(QtCore.QRect(460, 30, 231, 31))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(12)
        self.enableRichPresence.setFont(font)
        self.enableRichPresence.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.enableRichPresence.setStyleSheet("")
        self.enableRichPresence.setObjectName("enableRichPresence")
        self.hunterPyLogo = QtWidgets.QLabel(self.centralwidget)
        self.hunterPyLogo.setGeometry(QtCore.QRect(10, 5, 211, 51))
        self.hunterPyLogo.setObjectName("hunterPyLogo")
        self.changelogWindow = QtWidgets.QWidget(self.centralwidget)
        self.changelogWindow.setGeometry(QtCore.QRect(0, 0, 701, 401))
        self.changelogWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.changelogWindow.setStyleSheet("QWidget {\n"
        "    background-color: rgba(0, 0, 0, 0.2);\n"
        "    border-radius: 3px;\n"
        "}\n"
        "QTextBrowser {\n"
        "    background-color: white;\n"
        "}\n"
        "QPushButton {\n"
        "    background-color: rgb(191, 0, 0);\n"
        "    color: white;\n"
        "    border-radius: 3px\n"
        "}\n"
        "QPushButton:hover {\n"
        "    background-color: rgb(154, 0, 0);\n"
        "}\n"
        "QScrollBar:vertical {\n"
        "    border-width: 1px;\n"
        "    background-color: white;\n"
        "    width: 10px;\n"
        "    padding-right: 2px;\n"
        "    border-radius: 3px;\n"
        "    padding-top: 2px;\n"
        "    padding-bottom: 2px;\n"
        "}\n"
        "QScrollBar::handle:vertical {\n"
        "    background-color: rgb(160, 160, 160);\n"
        "    min-width: 5px;\n"
        "    border-radius: 3px;\n"
        "}\n"
        "QScrollBar::add-page:vertical {\n"
        "    background-color: none;\n"
        "}\n"
        "QScrollBar::sub-page:vertical {\n"
        "    background-color: none;\n"
        "}\n"
        "QScrollBar::add-line:vertical {\n"
        "    border: none;\n"
        "    background-color: none;\n"
        "}\n"
        "QScrollBar::sub-line:vertical {\n"
        "    border: none;\n"
        "    background-color: none;\n"
        "}\n"
        "QScrollBar::handle:vertical:hover {\n"
        "    background-color: rgb(200, 200, 200);\n"
        "}")
        self.changelogWindow.setObjectName("changelogWindow")
        self.changelogText = QtWidgets.QTextBrowser(self.changelogWindow)
        self.changelogText.setGeometry(QtCore.QRect(70, 35, 571, 311))
        self.changelogText.setObjectName("changelogText")
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.changelogText.setFont(font)
        self.changeLogButton = QtWidgets.QPushButton(self.changelogWindow)
        self.changeLogButton.setGeometry(QtCore.QRect(290, 350, 121, 31))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.changeLogButton.setFont(font)
        self.changeLogButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.changeLogButton.setObjectName("changeLogButton")
        self.changelogWindBG = QtWidgets.QWidget(self.changelogWindow)
        self.changelogWindBG.setGeometry(QtCore.QRect(60, 29, 591, 361))
        self.changelogWindBG.setObjectName("changelogWindBG")
        self.changelogWindBG.raise_()
        self.changelogText.raise_()
        self.changeLogButton.raise_()
        Console.setCentralWidget(self.centralwidget)

        self.retranslateUi(Console)
        QtCore.QMetaObject.connectSlotsByName(Console)

        self.OpenOverlayWindow()
        self.loadConfigEvent()

        self.enableOverlay.setCheckable(True)
        self.enableOverlay.stateChanged.connect(self.enableOverlayHandler)

        self.enableRichPresence.setCheckable(True)
        self.enableRichPresence.stateChanged.connect(self.enablePresenceHandler)
        
        
        QtCore.QTimer.singleShot(1, self.UpdateOverlay)
        # Close hook
        Console.closeEvent = self.closeEverything
        # Minimize to taskbar
        Console.hideEvent = self.minToTray
        self.Console = Console
        self.trayIcon = QtWidgets.QSystemTrayIcon(QtGui.QIcon("icon.ico"), parent=self.Console)
        self.trayIcon.activated.connect(self.showMainWindow)
        self.trayIcon.show()
        

        ### Rich presence checkbox
        if self.MHWPresence.Enabled:
            self.enableRichPresence.setChecked(True)
        else:
            self.enableRichPresence.setChecked(False)
        ### Overlay checkbox
        if self.OverlayUI.Enabled:
            self.enableOverlay.setChecked(True)
            self.OverlayWindow.show()
        else:
            self.enableOverlay.setChecked(False)
            self.OverlayWindow.hide()

        self.changeLogButton.clicked.connect(self.hideChangelog)

    def retranslateUi(self, Console):
        _translate = QtCore.QCoreApplication.translate
        Console.setWindowTitle(_translate("Console", f"HunterPy (v{Version})"))
        self.enableOverlay.setText(_translate("Console", "Enable in-game overlay"))
        self.enableRichPresence.setText(_translate("Console", "Enable Discord presence"))
        self.hunterPyLogo.setText(_translate("Console", "<html><head/><body><p><img src=\":/Console/hunterPyConsole.png\"/></p></body></html>"))
        self.changeLogButton.setText(_translate("Console", "Ok!"))

    def loadConfigEvent(self):
        self.ConfigModule.LoadConfig()
        self.Config = self.ConfigModule.Config
        self.checkIfWidgetsEnabled()
        QtCore.QTimer.singleShot(1, self.loadConfigEvent)

    def checkIfWidgetsEnabled(self):
        # Check if they're enabled
        self.MHWPresence.Enabled = self.Config["RichPresence"]["Enabled"]
        self.OverlayUI.Enabled = self.Config["Overlay"]["Enabled"]
        self.OverlayUI.FertilizerWidgetEnabled = self.Config["Overlay"]["HarvestBoxComponent"]["Enabled"]
        self.OverlayUI.PrimaryMantleEnabled = self.Config["Overlay"]["PrimaryMantle"]["Enabled"]
        self.OverlayUI.SecondaryMantleEnabled = self.Config["Overlay"]["SecondaryMantle"]["Enabled"]
        #Get Position of overlay widgets
        self.OverlayUI.monsterWidgetPosition = self.Config["Overlay"]["MonstersComponent"]["Position"]
        self.OverlayUI.fertWidgetPosition = self.Config["Overlay"]["HarvestBoxComponent"]["Position"]
        self.OverlayUI.PrimaryMantlePosition = self.Config["Overlay"]["PrimaryMantle"]["Position"]
        self.OverlayUI.SecondaryMantlePosition = self.Config["Overlay"]["SecondaryMantle"]["Position"]

    def showMainWindow(self, event):
        if event == QtWidgets.QSystemTrayIcon.Trigger:
            pass
        elif event == QtWidgets.QSystemTrayIcon.DoubleClick:
            self.Console.showNormal()
            self.Console.activateWindow()
        
    def minToTray(self, event):
        if event.type() == 18 and self.closedWindow == False:
            self.Console.hide()
            self.trayIcon.show()

    def checkIfJustUpdated(self):
        ### If program just updated
        if self.JustUpdated:
            self.GetChangelog()
        else:
            self.hideChangelog()

    def OpenChangelogAndReturnBytes(self):
        try:
            changelog = open("changelog.log", "r")
            changelogBytes = changelog.read()
            changelog.close()
        except:
            changelogBytes = "ERROR!\nNO CHANGELOG FOUND!"
        return changelogBytes


    def GetChangelog(self):
        changelog = self.OpenChangelogAndReturnBytes()
        self.ConsoleBox.setGraphicsEffect(QtWidgets.QGraphicsBlurEffect())
        self.enableOverlay.setGraphicsEffect(QtWidgets.QGraphicsBlurEffect())
        self.enableRichPresence.setGraphicsEffect(QtWidgets.QGraphicsBlurEffect())
        self.hunterPyLogo.setGraphicsEffect(QtWidgets.QGraphicsBlurEffect())
        self.changelogText.setText(changelog)

    def UpdateOverlay(self):
        if self.OverlayUI.Enabled and self.MHWPresence.Scanning:
            self.OverlayUI.showMonstersWidget()
            self.firstMonsterInfo()
            self.secondMonsterInfo()
            self.thirdMonsterInfo()
            self.updateFertilizerOverlay()
            self.updatePrimaryMantle()
            self.updateSecondaryMantle()
        QtCore.QTimer.singleShot(1, self.UpdateOverlay)

    def updatePrimaryMantle(self):
        if self.OverlayUI.PrimaryMantleEnabled:
            try:
                mantleName = self.MHWPresence.MantleIds[self.MHWPresence.PlayerInfo.PrimaryMantle]
            except:
                mantleName = None
            if 0 < self.MHWPresence.PlayerInfo.PrimaryMantleInfo[1] < self.MHWPresence.PlayerInfo.PrimaryMantleInfo[0]:
                if self.OverlayUI.mantleName.text() != f"{mantleName} ({int(self.MHWPresence.PlayerInfo.PrimaryMantleInfo[1])})": # Only update widget if the text is different. This reduces CPU usage by A LOT
                    fixedCd = self.MHWPresence.PlayerInfo.PrimaryMantleInfo[0]
                    cd = self.MHWPresence.PlayerInfo.PrimaryMantleInfo[1]
                    self.OverlayUI.setColorDependingOnMantle(self.MHWPresence.PlayerInfo.PrimaryMantle, "primary")
                    self.OverlayUI.updatePrimaryMantleBar(fixedCd-cd, fixedCd)
                    self.OverlayUI.updatePrimaryMantleName(mantleName, cd)
                    self.OverlayUI.showPrimaryMantle()
            elif 0 < self.MHWPresence.PlayerInfo.PrimaryMantleInfo[3] < self.MHWPresence.PlayerInfo.PrimaryMantleInfo[2]:
                if self.OverlayUI.mantleName.text() != f"{mantleName} ({int(self.MHWPresence.PlayerInfo.PrimaryMantleInfo[3])})":
                    fixedTimer = self.MHWPresence.PlayerInfo.PrimaryMantleInfo[2]
                    timer = self.MHWPresence.PlayerInfo.PrimaryMantleInfo[3]
                    self.OverlayUI.setColorDependingOnMantle(self.MHWPresence.PlayerInfo.PrimaryMantle, "primary")
                    self.OverlayUI.updatePrimaryMantleBar(timer, fixedTimer)
                    self.OverlayUI.updatePrimaryMantleName(mantleName, timer)
                    self.OverlayUI.showPrimaryMantle()
            else:
                self.OverlayUI.hidePrimaryMantle()
        else:
            self.OverlayUI.hidePrimaryMantle()

    def updateSecondaryMantle(self):
        if self.OverlayUI.SecondaryMantleEnabled:
            try:
                mantleName = self.MHWPresence.MantleIds[self.MHWPresence.PlayerInfo.SecondaryMantle]
            except:
                mantleName = None
            if 0 < self.MHWPresence.PlayerInfo.SecondaryMantleInfo[1] < self.MHWPresence.PlayerInfo.SecondaryMantleInfo[0]:
                if self.OverlayUI.secondaryMantleName.text() != f"{mantleName} ({int(self.MHWPresence.PlayerInfo.SecondaryMantleInfo[1])})":
                    fixedCd = self.MHWPresence.PlayerInfo.SecondaryMantleInfo[0]
                    cd = self.MHWPresence.PlayerInfo.SecondaryMantleInfo[1]
                    self.OverlayUI.setColorDependingOnMantle(self.MHWPresence.PlayerInfo.SecondaryMantle, "secondary")
                    self.OverlayUI.updateSecondaryMantleBar(fixedCd-cd, fixedCd)
                    self.OverlayUI.updateSecondaryMantleName(mantleName, cd)
                    self.OverlayUI.showSecondaryMantle()
            elif 0 < self.MHWPresence.PlayerInfo.SecondaryMantleInfo[3] < self.MHWPresence.PlayerInfo.SecondaryMantleInfo[2]:
                if self.OverlayUI.secondaryMantleName.text() != f"{mantleName} ({int(self.MHWPresence.PlayerInfo.SecondaryMantleInfo[3])})":
                    fixedTimer = self.MHWPresence.PlayerInfo.SecondaryMantleInfo[2]
                    timer = self.MHWPresence.PlayerInfo.SecondaryMantleInfo[3]
                    self.OverlayUI.setColorDependingOnMantle(self.MHWPresence.PlayerInfo.SecondaryMantle, "secondary")
                    self.OverlayUI.updateSecondaryMantleBar(timer, fixedTimer)
                    self.OverlayUI.updateSecondaryMantleName(mantleName, timer)
                    self.OverlayUI.showSecondaryMantle()
            else:
                self.OverlayUI.hideSecondaryMantle()
        else:
            self.OverlayUI.hideSecondaryMantle()

    def updateFertilizerOverlay(self):
        if self.OverlayUI.FertilizerWidgetEnabled and self.MHWPresence.PlayerInfo.ZoneID in self.MHWPresence.NoMonsterZones and len(self.MHWPresence.PlayerInfo.HarvestBoxFertilizers) == 4 and self.MHWPresence.Scanning:
            if self.MHWPresence.PlayerInfo.ZoneName in ["Main Menu", "Training area"]: # hides harvest window in main menu, needs this because Main Menu is a "NoMonsterZone"
                self.OverlayUI.hideFertilizerWindow()
            else:
                self.OverlayUI.showFertilizerWindow()
                self.OverlayUI.updateFertilizerCounter(self.MHWPresence.PlayerInfo.HarvestBoxFertilizers)
                self.OverlayUI.updateHarvestedTotal(self.MHWPresence.PlayerInfo.HarvestedItemsCounter)
        else:
            self.OverlayUI.hideFertilizerWindow()

    def firstMonsterInfo(self):
        if self.MHWPresence.Player.PrimaryMonster.Id in self.MHWPresence.MonstersIds and self.MHWPresence.Player.PrimaryMonster.CurrentHP > 0:
            MonsterData = {
                "name" : self.MHWPresence.Player.PrimaryMonster.Name,
                "hp" : [int(self.MHWPresence.Player.PrimaryMonster.CurrentHP), int(self.MHWPresence.Player.PrimaryMonster.TotalHP)]
            }
            self.OverlayUI.UpdateFirstMonster('UPDATE', MonsterData)
        else:
            self.OverlayUI.UpdateFirstMonster('HIDE')
    
    def secondMonsterInfo(self):
        if self.MHWPresence.Player.SecondaryMonster.Id in self.MHWPresence.MonstersIds and self.MHWPresence.Player.SecondaryMonster.CurrentHP > 0:
            MonsterData = {
                "name" : self.MHWPresence.Player.SecondaryMonster.Name,
                "hp" : [int(self.MHWPresence.Player.SecondaryMonster.CurrentHP), int(self.MHWPresence.Player.SecondaryMonster.TotalHP)]
            }
            self.OverlayUI.UpdateSecondMonster('UPDATE', MonsterData)
        else:
            self.OverlayUI.UpdateSecondMonster('HIDE')

    def thirdMonsterInfo(self):
        if self.MHWPresence.Player.ThirtiaryMonster.Id in self.MHWPresence.MonstersIds and self.MHWPresence.Player.ThirtiaryMonster.CurrentHP > 0:
            MonsterData = {
                "name" : self.MHWPresence.Player.ThirtiaryMonster.Name,
                "hp" : [self.MHWPresence.Player.ThirtiaryMonster.CurrentHP, self.MHWPresence.Player.ThirtiaryMonster.TotalHP]
            }
            self.OverlayUI.UpdateThirdMonster('UPDATE', MonsterData)
        else:
            self.OverlayUI.UpdateThirdMonster('HIDE')


    def GetTextFromPresence(self):
        message = '\n'.join(self.MHWPresence.ConsoleMessage)
        message = message + "".join(self.ConsolePrint)
        if message != self.LastMessage:
            self.UpdateConsoleText(message)
            self.LastMessage = message
        QtCore.QTimer.singleShot(1, self.GetTextFromPresence)

    def GetTheConsoleText(self):
        QtCore.QTimer.singleShot(1, self.GetTextFromPresence)

    def UpdateConsoleText(self, string):
        self.TextBox.setText(string)

    def Log(self, text):
        if len(self.ConsolePrint) > 100:
            self.ConsolePrint = []
        self.ConsolePrint.append(text+"\n")

    def enableOverlayHandler(self):
        if self.enableOverlay.isChecked():
            self.OverlayWindow.show()
            self.setOverlayEnabled(True)
            self.Log("Overlay is now enabled!")
        else:
            self.OverlayWindow.hide()
            self.OverlayUI.hideMonstersWidget()
            self.setOverlayEnabled(False)
            self.Log("Overlay is now disabled!")

    def OpenOverlayWindow(self):
        self.OverlayWindow = QtWidgets.QMainWindow()
        self.OverlayUI = Ui_OverlayWindow()
        self.OverlayUI.setupUi(self.OverlayWindow)

    def closeEverything(self, event):
        self.closedWindow = True
        self.OverlayWindow.close()
        self.trayIcon.hide()
        event.accept()
        
        
    def enablePresenceHandler(self):
        if self.enableRichPresence.isChecked():
            self.Log("Rich presence is now enabled!")
            self.setPresenceEnabled(True)
        else:
            self.Log("Rich presence is now disabled!")
            self.setPresenceEnabled(False)


    def setOverlayEnabled(self, bool):
        self.ConfigModule.LoadConfig()
        self.Config = self.ConfigModule.Config
        self.Config["Overlay"]["Enabled"] = bool
        self.ConfigModule.SaveConfig()
        self.OverlayUI.Enabled = bool

    def setPresenceEnabled(self, bool):
        self.ConfigModule.LoadConfig()
        self.Config = self.ConfigModule.Config
        self.Config["RichPresence"]["Enabled"] = bool
        self.MHWPresence.Enabled = bool
        self.ConfigModule.SaveConfig()

    def hideChangelog(self, event=None):
        self.ConsoleBox.setGraphicsEffect(None)
        self.enableOverlay.setGraphicsEffect(None)
        self.enableRichPresence.setGraphicsEffect(None)
        self.hunterPyLogo.setGraphicsEffect(None)
        self.changeLogButton.hide()
        self.changelogText.hide()
        self.changelogWindBG.hide()
        self.changelogWindow.hide()

def GetNewUpdater():
    import requests
    import hashlib
    try:
        url = "https://bitbucket.org/Haato/hunterpy/raw/master/update.exe"
        update = requests.request('get', url).content
    except ConnectionError:
        return
    hOnline = hashlib.sha256(update).hexdigest()
    local = open("update.exe", "rb")
    hLocal = hashlib.sha256(local.read()).hexdigest()
    local.close()
    if hOnline != hLocal:
        u = open("update.exe", "wb")
        u.write(update)
        u.close()

def MainUp():
    config = Config()
    config.LoadConfig()
    checkIfBranchExist = lambda name: name if name in ["BETA", "master"] else "master" # quick workaround to avoid update.exe crash
    if config.Config["HunterPy"]["Update"]["Enabled"]:
        subprocess.Popen(f'update.exe {Version} {checkIfBranchExist(config.Config["HunterPy"]["Update"]["Branch"])}', shell=True)
        sys.exit()
    else:
        Main("notupdated")

def Main(arg):
    app = QtWidgets.QApplication(sys.argv)
    Console = QtWidgets.QMainWindow()
    ui = Ui_Console()
    ui.setupUi(Console)
    if arg == "updated":
        ui.JustUpdated = True
        GetNewUpdater()
    else:
        ui.JustUpdated = False
    ui.checkIfJustUpdated()
    Console.showNormal()
    sys.exit(app.exec_())

if __name__ == "__main__":
    args = sys.argv
    if len(args) == 1:
        MainUp()
    else:
        Main(args[1])

