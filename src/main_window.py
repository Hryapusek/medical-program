from PyQt5 import QtWidgets, QtSql
from ui.ui_main_window import Ui_MainWindow
from settings import settings
from enum import Enum

class ConnectionState(Enum):
    CONNECTED = 0
    DISCONNECTED = 1

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.database = QtSql.QSqlDatabase.addDatabase("QPSQL")
        self.database.setHostName(settings.database_host)
        self.database.setPort(settings.database_port)
        self.database.setDatabaseName(settings.database_name)
        self.database.setUserName(settings.database_username)
        self.database.setPassword(settings.database_password)        
        
        if self.database.open():
            self.set_state(ConnectionState.CONNECTED)
        else:
            QtWidgets.QMessageBox.critical(self, "Error", self.database.lastError().text())
            self.set_state(ConnectionState.DISCONNECTED)

          
    def set_state(self, state: ConnectionState):
        print(f"Setting state to {state}")
        central_status_widget = QtWidgets.QWidget()
        central_status_layout = QtWidgets.QHBoxLayout(central_status_widget)
        central_status_layout.addWidget(QtWidgets.QLabel("Состояние: "))
        state_label = QtWidgets.QLabel()
        if state == ConnectionState.CONNECTED:
            state_label.setText("Подключено")
            state_label.setStyleSheet("color: green")
        else:
            state_label.setText("Не подключено")
            state_label.setStyleSheet("color: red")
        central_status_layout.addWidget(state_label)
        self.ui.statusbar.addWidget(central_status_widget)
            
