from PyQt5.QtWidgets import *

app = QApplication([])

window = QWidget()

lbl = QLabel("Скільки годин в році?")
ans1 = QRadioButton("Багато")
ans2 = QRadioButton("Незнаю")
ans3 = QRadioButton("Дуже багато")
ans4 = QRadioButton("81623")

main_line = QVBoxLayout()
main_line.addWidget(lbl)

h1 = QHBoxLayout()
h1.addWidget(ans1)
h1.addWidget(ans2)
main_line.addLayout(h1)



def win_label():
    msg = QMessageBox()
    msg.setText("Правильно, ти крутий!")
    msg.exec()

def lose_label():
    msg = QMessageBox()
    msg.setText("Не правильно, але ти крутий!")
    msg.exec()



h2 = QHBoxLayout()
h2.addWidget(ans3)
h2.addWidget(ans4)
main_line.addLayout(h2)

ans1.clicked.connect(win_label)
ans2.clicked.connect(lose_label)
ans3.clicked.connect(lose_label)
ans4.clicked.connect(lose_label)

window.setLayout(main_line)
window.show()

app.exec()