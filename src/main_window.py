from PyQt5 import QtWidgets, QtSql
from ui.ui_main_window import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.database = QtSql.QSqlDatabase.addDatabase("QPSQL")
        

