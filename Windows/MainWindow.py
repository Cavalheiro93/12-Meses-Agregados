# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QTabWidget, QTableView, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1331, 565)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.TabAgregados = QTabWidget(self.centralwidget)
        self.TabAgregados.setObjectName(u"TabAgregados")
        self.TabAgregados.setGeometry(QRect(10, 0, 1311, 551))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 761, 41))
        font = QFont()
        font.setFamilies([u"Comic Sans MS"])
        self.label.setFont(font)
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 110, 1291, 71))
        self.LineEdit_QVV = QLineEdit(self.groupBox)
        self.LineEdit_QVV.setObjectName(u"LineEdit_QVV")
        self.LineEdit_QVV.setGeometry(QRect(20, 30, 111, 25))
        self.LineEdit_M = QLineEdit(self.groupBox)
        self.LineEdit_M.setObjectName(u"LineEdit_M")
        self.LineEdit_M.setGeometry(QRect(140, 30, 65, 25))
        self.LineEdit_M.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.LineEdit_G = QLineEdit(self.groupBox)
        self.LineEdit_G.setObjectName(u"LineEdit_G")
        self.LineEdit_G.setGeometry(QRect(210, 30, 65, 25))
        self.LineEdit_G.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.LineEdit_H = QLineEdit(self.groupBox)
        self.LineEdit_H.setObjectName(u"LineEdit_H")
        self.LineEdit_H.setGeometry(QRect(280, 30, 65, 25))
        self.LineEdit_H.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.LineEdit_J = QLineEdit(self.groupBox)
        self.LineEdit_J.setObjectName(u"LineEdit_J")
        self.LineEdit_J.setGeometry(QRect(350, 30, 65, 25))
        self.LineEdit_J.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.LineEdit_V = QLineEdit(self.groupBox)
        self.LineEdit_V.setObjectName(u"LineEdit_V")
        self.LineEdit_V.setGeometry(QRect(420, 30, 65, 25))
        self.LineEdit_V.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.LineEdit_W = QLineEdit(self.groupBox)
        self.LineEdit_W.setObjectName(u"LineEdit_W")
        self.LineEdit_W.setGeometry(QRect(490, 30, 65, 25))
        self.LineEdit_W.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.LineEdit_A = QLineEdit(self.groupBox)
        self.LineEdit_A.setObjectName(u"LineEdit_A")
        self.LineEdit_A.setGeometry(QRect(560, 30, 65, 25))
        self.LineEdit_A.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.Button_Cadastrar = QPushButton(self.groupBox)
        self.Button_Cadastrar.setObjectName(u"Button_Cadastrar")
        self.Button_Cadastrar.setGeometry(QRect(940, 30, 75, 25))
        self.RadioButton_NotFound = QRadioButton(self.groupBox)
        self.RadioButton_NotFound.setObjectName(u"RadioButton_NotFound")
        self.RadioButton_NotFound.setGeometry(QRect(750, 30, 171, 20))
        self.RadioButton_Tudo = QRadioButton(self.groupBox)
        self.RadioButton_Tudo.setObjectName(u"RadioButton_Tudo")
        self.RadioButton_Tudo.setGeometry(QRect(640, 30, 101, 20))
        self.TableView_QVV = QTableView(self.tab)
        self.TableView_QVV.setObjectName(u"TableView_QVV")
        self.TableView_QVV.setGeometry(QRect(10, 190, 1291, 321))
        font1 = QFont()
        font1.setFamilies([u"Comic Sans MS"])
        font1.setPointSize(7)
        self.TableView_QVV.setFont(font1)
        self.RadioButton_BM = QRadioButton(self.tab)
        self.RadioButton_BM.setObjectName(u"RadioButton_BM")
        self.RadioButton_BM.setGeometry(QRect(760, 90, 82, 17))
        self.RadioButton_Modelo = QRadioButton(self.tab)
        self.RadioButton_Modelo.setObjectName(u"RadioButton_Modelo")
        self.RadioButton_Modelo.setGeometry(QRect(870, 90, 82, 17))
        self.TabAgregados.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.TableView_Categoria_Agr = QTableView(self.tab_2)
        self.TableView_Categoria_Agr.setObjectName(u"TableView_Categoria_Agr")
        self.TableView_Categoria_Agr.setGeometry(QRect(10, 190, 451, 321))
        self.label_2 = QLabel(self.tab_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 0, 451, 41))
        self.label_2.setFont(font)
        self.groupBox_2 = QGroupBox(self.tab_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 110, 451, 71))
        self.LineEdit_BM = QLineEdit(self.groupBox_2)
        self.LineEdit_BM.setObjectName(u"LineEdit_BM")
        self.LineEdit_BM.setGeometry(QRect(10, 30, 111, 25))
        self.LineEdit_Tipo_agr = QLineEdit(self.groupBox_2)
        self.LineEdit_Tipo_agr.setObjectName(u"LineEdit_Tipo_agr")
        self.LineEdit_Tipo_agr.setGeometry(QRect(130, 30, 151, 25))
        self.LineEdit_Linha_agr = QLineEdit(self.groupBox_2)
        self.LineEdit_Linha_agr.setObjectName(u"LineEdit_Linha_agr")
        self.LineEdit_Linha_agr.setGeometry(QRect(290, 30, 51, 25))
        self.Button_Cadastrar_Agregado = QPushButton(self.groupBox_2)
        self.Button_Cadastrar_Agregado.setObjectName(u"Button_Cadastrar_Agregado")
        self.Button_Cadastrar_Agregado.setGeometry(QRect(360, 30, 75, 25))
        self.TabAgregados.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.groupBox_3 = QGroupBox(self.tab_3)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 50, 451, 131))
        self.LineEdit_Exp_Variante = QLineEdit(self.groupBox_3)
        self.LineEdit_Exp_Variante.setObjectName(u"LineEdit_Exp_Variante")
        self.LineEdit_Exp_Variante.setGeometry(QRect(10, 30, 141, 25))
        self.LineEdit_Exp_BM = QLineEdit(self.groupBox_3)
        self.LineEdit_Exp_BM.setObjectName(u"LineEdit_Exp_BM")
        self.LineEdit_Exp_BM.setGeometry(QRect(160, 30, 71, 25))
        self.LineEdit_Exp_Agregado = QLineEdit(self.groupBox_3)
        self.LineEdit_Exp_Agregado.setObjectName(u"LineEdit_Exp_Agregado")
        self.LineEdit_Exp_Agregado.setGeometry(QRect(240, 30, 71, 25))
        self.Button_Cadastrar_Agregado_Exp = QPushButton(self.groupBox_3)
        self.Button_Cadastrar_Agregado_Exp.setObjectName(u"Button_Cadastrar_Agregado_Exp")
        self.Button_Cadastrar_Agregado_Exp.setGeometry(QRect(330, 30, 91, 81))
        self.LineEdit_Exp_Tipo = QLineEdit(self.groupBox_3)
        self.LineEdit_Exp_Tipo.setObjectName(u"LineEdit_Exp_Tipo")
        self.LineEdit_Exp_Tipo.setGeometry(QRect(10, 80, 141, 25))
        self.LineEdit_Exp_Serie = QLineEdit(self.groupBox_3)
        self.LineEdit_Exp_Serie.setObjectName(u"LineEdit_Exp_Serie")
        self.LineEdit_Exp_Serie.setGeometry(QRect(170, 80, 141, 25))
        self.TableView_Exp = QTableView(self.tab_3)
        self.TableView_Exp.setObjectName(u"TableView_Exp")
        self.TableView_Exp.setGeometry(QRect(10, 190, 651, 321))
        self.label_3 = QLabel(self.tab_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 0, 451, 41))
        self.label_3.setFont(font)
        self.TabAgregados.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.TabAgregados.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">12MPP de Agregados</span></p></body></html>", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Cadastro Manual de QVV", None))
        self.LineEdit_QVV.setPlaceholderText(QCoreApplication.translate("MainWindow", u"QVV...", None))
#if QT_CONFIG(tooltip)
        self.LineEdit_M.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.LineEdit_M.setPlaceholderText(QCoreApplication.translate("MainWindow", u"M", None))
#if QT_CONFIG(tooltip)
        self.LineEdit_G.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.LineEdit_G.setPlaceholderText(QCoreApplication.translate("MainWindow", u"G", None))
#if QT_CONFIG(tooltip)
        self.LineEdit_H.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.LineEdit_H.setPlaceholderText(QCoreApplication.translate("MainWindow", u"H", None))
#if QT_CONFIG(tooltip)
        self.LineEdit_J.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.LineEdit_J.setPlaceholderText(QCoreApplication.translate("MainWindow", u"J", None))
#if QT_CONFIG(tooltip)
        self.LineEdit_V.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.LineEdit_V.setPlaceholderText(QCoreApplication.translate("MainWindow", u"V", None))
#if QT_CONFIG(tooltip)
        self.LineEdit_W.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.LineEdit_W.setPlaceholderText(QCoreApplication.translate("MainWindow", u"W", None))
#if QT_CONFIG(tooltip)
        self.LineEdit_A.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.LineEdit_A.setPlaceholderText(QCoreApplication.translate("MainWindow", u"A", None))
        self.Button_Cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.RadioButton_NotFound.setText(QCoreApplication.translate("MainWindow", u"Sem Cadastro de Agregados", None))
        self.RadioButton_Tudo.setText(QCoreApplication.translate("MainWindow", u"Visualizar Tudo", None))
        self.RadioButton_BM.setText(QCoreApplication.translate("MainWindow", u"Por BM", None))
        self.RadioButton_Modelo.setText(QCoreApplication.translate("MainWindow", u"Por Modelo", None))
        self.TabAgregados.setTabText(self.TabAgregados.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Programa de Agregados (BM)", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Agrupamento de Agregados</span></p></body></html>", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Categoria de Agregados", None))
        self.LineEdit_BM.setPlaceholderText(QCoreApplication.translate("MainWindow", u"BM...", None))
        self.LineEdit_Tipo_agr.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Modelo...", None))
        self.LineEdit_Linha_agr.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Linha...", None))
        self.Button_Cadastrar_Agregado.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.TabAgregados.setTabText(self.TabAgregados.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Agrupamento dos Agregados", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Categoria de Agregados", None))
        self.LineEdit_Exp_Variante.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Variante...", None))
        self.LineEdit_Exp_BM.setPlaceholderText(QCoreApplication.translate("MainWindow", u"BM...", None))
        self.LineEdit_Exp_Agregado.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Agregado...", None))
        self.Button_Cadastrar_Agregado_Exp.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.LineEdit_Exp_Tipo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Tipo...", None))
        self.LineEdit_Exp_Serie.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Serie...", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Agregados Exporta\u00e7\u00e3o</span></p></body></html>", None))
        self.TabAgregados.setTabText(self.TabAgregados.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Agregados Exporta\u00e7\u00e3o", None))
    # retranslateUi

