from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QListWidget, QFileDialog, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QPixmap
import os
from PIL import Image, ImageFilter

app=QApplication([])
win=QWidget()
win.resize(680, 500)
win.setWindowTitle("Easy Editor")

btn_file=QPushButton("Папка")
btn_left=QPushButton("Вліво")
btn_right=QPushButton("Вправо")
btn_mirror=QPushButton("Відзеркалити")
btn_intensity=QPushButton("Різкість")
btn_wb=QPushButton("Ч\Б")

picture=QLabel("Картина")

filelist=QListWidget()

mainlayout=QHBoxLayout()

Vlayout1=QVBoxLayout()
Vlayout2=QVBoxLayout()

Hlayout1=QHBoxLayout()
Hlayout2=QHBoxLayout()
Hlayout3=QHBoxLayout()

Vlayout1.addWidget(btn_file)
Vlayout1.addWidget(filelist)

Hlayout2.addWidget(picture, 100)
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

class ImageProcessor():
    def __init__(self):
        self.picture=None
        self.dir=None
        self.filename=None
        self.save_dir=("Modified/")
    def loadImage(self, filename):
        self.filename=filename
        thefile=os.path.join(filedir, filename)
        self.image = Image.open(thefile)

workImage=ImageProcessor()

def showImage(self, path):
    picture.hide()
    pmimage=QPixmap(path)
    w = picture.width()
    h =  picture.height()
    pmimage=pmimage.scaled(w, h, Qt.KeepAspectRatio)
    picture.setPixmap(pmimage)
    picture.show()

def showchosenimage():
    if filelist.currentRow() >= 0:
        workImage.filename=filelist.currentItem().text()
        workImage.loadImage(workImage.filename)
        img_path=os.path.join(filedir, workImage.filename)
        showImage(workImage, img_path)

def choosefiledir():
    global filedir
    filedir=QFileDialog.getExistingDirectory()


def filter(files, extensions):
    result=[]
    for file in files:
        for extension in extensions:
            if file.endswith(extension):
                result.append(file)
    return result
    
def showfilenameslist():
    extensions=[".jpg", ".jpeg", ".png", ".webp", ".gif"]
    choosefiledir()
    files=filter(os.listdir(filedir), extensions)
    filelist.clear()
    for file in files:
        filelist.addItem(file)

btn_file.clicked.connect(showfilenameslist)
filelist.itemClicked.connect(showchosenimage)

win.show()
app.exec()