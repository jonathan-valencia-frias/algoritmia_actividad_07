# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formularioparticulasBWMhhJ.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide2.QtWidgets import (QApplication, QFormLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPlainTextEdit, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(667, 619)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 321, 571))
        self.formLayout = QFormLayout(self.layoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.text_id = QLabel(self.layoutWidget)
        self.text_id.setObjectName(u"text_id")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.text_id)

        self.input_id = QLineEdit(self.layoutWidget)
        self.input_id.setObjectName(u"input_id")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.input_id)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label)

        self.input_origenx = QLineEdit(self.layoutWidget)
        self.input_origenx.setObjectName(u"input_origenx")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.input_origenx)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_2)

        self.input_origeny = QLineEdit(self.layoutWidget)
        self.input_origeny.setObjectName(u"input_origeny")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.input_origeny)

        self.text_destinox = QLabel(self.layoutWidget)
        self.text_destinox.setObjectName(u"text_destinox")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.text_destinox)

        self.input_destinox = QLineEdit(self.layoutWidget)
        self.input_destinox.setObjectName(u"input_destinox")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.input_destinox)

        self.text_destinoy = QLabel(self.layoutWidget)
        self.text_destinoy.setObjectName(u"text_destinoy")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.text_destinoy)

        self.input_destinoy = QLineEdit(self.layoutWidget)
        self.input_destinoy.setObjectName(u"input_destinoy")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.input_destinoy)

        self.text_velocidad = QLabel(self.layoutWidget)
        self.text_velocidad.setObjectName(u"text_velocidad")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.text_velocidad)

        self.input_velocidad = QLineEdit(self.layoutWidget)
        self.input_velocidad.setObjectName(u"input_velocidad")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.input_velocidad)

        self.text_red = QLabel(self.layoutWidget)
        self.text_red.setObjectName(u"text_red")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.text_red)

        self.input_red = QLineEdit(self.layoutWidget)
        self.input_red.setObjectName(u"input_red")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.input_red)

        self.text_green = QLabel(self.layoutWidget)
        self.text_green.setObjectName(u"text_green")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.text_green)

        self.input_green = QLineEdit(self.layoutWidget)
        self.input_green.setObjectName(u"input_green")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.input_green)

        self.text_blue = QLabel(self.layoutWidget)
        self.text_blue.setObjectName(u"text_blue")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.text_blue)

        self.input_blue = QLineEdit(self.layoutWidget)
        self.input_blue.setObjectName(u"input_blue")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.input_blue)

        self.btn_enviar_final = QPushButton(self.layoutWidget)
        self.btn_enviar_final.setObjectName(u"btn_enviar_final")

        self.formLayout.setWidget(10, QFormLayout.SpanningRole, self.btn_enviar_final)

        self.btn_inicio = QPushButton(self.layoutWidget)
        self.btn_inicio.setObjectName(u"btn_inicio")

        self.formLayout.setWidget(11, QFormLayout.SpanningRole, self.btn_inicio)

        self.Canvas_mostar = QPlainTextEdit(self.centralwidget)
        self.Canvas_mostar.setObjectName(u"Canvas_mostar")
        self.Canvas_mostar.setGeometry(QRect(330, 0, 331, 511))
        self.mostrar_datos = QPushButton(self.centralwidget)
        self.mostrar_datos.setObjectName(u"mostrar_datos")
        self.mostrar_datos.setGeometry(QRect(340, 520, 161, 41))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 667, 22))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.text_id.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Origen X", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Origen Y", None))
        self.text_destinox.setText(QCoreApplication.translate("MainWindow", u"Destino X", None))
        self.text_destinoy.setText(QCoreApplication.translate("MainWindow", u"Destino Y", None))
        self.text_velocidad.setText(QCoreApplication.translate("MainWindow", u"Velocidad", None))
        self.text_red.setText(QCoreApplication.translate("MainWindow", u"Red", None))
        self.text_green.setText(QCoreApplication.translate("MainWindow", u"Green", None))
        self.text_blue.setText(QCoreApplication.translate("MainWindow", u"Blue", None))
        self.btn_enviar_final.setText(QCoreApplication.translate("MainWindow", u"Agregar Final", None))
        self.btn_inicio.setText(QCoreApplication.translate("MainWindow", u"Agregar principio", None))
        self.mostrar_datos.setText(QCoreApplication.translate("MainWindow", u"Mostrar datos", None))
    # retranslateUi