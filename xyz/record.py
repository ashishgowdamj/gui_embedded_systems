from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QFileDialog
from about import Ui_Dialog
from replay import Ui_MainWindow as ReplayMainWindow
from PyQt6.QtWidgets import QDialog


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 726)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 871, 591))
        font = QtGui.QFont()
        font.setBold(True)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(120, 420, 481, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(40, 420, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(40, 470, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 520, 231, 31))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(760, 470, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color:green;\n"
                                       "color:white;\n"
                                       "border-radius:20;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(760, 530, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color:red;\n"
                                       "color:white;\n"
                                       "border-radius:20;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 20, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color:paleGreen;\n"
                                         "color:black;\n"
                                         "border-style:outset;\n"
                                         "border-width:5px;\n"
                                         "border-color:black;\n"
                                         "border-radius:30;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(360, 20, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color:white;\n"
                                         "color:black;\n"
                                         "border-style:outset;\n"
                                         "border-width:5px;\n"
                                         "border-color:black;\n"
                                         "border-radius:30;\n"
                                         "")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(620, 20, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color:white;\n"
                                         "color:black;\n"
                                         "border-style:outset;\n"
                                         "border-width:5px;\n"
                                         "border-color:black;\n"
                                         "border-radius:30;")
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(320, 140, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(630, 140, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(230, 210, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setPlaceholderText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(540, 210, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setPlaceholderText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(80, 310, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(10, 380, 851, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(80, 200, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(80, 220, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(220, 290, 261, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame)
        self.comboBox_2.setGeometry(QtCore.QRect(540, 290, 251, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(40, 520, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_5.setGeometry(QtCore.QRect(120, 470, 231, 31))
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame)  # Add a QLineEdit for the timer
        self.lineEdit_6.setGeometry(QtCore.QRect(120, 520, 231, 31))  # Adjust position to fit next to progress bar
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.setReadOnly(True)  # Make the timer display read-only
        self.lineEdit_6.setStyleSheet("background-color: lightgray;")  # Set background color
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1080, 38))
        self.menubar.setObjectName("menubar")
        self.menuEmbedded_Systems = QtWidgets.QMenu(self.menubar)
        self.menuEmbedded_Systems.setTitle("")
        self.menuEmbedded_Systems.setObjectName("menuEmbedded_Systems")
        MainWindow.setMenuBar(self.menubar)
#        self.menubar.addAction(self.menuEmbedded_Systems.menuAction)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Create a QTimer object
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.timer_started = False
        self.elapsed_time = QtCore.QTime(0, 0)

        # Connect the replay button to open the replay window
        self.pushButton_4.clicked.connect(self.open_replay_window)
        # Connect the start button to start the timer
        self.pushButton.clicked.connect(self.start_timer)
        # Connect the stop button to stop the timer
        self.pushButton_3.clicked.connect(self.stop_timer)

        # Connect the replay button to open the replay window
        self.pushButton_4.clicked.connect(self.open_replay_window)

        self.menuEmbedded_Systems = QtWidgets.QMenu(self.menubar)
        self.menuEmbedded_Systems.setTitle("Embedded_Systems")

        self.pushButton_5.clicked.connect(self.open_about_dialog)



    def open_replay_window(self):
        self.replay_window = QtWidgets.QMainWindow()
        self.replay_ui = ReplayMainWindow()
        self.replay_ui.setupUi(self.replay_window)
        self.replay_window.show()
        MainWindow.hide()

    def open_about_dialog(self):
        # Create an instance of the QDialog
        self.about_dialog = QDialog()
        # Instantiate the UI defined in about.py
        self.about_ui = Ui_Dialog()
        # Set up the UI in the QDialog instance
        self.about_ui.setupUi(self.about_dialog)
        # Show the dialog
        self.about_dialog.exec()

    def start_timer(self):
        if not self.timer_started:
            self.elapsed_time = QtCore.QTime(0, 0)
            self.timer.start(1000)  # Update every 1 second
            self.timer_started = True
            self.lineEdit_5.setEnabled(False)  # Disable editing
            self.update_timer()

    def stop_timer(self):
        if self.timer_started:
            self.timer.stop()
            self.timer_started = False
            self.lineEdit_5.setEnabled(True)  # Enable editing

    def update_timer(self):
        self.elapsed_time = self.elapsed_time.addSecs(1)
        self.lineEdit_6.setText(self.elapsed_time.toString("HH:mm:ss"))
        self.lineEdit_6.setStyleSheet("color: white;")  # Change the text color to white

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "  Enter the file name"))
        self.label.setText(_translate("MainWindow", "File Name:"))
        self.label_2.setText(_translate("MainWindow", "Duration:"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "  HH:MM:SS"))
        self.pushButton.setText(_translate("MainWindow", "START"))
        self.pushButton_3.setText(_translate("MainWindow", "STOP"))
        self.pushButton_2.setText(_translate("MainWindow", "Record"))
        self.pushButton_4.setText(_translate("MainWindow", "Replay"))
        self.pushButton_5.setText(_translate("MainWindow", "About"))
        self.label_3.setText(_translate("MainWindow", "Rx 1"))
        self.label_4.setText(_translate("MainWindow", "Rx 2"))
        self.label_8.setText(_translate("MainWindow", "#ADC Bits"))
        self.label_9.setText(_translate("MainWindow", "Centre"))
        self.label_10.setText(_translate("MainWindow", "Frequency (MHz)"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Select"))
        self.comboBox.setItemText(1, _translate("MainWindow", "1"))
        self.comboBox.setItemText(2, _translate("MainWindow", "2"))
        self.comboBox.setItemText(3, _translate("MainWindow", "3"))
        self.comboBox.setItemText(4, _translate("MainWindow", "4"))
        self.comboBox.setItemText(5, _translate("MainWindow", "5"))
        self.comboBox.setItemText(6, _translate("MainWindow", "6"))
        self.comboBox.setItemText(7, _translate("MainWindow", "7"))
        self.comboBox.setItemText(8, _translate("MainWindow", "8"))
        self.comboBox.setItemText(9, _translate("MainWindow", "9"))
        self.comboBox.setItemText(10, _translate("MainWindow", "10"))
        self.comboBox.setItemText(11, _translate("MainWindow", "11"))
        self.comboBox.setItemText(12, _translate("MainWindow", "12"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Select"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "1"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "2"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "3"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "4"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "5"))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "6"))
        self.comboBox_2.setItemText(7, _translate("MainWindow", "7"))
        self.comboBox_2.setItemText(8, _translate("MainWindow", "8"))
        self.comboBox_2.setItemText(9, _translate("MainWindow", "9"))
        self.comboBox_2.setItemText(10, _translate("MainWindow", "10"))
        self.comboBox_2.setItemText(11, _translate("MainWindow", "11"))
        self.comboBox_2.setItemText(12, _translate("MainWindow", "12"))
        self.label_5.setText(_translate("MainWindow", "Progress:"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "  HH:MM:SS"))

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.timer_started = False
        self.elapsed_time = QtCore.QTime(0, 0)

        # Connect the replay button to open the replay window
        self.pushButton_4.clicked.connect(self.open_replay_window)
        # Connect the start button to start the timer
        self.pushButton.clicked.connect(self.start_timer)
        # Connect the stop button to stop the timer
        self.pushButton_3.clicked.connect(self.stop_timer)

class MyMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
