from typing import Optional

from PyQt5 import QtWidgets, QtSql, QtCore, QtGui

class DoctorsItemDelegate(QtWidgets.QStyledItemDelegate):
  def __init__(self, doctors_model: QtSql.QSqlTableModel, parent=None):
    super().__init__(parent)
    self.doctors_model = doctors_model

  def get_doctor_str(self, row: int):
    return (self.doctors_model.data(self.doctors_model.index(row, 1)) # type: ignore
                    + " " + self.doctors_model.data(self.doctors_model.index(row, 2)) # type: ignore
                    + " - " + self.doctors_model.data(self.doctors_model.index(row, 3))) # type: ignore

  def find_doctor_with_id(self, id) -> Optional[int]:
    for row in range(self.doctors_model.rowCount()): # type: ignore
      if self.doctors_model.data(self.doctors_model.index(row, 0)) == id: # type: ignore
        return row

  def createEditor(self, parent, option, index: QtCore.QModelIndex):
    combobox = QtWidgets.QComboBox(parent)
    for row in range(self.doctors_model.rowCount()): # type: ignore
      doctor_str = self.get_doctor_str(row)
      combobox.addItem(doctor_str)
      combobox.setItemData(combobox.count() - 1, self.doctors_model.data(self.doctors_model.index(row, 0)), QtCore.Qt.ItemDataRole.UserRole) # type: ignore
    return combobox

  def setEditorData(self, editor: QtWidgets.QComboBox, index):
    index.model().setData(index, editor.itemData(editor.currentIndex(), QtCore.Qt.ItemDataRole.UserRole)) # type: ignore

  def setModelData(self, editor: QtWidgets.QComboBox, model: QtSql.QSqlTableModel, index): # type: ignore
    model.setData(index, editor.itemData(editor.currentIndex(), QtCore.Qt.ItemDataRole.UserRole))

  def sizeHint(self, option, index):
    label = QtWidgets.QLabel()
    label.setText(self.get_doctor_str(self.find_doctor_with_id(index.data()))) # type: ignore
    size_hint = label.sizeHint()
    label.destroy()
    return size_hint

  def paint(self, painter: QtGui.QPainter, option, index):
    found = self.find_doctor_with_id(index.data())
    if found is None:
      return
    doc_str = self.get_doctor_str(found) # type: ignore
    painter.drawText(option.rect, option.displayAlignment, doc_str)
