from typing import Optional

from PyQt5 import QtWidgets, QtSql, QtCore, QtGui

def date_to_str(date: QtCore.QDate):
    return date.toString("yyyy-MM-dd")

class PatientsItemDelegate(QtWidgets.QStyledItemDelegate):
  def __init__(self, patients_model: QtSql.QSqlTableModel, parent=None):
    super().__init__(parent)
    self.patients_model = patients_model

  def get_patient_str(self, row: int):
    return (self.patients_model.data(self.patients_model.index(row, 1)) # type: ignore
                    + " " + self.patients_model.data(self.patients_model.index(row, 2)) # type: ignore
                    + " - " + date_to_str(self.patients_model.data(self.patients_model.index(row, 3)))) # type: ignore

  def find_patient_with_id(self, id) -> Optional[int]:
    for row in range(self.patients_model.rowCount()): # type: ignore
      if self.patients_model.data(self.patients_model.index(row, 0)) == id: # type: ignore
        return row

  def createEditor(self, parent, option, index: QtCore.QModelIndex):
    combobox = QtWidgets.QComboBox(parent)
    for row in range(self.patients_model.rowCount()): # type: ignore
      doctor_str = self.get_patient_str(row)
      combobox.addItem(doctor_str)
      combobox.setItemData(combobox.count() - 1, self.patients_model.data(self.patients_model.index(row, 0)), QtCore.Qt.ItemDataRole.UserRole) # type: ignore
    return combobox

  def setEditorData(self, editor: QtWidgets.QComboBox, index):
    index.model().setData(index, editor.itemData(editor.currentIndex(), QtCore.Qt.ItemDataRole.UserRole)) # type: ignore

  def setModelData(self, editor: QtWidgets.QComboBox, model: QtSql.QSqlTableModel, index): # type: ignore
    model.setData(index, editor.itemData(editor.currentIndex(), QtCore.Qt.ItemDataRole.UserRole))

  def sizeHint(self, option, index):
    label = QtWidgets.QLabel()
    label.setText(self.get_patient_str(self.find_patient_with_id(index.data()))) # type: ignore
    size_hint = label.sizeHint()
    label.destroy()
    return size_hint

  def paint(self, painter: QtGui.QPainter, option: QtWidgets.QStyleOptionViewItem, index):
    found = self.find_patient_with_id(index.data())
    if found is None:
      return
    doc_str = self.get_patient_str(found) # type: ignore
    painter.drawText(option.rect, option.displayAlignment, doc_str)
