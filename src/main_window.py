from enum import Enum
from datetime import datetime
from typing import Any, Callable, Optional

from result import Ok, Err, Result, is_ok, is_err

from PyQt5 import QtWidgets, QtSql, QtCore
from sqlalchemy.sql import insert, delete
from sqlalchemy.orm import sessionmaker

from ui.ui_main_window import Ui_MainWindow
from ui.ui_create_patient import Ui_CreatePatientForm
from ui.ui_id_form import Ui_EnterIdForm
from ui.ui_create_doctor import Ui_CreateDoctorForm
from ui.ui_create_appointment import Ui_CreateAppointmentForm

from delegates.doctors_item_delegate import DoctorsItemDelegate
from delegates.patients_item_delegate import PatientsItemDelegate

from settings import settings
from database_api.schema import Doctor, Patient, Appointment, init_db, main_engine

from utils import Finally


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

        self.sessionmaker = sessionmaker(main_engine)
        self.setup_patients_tab()
        self.setup_doctors_tab()
        self.setup_appointments_tab()
        self.connect_to_database_clicked()

    def setup_patients_tab(self):
        self.ui.addPatientBtn.clicked.connect(
            self.create_crud_button_handler(
                self.create_create_patient_dialog,
                self.collect_create_patient_from_form,
                self.try_create_patient,
            )
        )
        self.ui.deletePatientBtn.clicked.connect(
            self.create_crud_button_handler(
                self.create_delete_patient_dialog,
                self.collect_id_from_form,
                self.try_delete_patient,
            )
        )

    def setup_doctors_tab(self):
        self.ui.addDoctorBtn.clicked.connect(
            self.create_crud_button_handler(
                self.create_create_doctor_dialog,
                self.collect_create_doctor_from_form,
                self.try_create_doctor,
            )
        )
        self.ui.deleteDoctorBtn.clicked.connect(
            self.create_crud_button_handler(
                self.create_delete_doctor_dialog,
                self.collect_id_from_form,
                self.try_delete_doctor,
            )
        )

    def setup_appointments_tab(self):
        self.ui.addAppointment.clicked.connect(
            self.create_crud_button_handler(
                self.create_create_appointment_dialog,
                self.collect_create_appointment_from_form,
                self.try_create_appointment,
            )
        )
        self.ui.deleteAppointment.clicked.connect(
            self.create_crud_button_handler(
                self.create_delete_appointment_dialog,
                self.collect_id_from_form,
                self.try_delete_appointment,
            )
        )
        
    def connect_to_database_clicked(self):
        if self.database.open():
            if not init_db():
                self.set_state(ConnectionState.DISCONNECTED)
                return
            self.fill_tables()
            self.set_state(ConnectionState.CONNECTED)
        else:
            QtWidgets.QMessageBox.critical(
                self,
                "Ошибка подключения",
                "Не удалось подключиться к базе данных. Возможно ее забыли подключить?",
            )
            self.set_state(ConnectionState.DISCONNECTED)

    def fill_tables(self):
        self.patients_table = QtSql.QSqlTableModel(self, self.database)
        self.patients_table.setTable("patients")
        self.patients_table.setEditStrategy(
            QtSql.QSqlTableModel.EditStrategy.OnFieldChange
        )
        self.patients_table.select()
        self.patients_table.setHeaderData(0, QtCore.Qt.Orientation.Horizontal, "ID")
        self.patients_table.setHeaderData(1, QtCore.Qt.Orientation.Horizontal, "Имя")
        self.patients_table.setHeaderData(
            2, QtCore.Qt.Orientation.Horizontal, "Фамилия"
        )
        self.patients_table.setHeaderData(
            3, QtCore.Qt.Orientation.Horizontal, "Дата рождения"
        )
        self.patients_table.setHeaderData(4, QtCore.Qt.Orientation.Horizontal, "Пол")
        self.patients_table.setHeaderData(
            5, QtCore.Qt.Orientation.Horizontal, "Контактный номер"
        )
        self.patients_table.setHeaderData(6, QtCore.Qt.Orientation.Horizontal, "Email")
        self.patients_table.setHeaderData(7, QtCore.Qt.Orientation.Horizontal, "Адрес")
        self.ui.patientsTable.setModel(self.patients_table)
        self.ui.patientsTable.resizeColumnsToContents()

        self.doctors_table = QtSql.QSqlTableModel(self, self.database)
        self.doctors_table.setTable("doctors")
        self.doctors_table.setEditStrategy(
            QtSql.QSqlTableModel.EditStrategy.OnFieldChange
        )
        self.doctors_table.select()
        self.doctors_table.setHeaderData(0, QtCore.Qt.Orientation.Horizontal, "ID")
        self.doctors_table.setHeaderData(1, QtCore.Qt.Orientation.Horizontal, "Имя")
        self.doctors_table.setHeaderData(2, QtCore.Qt.Orientation.Horizontal, "Фамилия")
        self.doctors_table.setHeaderData(
            3, QtCore.Qt.Orientation.Horizontal, "Специальность"
        )
        self.doctors_table.setHeaderData(
            4, QtCore.Qt.Orientation.Horizontal, "Контактный номер"
        )
        self.doctors_table.setHeaderData(5, QtCore.Qt.Orientation.Horizontal, "Email")
        self.doctors_table.setHeaderData(6, QtCore.Qt.Orientation.Horizontal, "Кабинет")
        self.ui.doctorsTable.setModel(self.doctors_table)
        self.ui.doctorsTable.resizeColumnsToContents()

        self.appointments_table = QtSql.QSqlTableModel(self, self.database)
        self.appointments_table.setTable("appointments")
        self.appointments_table.setEditStrategy(
            QtSql.QSqlTableModel.EditStrategy.OnFieldChange
        )
        self.appointments_table.select()
        self.appointments_table.setHeaderData(0, QtCore.Qt.Orientation.Horizontal, "ID")
        self.appointments_table.setHeaderData(
            1, QtCore.Qt.Orientation.Horizontal, "Пациент"
        )
        self.appointments_table.setHeaderData(
            2, QtCore.Qt.Orientation.Horizontal, "Врач"
        )
        self.appointments_table.setHeaderData(
            3, QtCore.Qt.Orientation.Horizontal, "Дата и время"
        )
        self.appointments_table.setHeaderData(
            4, QtCore.Qt.Orientation.Horizontal, "Статус"
        )
        self.appointments_table.setHeaderData(
            5, QtCore.Qt.Orientation.Horizontal, "Примечание"
        )
        self.ui.appointmentsTable.setModel(self.appointments_table)
        self.ui.appointmentsTable.resizeColumnsToContents()

    def clear_status_bar(self):
        if hasattr(self, "status_widget"):
            self.ui.statusbar.removeWidget(self.status_widget)

    def set_status_widget(self, widget: QtWidgets.QWidget):
        self.clear_status_bar()
        self.status_widget = widget
        self.ui.statusbar.addWidget(widget)

    def create_connect_button(self) -> QtWidgets.QPushButton:
        button = QtWidgets.QPushButton("Подключиться")
        button.clicked.connect(self.connect_to_database_clicked)
        return button

    def set_state(self, state: ConnectionState):
        print(f"Setting state to {state}")
        central_status_widget = QtWidgets.QWidget()
        self.set_status_widget(central_status_widget)
        central_status_layout = QtWidgets.QHBoxLayout(central_status_widget)
        central_status_layout.addWidget(QtWidgets.QLabel("Состояние: "))
        state_label = QtWidgets.QLabel()
        central_status_layout.addWidget(state_label)
        if state == ConnectionState.CONNECTED:
            state_label.setText("Подключено")
            state_label.setStyleSheet("color: green")
            self.ui.doctorsTable.setEnabled(True)
            self.ui.patientsTable.setEnabled(True)
            self.ui.appointmentsTable.setEnabled(True)
            self.post_connection_successfull_hook()
        else:
            state_label.setText("Не подключено")
            state_label.setStyleSheet("color: red")
            central_status_layout.addWidget(self.create_connect_button())
            self.ui.doctorsTable.setEnabled(False)
            self.ui.patientsTable.setEnabled(False)
            self.ui.appointmentsTable.setEnabled(False)
        self.ui.statusbar.addWidget(central_status_widget)

    def create_crud_button_handler(
        self,
        dialog_factory: Callable,
        parameters_collecter: Callable[..., Result],
        on_success: Callable[..., bool],
    ):
        def button_handler():
            dialog = dialog_factory()
            if dialog is None:
                return
            fin = Finally(lambda: dialog.deleteLater())
            while True:
                result = dialog.exec()
                if result == QtWidgets.QDialog.DialogCode.Accepted:
                    patient_dict_result = parameters_collecter(dialog.ui)
                    if is_err(patient_dict_result):
                        QtWidgets.QMessageBox.critical(
                            self, "Ошибка", patient_dict_result.unwrap_err()
                        )
                        continue
                    if not on_success(patient_dict_result.unwrap()):
                        continue
                return

        return button_handler

    # ---------- Create Patient ----------
    def create_create_patient_dialog(self) -> QtWidgets.QDialog:
        dialog = QtWidgets.QDialog(self)
        dialog.ui = Ui_CreatePatientForm()
        dialog.ui.setupUi(dialog)
        return dialog

    def collect_create_patient_from_form(
        self, form: Ui_CreatePatientForm
    ) -> Result[dict[str, Any], str]:
        patient_dict = {}
        patient_dict["first_name"] = form.nameEdit.text()
        patient_dict["last_name"] = form.surnameEdit.text()

        birthday_str = form.birthEdit.text()
        try:
            patient_dict["date_of_birth"] = datetime.strptime(birthday_str, "%d.%m.%Y")
        except ValueError:
            return Err("Неверный формат даты. Ожидается ДД.ММ.ГГГГ")

        patient_dict["gender"] = form.genderComboBox.currentText()
        patient_dict["contact_number"] = form.phoneEdit.text()
        patient_dict["email"] = form.emailEdit.text()
        patient_dict["address"] = form.addressEdit.text()
        return Ok(patient_dict)

    def try_create_patient(self, patient_dict: dict[str, Any]) -> bool:
        statement = insert(Patient).values(**patient_dict)

        with self.sessionmaker() as session:
            try:
                session.execute(statement)
                session.commit()
                self.patients_table.select()
                QtWidgets.QMessageBox.information(
                    self, "Добавлено", "Пациент успешно добавлен"
                )
                return True
            except Exception as e:
                QtWidgets.QMessageBox.critical(self, "Ошибка", str(e))
                return False

    # ---------- Delete Patient ----------
    def create_delete_patient_dialog(self) -> QtWidgets.QDialog:
        dialog = QtWidgets.QDialog(self)
        dialog.ui = Ui_EnterIdForm()
        dialog.ui.setupUi(dialog)
        dialog.ui.titleLabel.setText("Удаление пациента")
        return dialog

    def collect_id_from_form(self, form: Ui_EnterIdForm) -> Result[int, str]:
        try:
            return Ok(int(form.idEdit.text()))
        except ValueError:
            return Err("Неверный формат ID. Ожидается число")

    def try_delete_patient(self, patient_id: int) -> bool:
        statement = delete(Patient).where(Patient.patient_id == patient_id)

        with self.sessionmaker() as session:
            try:
                session.execute(statement)
                session.commit()
                self.patients_table.select()
                QtWidgets.QMessageBox.information(
                    self, "Удалено", "Пациент успешно удален"
                )
                return True
            except Exception as e:
                QtWidgets.QMessageBox.critical(self, "Ошибка", str(e))
                return False

    # ---------- Create Doctor ----------
    def create_create_doctor_dialog(self) -> QtWidgets.QDialog:
        dialog = QtWidgets.QDialog(self)
        dialog.ui = Ui_CreateDoctorForm()
        dialog.ui.setupUi(dialog)
        return dialog

    def collect_create_doctor_from_form(
        self, form: Ui_CreateDoctorForm
    ) -> Result[dict[str, Any], str]:
        doctor_dict = {}
        doctor_dict["first_name"] = form.nameEdit.text()
        doctor_dict["last_name"] = form.surnameEdit.text()
        doctor_dict["speciality"] = form.specializationEdit.text()
        doctor_dict["contact_number"] = form.phoneEdit.text()
        doctor_dict["email"] = form.emailEdit.text()
        doctor_dict["office_number"] = form.cabinetEdit.text()
        return Ok(doctor_dict)

    def try_create_doctor(self, doctor_dict: dict[str, Any]) -> bool:
        statement = insert(Doctor).values(**doctor_dict)

        with self.sessionmaker() as session:
            try:
                session.execute(statement)
                session.commit()
                self.doctors_table.select()
                QtWidgets.QMessageBox.information(
                    self, "Добавлено", "Доктор успешно добавлен"
                )
                return True
            except Exception as e:
                QtWidgets.QMessageBox.critical(self, "Ошибка", str(e))
                return False

    # ---------- Delete Doctor ----------
    def create_delete_doctor_dialog(self) -> QtWidgets.QDialog:
        dialog = QtWidgets.QDialog(self)
        dialog.ui = Ui_EnterIdForm()
        dialog.ui.setupUi(dialog)
        dialog.ui.titleLabel.setText("Удаление доктора")
        return dialog
    
    def try_delete_doctor(self, doctor_id: int) -> bool:
        statement = delete(Doctor).where(Doctor.doctor_id == doctor_id)

        with self.sessionmaker() as session:
            try:
                session.execute(statement)
                session.commit()
                self.doctors_table.select()
                QtWidgets.QMessageBox.information(
                    self, "Удалено", "Доктор успешно удален"
                )
                return True
            except Exception as e:
                QtWidgets.QMessageBox.critical(self, "Ошибка", str(e))
                return False

    # ---------- Create Appointment ----------
    def create_create_appointment_dialog(self) -> Optional[QtWidgets.QDialog]:
        dialog = QtWidgets.QDialog(self)
        ui: Ui_CreateAppointmentForm = Ui_CreateAppointmentForm()
        dialog.ui = ui
        dialog.ui.setupUi(dialog)
        try:
            doctors = self.sessionmaker().query(Doctor).all()
        except Exception:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Произошла ошибка при получении данных")
            self.set_state(ConnectionState.DISCONNECTED)
            return None
        
        ui.doctorCombobox.clear()
        for doctor in doctors:
            ui.doctorCombobox.addItem(doctor.first_name + " " + doctor.last_name + " - " + doctor.specialty) # type: ignore
            ui.doctorCombobox.setItemData(ui.doctorCombobox.count() - 1, doctor.doctor_id, QtCore.Qt.ItemDataRole.UserRole)
        
        patients = self.sessionmaker().query(Patient).all()
        ui.patientCombobox.clear()
        for patient in patients:
            ui.patientCombobox.addItem(patient.first_name + " " + patient.last_name + " - " + patient.date_of_birth.strftime("%d.%m.%Y")) # type: ignore
            ui.patientCombobox.setItemData(ui.patientCombobox.count() - 1, patient.patient_id, QtCore.Qt.ItemDataRole.UserRole)
        
        return dialog

    def collect_create_appointment_from_form(self, form: Ui_CreateAppointmentForm) -> Result[dict[str, Any], str]:
        appointment_dict = {}
        appointment_dict["patient_id"] = form.patientCombobox.itemData(form.patientCombobox.currentIndex(), QtCore.Qt.ItemDataRole.UserRole)
        appointment_dict["doctor_id"] = form.doctorCombobox.itemData(form.doctorCombobox.currentIndex(), QtCore.Qt.ItemDataRole.UserRole)
        try:
            appointment_dict["appointment_date"] = datetime.strptime(
                form.dateEdit.text(), "%d.%m.%Y %H:%M"
            )
        except ValueError:
            return Err("Неверный формат даты. Ожидается ДД.ММ.ГГГГ ЧЧ:ММ")
        
        appointment_dict["status"] = form.statusEdit.text()
        appointment_dict["notes"] = form.remarkEdit.toPlainText()
        return Ok(appointment_dict)

    def try_create_appointment(self, appointment_dict: dict[str, Any]) -> bool:
        statement = insert(Appointment).values(**appointment_dict)

        with self.sessionmaker() as session:
            try:
                session.execute(statement)
                session.commit()
                self.appointments_table.select()
                QtWidgets.QMessageBox.information(
                    self, "Добавлено", "Запись успешно добавлена"
                )
                return True
            except Exception as e:
                QtWidgets.QMessageBox.critical(self, "Ошибка", str(e))
                return False

    # ---------- Delete Appointment ----------
    def create_delete_appointment_dialog(self) -> QtWidgets.QDialog:
        dialog = QtWidgets.QDialog(self)
        dialog.ui = Ui_EnterIdForm()
        dialog.ui.setupUi(dialog)
        dialog.ui.titleLabel.setText("Удаление записи")
        return dialog
    
    def try_delete_appointment(self, appointment_id: int) -> bool:
        statement = delete(Appointment).where(Appointment.appointment_id == appointment_id)

        with self.sessionmaker() as session:
            try:
                session.execute(statement)
                session.commit()
                self.appointments_table.select()
                QtWidgets.QMessageBox.information(
                    self, "Удалено", "Запись успешно удалена"
                )
                return True
            except Exception as e:
                QtWidgets.QMessageBox.critical(self, "Ошибка", str(e))
                return False
            
    def post_connection_successfull_hook(self) -> None:
        self.ui.appointmentsTable.setItemDelegateForColumn(1, PatientsItemDelegate(self.patients_table, self))
        self.ui.appointmentsTable.setItemDelegateForColumn(2, DoctorsItemDelegate(self.doctors_table, self))
        for table in [self.ui.patientsTable, self.ui.doctorsTable, self.ui.appointmentsTable]:
            table.resizeColumnsToContents()
