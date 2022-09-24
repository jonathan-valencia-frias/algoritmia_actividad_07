from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide2.QtWidgets import (QApplication, QFormLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(220, 415)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 10, 172, 350))
        self.formLayout = QFormLayout(self.layoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.text_destinox = QLabel(self.layoutWidget)
        self.text_destinox.setObjectName(u"text_destinox")

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.text_destinox)

        self.input_destinox = QLineEdit(self.layoutWidget)
        self.input_destinox.setObjectName(u"input_destinox")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.input_destinox)

        self.text_destinoy = QLabel(self.layoutWidget)
        self.text_destinoy.setObjectName(u"text_destinoy")

        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.text_destinoy)

        self.input_destinoy = QLineEdit(self.layoutWidget)
        self.input_destinoy.setObjectName(u"input_destinoy")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.input_destinoy)

        self.text_velocidad = QLabel(self.layoutWidget)
        self.text_velocidad.setObjectName(u"text_velocidad")

        self.formLayout.setWidget(6, QFormLayout.SpanningRole, self.text_velocidad)

        self.input_velocidad = QLineEdit(self.layoutWidget)
        self.input_velocidad.setObjectName(u"input_velocidad")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.input_velocidad)

        self.text_red = QLabel(self.layoutWidget)
        self.text_red.setObjectName(u"text_red")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.text_red)

        self.input_red = QLineEdit(self.layoutWidget)
        self.input_red.setObjectName(u"input_red")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.input_red)

        self.text_green = QLabel(self.layoutWidget)
        self.text_green.setObjectName(u"text_green")

        self.formLayout.setWidget(12, QFormLayout.LabelRole, self.text_green)

        self.input_green = QLineEdit(self.layoutWidget)
        self.input_green.setObjectName(u"input_green")

        self.formLayout.setWidget(12, QFormLayout.FieldRole, self.input_green)

        self.text_blue = QLabel(self.layoutWidget)
        self.text_blue.setObjectName(u"text_blue")

        self.formLayout.setWidget(15, QFormLayout.LabelRole, self.text_blue)

        self.input_blue = QLineEdit(self.layoutWidget)
        self.input_blue.setObjectName(u"input_blue")

        self.formLayout.setWidget(15, QFormLayout.FieldRole, self.input_blue)

        self.btn_limpiar = QPushButton(self.layoutWidget)
        self.btn_limpiar.setObjectName(u"btn_limpiar")

        self.formLayout.setWidget(18, QFormLayout.SpanningRole, self.btn_limpiar)

        self.btn_enviar = QPushButton(self.layoutWidget)
        self.btn_enviar.setObjectName(u"btn_enviar")

        self.formLayout.setWidget(20, QFormLayout.SpanningRole, self.btn_enviar)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 220, 22))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.text_destinox.setText(QCoreApplication.translate("MainWindow", u"Destino X", None))
        self.text_destinoy.setText(QCoreApplication.translate("MainWindow", u"Destino Y", None))
        self.text_velocidad.setText(QCoreApplication.translate("MainWindow", u"Velocidad", None))
        self.text_red.setText(QCoreApplication.translate("MainWindow", u"Red", None))
        self.text_green.setText(QCoreApplication.translate("MainWindow", u"Green", None))
        self.text_blue.setText(QCoreApplication.translate("MainWindow", u"Blue", None))
        self.btn_limpiar.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.btn_enviar.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
    # retranslateUi