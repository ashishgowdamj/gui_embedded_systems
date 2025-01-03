from PyQt6 import QtWidgets
from record import Ui_MainWindow

class MyQtApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyQtApp, self).__init__()
        self.ui = Ui_MainWindow()  # Remove the argument here
        self.ui.setupUi(self)
        self.setWindowTitle("GNSS Record and Replay - User Interface")
        self.ui.main_window = self

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    qt_app = MyQtApp()
    qt_app.show()
    app.exec()
