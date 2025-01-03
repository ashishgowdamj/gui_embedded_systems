from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QFileDialog

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(884, 638)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 871, 601))
        font = QtGui.QFont()
        font.setBold(True)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(290, 140, 291, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(210, 140, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(210, 190, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(290, 190, 91, 31))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(320, 30, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
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
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(590, 140, 81, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(490, 190, 91, 31))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(410, 190, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(450, 270, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color:red;\n"
"color:white;\n"
"border-radius:20;")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 270, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color:green;\n"
"color:white;\n"
"border-radius:20;")
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 884, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connect the buttons to their respective functions
        self.pushButton_2.clicked.connect(self.start_timer)
        self.pushButton_5.clicked.connect(self.stop_timer)
        self.lineEdit_2.setReadOnly(True)
        self.pushButton_6.clicked.connect(self.browse_file)


        self.timer = QtCore.QTimer()  # Create a QTimer object
        self.timer.timeout.connect(self.update_timer)  # Connect the timer to the update_timer function
        self.timer_started = False  # Flag to keep track of whether the timer has started

    def start_timer(self):
        if not self.timer_started:
            self.start_time = QtCore.QTime.currentTime()  # Get the current time when the start button is clicked
            self.timer.start(1000)  # Start the timer with 1 second interval
            self.timer_started = True

    def stop_timer(self):
        if self.timer_started:
            self.timer.stop()
            self.timer_started = False
            self.update_timer()  # Update the timer display to show the final time

    def update_timer(self):
        if self.timer_started:
            current_time = QtCore.QTime.currentTime()
            elapsed_time = self.start_time.msecsTo(current_time) / 1000  # Calculate elapsed time in seconds
            display_time = QtCore.QTime(0, 0, 0).addSecs(round(elapsed_time)).toString("hh:mm:ss")  # Start from 00:00:00
            self.lineEdit_2.setText(display_time)

        # Your existing code for other UI elements


    def browse_file(self):
        file_path, _ = QFileDialog.getOpenFileName(None, "Open File", "", "All Files (*);;Text Files (*.txt)") # Filter to show only text files
        if file_path:
            self.lineEdit.setText(file_path)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "  Enter the file name"))
        self.label.setText(_translate("MainWindow", "File Name:"))
        self.label_2.setText(_translate("MainWindow", "Start Time:"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "  HH:MM:SS"))
        self.pushButton_4.setText(_translate("MainWindow", "Replay"))
        self.pushButton_6.setText(_translate("MainWindow", "Browse..."))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "  HH:MM:SS"))
        self.label_3.setText(_translate("MainWindow", "End Time:"))
        self.pushButton_5.setText(_translate("MainWindow", "STOP"))
        self.pushButton_2.setText(_translate("MainWindow", "START"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
