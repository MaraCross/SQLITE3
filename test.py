from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import sqlite3
import sys

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setFixedSize(1000, 900)
        MainWindow.setObjectName("MainWindow")        
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

       
        
        self.text=QtWidgets.QTextEdit(self.centralwidget)
        self.text.setGeometry(QtCore.QRect(60, 50, 400, 50))
        self.text.setObjectName("text")

        self.push_btn = QtWidgets.QPushButton(self.centralwidget)
        self.push_btn.setGeometry(QtCore.QRect(500, 50, 161, 51))
        self.push_btn.setObjectName("push_btn")

        self.text_1 = QtWidgets.QTextEdit(self.centralwidget)
        self.text_1.setGeometry(QtCore.QRect(60, 120, 400, 250))
        self.text_1.setObjectName("text_1")

        self.push_btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.push_btn_1.setGeometry(QtCore.QRect(500, 320, 161, 51))
        self.push_btn_1.setObjectName("push_btn_1")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.con=False

    

        self.add_functions()
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "sqlite3 query"))
        self.push_btn.setText(_translate("MainWindow", "CONNECT"))
        self.push_btn_1.setText(_translate("MainWindow", "INPUT"))
        self.text.setText(_translate("MainWindow",":memory:"))
        


    def add_functions(self):
        self.push_btn.clicked.connect(lambda:self.db_connect(self.text.toPlainText()))
        self.push_btn_1.clicked.connect(lambda:self.db_input(self.text_1.toPlainText()))
    
    def db_connect(self,txt1):

        
        self.db=sqlite3.connect(txt1)
        connected_label = QtWidgets.QLabel(self.centralwidget)
        connected_label.setGeometry(QtCore.QRect(700, 55, 150, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setWeight(40)
       
        connected_label.setFont(font)
        connected_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        connected_label.setStyleSheet("background-color: rgb(88,88,88);")
     
        connected_label.setAlignment(QtCore.Qt.AlignCenter)
    
        connected_label.setObjectName("connected_label")
        connected_label.setText(QtCore.QCoreApplication.translate("MainWindow", "connected "+txt1))

        connected_label.show()
        

    def db_input(self,txt):
        with self.db as db:
       
            c=db.cursor()

            c.execute(txt)
                
    
            if 'select' in txt:
                a=c.fetchall()

                table = QtWidgets.QTableView(self.centralwidget)
                table.setGeometry(QtCore.QRect(60, 400, 800, 400))
                table.setObjectName("table")

                names=[description[0] for description in c.description] 

                model = QtGui.QStandardItemModel(len(a), len(names))
                for row in range(len(a)):
                    for column in range(len(names)):
                        item = QtGui.QStandardItem(str(a[row][column]))
                        model.setItem(row, column, item)
                
                model.setHorizontalHeaderLabels(names)

                table.setModel(model)
                
                table.show()

            db.commit()

         
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())


