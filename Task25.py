#Задание25-1
from PyQt6.QtCore import QSize,Qt
from PyQt6.QtWidgets import QApplication, QMainWindow,QPushButton,QVBoxLayout
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.button=QPushButton('Число нажатий 0!!!')
        self.button.setCheckable(True)
        self.button.clicked.connect(self.the_button_was_clicked)
        self.setCentralWidget(self.button)
        self.count=0




    def the_button_was_clicked(self):
        if self.count==0:
            self.button.setText('Начнем!')
        else:
            self.button.setText('Число нажатий: ' + str(self.count))
        self.count+=1


app=QApplication([])
window=MainWindow()
window.show()
app.exec()


#Задание25-2
def is_palindrome(s):
    if len(s) < 1:
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False
string = str(input("Введите строку:"))
if (is_palindrome(string) == True):
    print("Данная строка палиндром!")
else:
    print("Данная строка не палиндром!")


#Задание25-3
def camelStyle(string):
   words = string.split(' ')
   string = ''.join(word.title() for word in words[0:])
   return string


str = "camel case word pop"
print(camelStyle(str))