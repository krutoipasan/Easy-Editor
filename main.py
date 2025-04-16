from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QHBoxLayout, QVBoxLayout

app=QApplication([])
win=QWidget()

btn_file=QPushButton("Папка")
btn_left=QPushButton("Вліво")
btn_right=QPushButton("Вправо")
btn_mirror=QPushButton("Відзеркалити")
btn_intensity=QPushButton("Різкість")
btn_wb=QPushButton("Ч\Б")

list=QFileDialog()

mainlayout=QHBoxLayout()

Vlayout1=QVBoxLayout()
Vlayout2=QVBoxLayout()

Hlayout1=QHBoxLayout()
Hlayout2=QHBoxLayout()
Hlayout3=QHBoxLayout()

Vlayout1.addWidget(btn_file)
Vlayout1.addWidget(list)


mainlayout.addLayout(Vlayout1)
mainlayout.addLayout(Vlayout2)

win.setLayout(mainlayout)

win.show()
app.exec()