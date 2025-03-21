from PyQt5 import QtWidgets, QtSql, QtCore
from ui.ui_main_window import Ui_MainWindow
from settings import settings
from enum import Enum
from database_api.schema import init_db

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
        
        self.connect_to_database_clicked()

    def connect_to_database_clicked(self):
        if self.database.open():
            if not init_db():
                self.set_state(ConnectionState.DISCONNECTED)
                return
            self.fill_tables()
            self.set_state(ConnectionState.CONNECTED)
        else:
            QtWidgets.QMessageBox.critical(self, "Ошибка подключения", "Не удалось подключиться к базе данных. Возможно ее забыли подключить?")
            self.set_state(ConnectionState.DISCONNECTED)

    def fill_tables(self):
        self.patients_table = QtSql.QSqlTableModel(self, self.database)
        self.patients_table.setTable("patients")
        self.patients_table.setEditStrategy(QtSql.QSqlTableModel.EditStrategy.OnFieldChange)
        self.patients_table.select()
        self.patients_table.setHeaderData(0, QtCore.Qt.Orientation.Horizontal, "ID")
        self.patients_table.setHeaderData(1, QtCore.Qt.Orientation.Horizontal, "Имя")
        self.patients_table.setHeaderData(2, QtCore.Qt.Orientation.Horizontal, "Фамилия")
        self.patients_table.setHeaderData(3, QtCore.Qt.Orientation.Horizontal, "Дата рождения")
        self.patients_table.setHeaderData(4, QtCore.Qt.Orientation.Horizontal, "Пол")
        self.patients_table.setHeaderData(5, QtCore.Qt.Orientation.Horizontal, "Контактный номер")
        self.patients_table.setHeaderData(6, QtCore.Qt.Orientation.Horizontal, "Email")
        self.patients_table.setHeaderData(7, QtCore.Qt.Orientation.Horizontal, "Адрес")
        self.ui.patientsTable.setModel(self.patients_table)
        self.ui.patientsTable.resizeColumnsToContents()

        self.doctors_table = QtSql.QSqlTableModel(self, self.database)
        self.doctors_table.setTable("doctors")
        self.doctors_table.setEditStrategy(QtSql.QSqlTableModel.EditStrategy.OnFieldChange)
        self.doctors_table.select()
        self.doctors_table.setHeaderData(0, QtCore.Qt.Orientation.Horizontal, "ID")
        self.doctors_table.setHeaderData(1, QtCore.Qt.Orientation.Horizontal, "Имя")
        self.doctors_table.setHeaderData(2, QtCore.Qt.Orientation.Horizontal, "Фамилия")
        self.doctors_table.setHeaderData(3, QtCore.Qt.Orientation.Horizontal, "Специальность")
        self.doctors_table.setHeaderData(4, QtCore.Qt.Orientation.Horizontal, "Контактный номер")
        self.doctors_table.setHeaderData(5, QtCore.Qt.Orientation.Horizontal, "Email")
        self.doctors_table.setHeaderData(6, QtCore.Qt.Orientation.Horizontal, "Кабинет")
        self.ui.doctorsTable.setModel(self.doctors_table)
        self.ui.doctorsTable.resizeColumnsToContents()

        self.appointments_table = QtSql.QSqlTableModel(self, self.database)
        self.appointments_table.setTable("appointments")
        self.appointments_table.setEditStrategy(QtSql.QSqlTableModel.EditStrategy.OnFieldChange)
        self.appointments_table.select()
        self.appointments_table.setHeaderData(0, QtCore.Qt.Orientation.Horizontal, "ID")
        self.appointments_table.setHeaderData(1, QtCore.Qt.Orientation.Horizontal, "ID пациента")
        self.appointments_table.setHeaderData(2, QtCore.Qt.Orientation.Horizontal, "ID доктора")
        self.appointments_table.setHeaderData(3, QtCore.Qt.Orientation.Horizontal, "Дата и время")
        self.appointments_table.setHeaderData(4, QtCore.Qt.Orientation.Horizontal, "Примечание")
        self.appointments_table.setHeaderData(5, QtCore.Qt.Orientation.Horizontal, "Статус")
        self.appointments_table.setHeaderData(6, QtCore.Qt.Orientation.Horizontal, "Заметки")
        self.ui.tableView.setModel(self.appointments_table)
        self.ui.tableView.resizeColumnsToContents()
        
    def clear_status_bar(self):
        if hasattr(self, "status_widget"):
            self.ui.statusbar.removeWidget(self.status_widget)
        
    def create_connect_button(self) -> QtWidgets.QPushButton:
        button = QtWidgets.QPushButton("Подключиться")
        button.clicked.connect(self.connect_to_database_clicked)
        return button
    
    def set_state(self, state: ConnectionState):
        print(f"Setting state to {state}")
        self.clear_status_bar()
        central_status_widget = QtWidgets.QWidget()
        self.status_widget = central_status_widget
        central_status_layout = QtWidgets.QHBoxLayout(central_status_widget)
        central_status_layout.addWidget(QtWidgets.QLabel("Состояние: "))
        state_label = QtWidgets.QLabel()
        central_status_layout.addWidget(state_label)
        if state == ConnectionState.CONNECTED:
            state_label.setText("Подключено")
            state_label.setStyleSheet("color: green")
        else:
            state_label.setText("Не подключено")
            state_label.setStyleSheet("color: red")
            central_status_layout.addWidget(self.create_connect_button())
        self.ui.statusbar.addWidget(central_status_widget)
