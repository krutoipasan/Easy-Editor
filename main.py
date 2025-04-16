from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QListWidget, QFileDialog, QHBoxLayout, QVBoxLayout

app=QApplication([])
win=QWidget()
win.resize(700, 500)
win.setWindowTitle("Easy Editor")

btn_file=QPushButton("Папка")
btn_left=QPushButton("Вліво")
btn_right=QPushButton("Вправо")
btn_mirror=QPushButton("Відзеркалити")
btn_intensity=QPushButton("Різкість")
btn_wb=QPushButton("Ч\Б")

label=QLabel("Картина")

thelist=QListWidget()

mainlayout=QHBoxLayout()

Vlayout1=QVBoxLayout()
Vlayout2=QVBoxLayout()

Hlayout1=QHBoxLayout()
Hlayout2=QHBoxLayout()
Hlayout3=QHBoxLayout()

Vlayout1.addWidget(btn_file)
Vlayout1.addWidget(thelist)

Hlayout2.addWidget(label, 95)
Hlayout3.addWidget(btn_left)
Hlayout3.addWidget(btn_right)
Hlayout3.addWidget(btn_mirror)
Hlayout3.addWidget(btn_intensity)
Hlayout3.addWidget(btn_wb)

Vlayout2.addLayout(Hlayout1)
Vlayout2.addLayout(Hlayout2)
Vlayout2.addLayout(Hlayout3)

mainlayout.addLayout(Vlayout1)
mainlayout.addLayout(Vlayout2)

win.setLayout(mainlayout)

win.show()
app.exec()