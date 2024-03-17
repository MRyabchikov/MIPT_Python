from PyQt6 import QtWidgets
from calc_ui import Ui_Form
from PyQt6.QtCore import Qt

class Window(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.lineEdit.setText('0')

        self.cur = 0
        self.next = 0

        self.ops = ['+', '-', '*', '/', '%']

        numbers = [self.ui.pushButton_0, self.ui.pushButton_1, self.ui.pushButton_2,
                        self.ui.pushButton_3, self.ui.pushButton_4, self.ui.pushButton_5,
                        self.ui.pushButton_6, self.ui.pushButton_7, self.ui.pushButton_8,
                        self.ui.pushButton_9]
        
        for i in range(10):
            self.connect_button(numbers[i], i)

        self.ui.pushButton_plus.clicked.connect(self.sum)
        self.ui.pushButton_eq.clicked.connect(self.eq)
        self.ui.pushButton_mul.clicked.connect(self.mul)
        self.ui.pushButton_minus.clicked.connect(self.minus)
        self.ui.pushButton_div.clicked.connect(self.div)
        self.ui.pushButton_percent.clicked.connect(self.percent)
        self.ui.pushButton_C.clicked.connect(self.C)
        self.ui.pushButton_del.clicked.connect(self.Del)
        self.ui.pushButton_sqrt.clicked.connect(self.sqrt)
        self.ui.pushButton_sqr.clicked.connect(self.sqr)
        self.ui.pushButton_rev.clicked.connect(self.rev)
        self.ui.pushButton_dot.clicked.connect(self.dot)

    def dot(self):
        text = self.ui.lineEdit.displayText()
        print(text)
        for i in range(len(text)-1, 0, -1):
            if(text[i] == '.'):
                return
            if (not text[i].isdigit()):
                break
        self.ui.lineEdit.setText(text+'.')
    
    def C(self):
        self.ui.lineEdit.setText('0')

    def Del(self):
        text = self.ui.lineEdit.displayText()
        self.ui.lineEdit.setText(text[:-1] if len(text) != 1 else '0')

    def sqrt(self):
        text = self.ui.lineEdit.displayText()
        self.cur = eval(text)**0.5
        self.next = 0
        self.ui.lineEdit.setText(str(self.cur))

    def sqr(self):
        text = self.ui.lineEdit.displayText()
        self.cur = eval(text)**2
        self.next = 0
        self.ui.lineEdit.setText(str(self.cur))

    def rev(self):
        text = self.ui.lineEdit.displayText()
        self.cur = 1/eval(text)
        self.next = 0
        self.ui.lineEdit.setText(str(self.cur))

    def eq(self):
        text = self.ui.lineEdit.displayText()

        self.cur = eval(text)
        self.next = 0

        self.ui.lineEdit.setText(str(self.cur))

    def sum(self):
        self.cur = self.next
        self.next = 0

        text = self.ui.lineEdit.displayText()

        if text[-1] not in self.ops:
            text += '+'
            self.ui.lineEdit.setText(text)
    def mul(self):
        self.cur = self.next
        self.next = 0

        text = self.ui.lineEdit.displayText()

        if text[-1] not in self.ops:
            text += '*'
            self.ui.lineEdit.setText(text)
    def minus(self):
        self.cur = self.next
        self.next = 0

        text = self.ui.lineEdit.displayText()

        if text[-1] not in self.ops:
            text += '-'
            self.ui.lineEdit.setText(text)
    def div(self):
        self.cur = self.next
        self.next = 0

        text = self.ui.lineEdit.displayText()

        if text[-1] not in self.ops:
            text += '/'
            self.ui.lineEdit.setText(text)
    def percent(self):
        self.cur = self.next
        self.next = 0

        text = self.ui.lineEdit.displayText()

        if text[-1] not in self.ops:
            text += '%'
            self.ui.lineEdit.setText(text)


    def connect_button(self, button, number):
        button.clicked.connect(lambda: self.change_number(number))

    def change_number(self, number):
        text = self.ui.lineEdit.displayText()
        last_num = self.next

        self.next *= 10
        self.next += number

        new_text = text + str(self.next)[-1]

        if self.next != last_num:
            if text == '0':
                self.ui.lineEdit.setText(str(self.next)[-1])
            else:
                self.ui.lineEdit.setText(new_text)



        


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Window()
    window.show()

    app.exec()