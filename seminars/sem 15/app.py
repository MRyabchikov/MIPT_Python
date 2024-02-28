from PyQt6 import QtWidgets

import sys

class FirstApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello world")

        self.button = QtWidgets.QPushButton("Send")
        # self.button2 = QtWidgets.QPushButton("2")
        # self.button.setCheckable(True)
        # self.button2.setCheckable(True)

        self.label = QtWidgets.QLabel()
        self.lineEdit = QtWidgets.QLineEdit()


        self.my_layout = QtWidgets.QVBoxLayout()
        self.my_layout.addWidget(self.lineEdit)
        self.my_layout.addWidget(self.label)
        self.my_layout.addWidget(self.button)
        # self.my_layout.addWidget(self.button2)

        self.button.clicked.connect(self.button_func)
        # self.button2.clicked.connect(self.button2_func)
        self.wid = QtWidgets.QWidget()
        self.wid.setLayout(self.my_layout)
        self.setCentralWidget(self.wid)

    def button_func(self):
        text = self.lineEdit.text()
        self.label.setText(text)
    # def button2_func(self, checked):
    #     print("2 Checked? : ", checked)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = FirstApp()
    window.show()

    app.exec()
