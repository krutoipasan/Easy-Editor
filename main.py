from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMessageBox, QWidget, QPushButton, QListWidget, QFileDialog, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QPixmap
import os
from PIL import Image, ImageFilter

app=QApplication([])
win=QWidget()
win.resize(680, 500)
win.setWindowTitle("Easy Editor")

btn_file=QPushButton("Папка")
btn_file.setCheckable(True)
btn_left=QPushButton("Вліво")
btn_right=QPushButton("Вправо")
btn_mirror=QPushButton("Відзеркалити")
btn_blur=QPushButton("Різкість")
btn_wb=QPushButton("Ч\Б")
picture=QLabel("Картина", alignment=Qt.AlignCenter)

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
Hlayout3.addWidget(btn_blur)
Hlayout3.addWidget(btn_wb)

Vlayout2.addLayout(Hlayout1)
Vlayout2.addLayout(Hlayout2)
Vlayout2.addLayout(Hlayout3)

mainlayout.addLayout(Vlayout1)
mainlayout.addLayout(Vlayout2)

win.setLayout(mainlayout)


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
    #btn_file.isChecked()
    extensions=[".jpg", ".jpeg", ".png", ".webp", ".gif"]
    choosefiledir()
    files=filter(os.listdir(filedir), extensions)
    filelist.clear()
    for file in files:
        filelist.addItem(file)

class ImageProcessor():
    def __init__(self):
        self.picture=None
        self.dir=None
        self.filename=None
        self.save_dir=("Modified/")

    def loadImage(self, dir, filename):
        self.dir=dir
        self.filename=filename
        thefile=os.path.join(filedir, filename)
        self.image = Image.open(thefile)

    def saveimage(self):
        save_path=os.path.join(self.dir, self.save_dir)
        if not(os.path.exists(save_path) or os.path.isdir(save_path)):
            os.mkdir(save_path)
        self.image.save(os.path.join(save_path, self.filename))
    
    def do_bw(self):
        self.image=self.image.convert("L")
        self.saveimage()
        img_path=os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(img_path)

    def do_mirror(self):
        self.image=self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.saveimage()
        img_path=os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(img_path)

    def do_blur(self):
        self.image=self.image.filter(ImageFilter.BLUR)
        self.saveimage()
        img_path=os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(img_path)

    def turn_right(self):
        self.image=self.image.transpose(Image.ROTATE_90)
        self.saveimage()
        img_path=os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(img_path)

    def turn_left(self):
        self.image=self.image.transpose(Image.ROTATE_270)
        self.saveimage()
        img_path=os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(img_path)

    def showImage(self, path):
        picture.hide()
        pmimage=QPixmap(path)
        w = picture.width()
        h =  picture.height()
        pmimage=pmimage.scaled(w, h, Qt.KeepAspectRatio)
        picture.setPixmap(pmimage)
        picture.show()

def error():
    error_message=QMessageBox()
    error_message.setIcon(QMessageBox.Warning)
    error_message.setWindowTitle("Обережно!")
    error_message.setText("Ви не обрали папку для ваших фотографій!")
    error_message.setStandardButtons(QMessageBox.Ok)
    error_message.exec_()
    error_message.show()

def showchosenimage():
    if filelist.currentRow() >= 0:
        filename=filelist.currentItem().text()
        workImage.loadImage(filedir, filename)
        workImage.showImage(os.path.join(filedir, filename))

workImage=ImageProcessor()


filelist.currentRowChanged.connect(showchosenimage)
def btn_file_clicked():
    if btn_file.isChecked():
        showfilenameslist()
        # Connect buttons to their functions
        btn_left.clicked.disconnect()
        btn_left.clicked.connect(workImage.turn_left)
        btn_right.clicked.disconnect()
        btn_right.clicked.connect(workImage.turn_right)
        btn_mirror.clicked.disconnect()
        btn_mirror.clicked.connect(workImage.do_mirror)
        btn_blur.clicked.disconnect()
        btn_blur.clicked.connect(workImage.do_blur)
        btn_wb.clicked.disconnect()
        btn_wb.clicked.connect(workImage.do_bw)

btn_file.clicked.connect(btn_file_clicked)
btn_left.clicked.connect(error)
btn_right.clicked.connect(error)
btn_mirror.clicked.connect(error)
btn_blur.clicked.connect(error)
btn_wb.clicked.connect(error)

win.show()
app.exec()
