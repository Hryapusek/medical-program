import sys

from dotenv import load_dotenv

from PyQt5 import QtWidgets

from main_window import MainWindow

if __name__ == '__main__':
    load_dotenv()
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
