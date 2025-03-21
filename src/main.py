import sys

from dotenv import load_dotenv

from PyQt5 import QtWidgets

from main_window import MainWindow
from database_api.schema import init_db
from database_api.schema import Doctor

if __name__ == '__main__':
    load_dotenv()
    init_db()
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
