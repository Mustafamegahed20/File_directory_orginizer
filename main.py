from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QFileDialog, QGraphicsView
import os 
import shutil 
import sys
import time
from mainui import Ui_MainWindow
class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.open)            
        
        self.pushButton_2.clicked.connect(self.organize_files)

        self.show()
                   
    def open(self):
        global current_path
        current_path =str(QFileDialog.getExistingDirectory(self,"Choose Directory"))
        self.label_2.setText(current_path)
        print(current_path)
    
        
    def organize_files(self,counter):    
      ## organize imagess into imagess folder 
        for filename in os.listdir(current_path):
            if filename.endswith((".jpg",".png",".jpeg")):
                if not os.path.exists(current_path + "/imagess"):
                    os.mkdir(current_path + "/imagess")
                source=os.path.join(current_path,filename)    
                shutil.copy(source,current_path + "/imagess")
                os.remove(source)
                
                
                
                print("done imagess")
             
                
        ## organize docs into docs folder 
        for filename in os.listdir(current_path):
            if filename.endswith((".pdf",".word","txt",".docs","xml","pptx")):
                if not os.path.exists(current_path + "/docs"):
                    os.mkdir(current_path + "/docs")
                source=os.path.join(current_path,filename)    
                shutil.copy(source,current_path + "/docs")
                os.remove(source)
                print("done docs")
                
        ## organize archives into archives folder 
        for filename in os.listdir(current_path):
            if filename.endswith((".zip",".rar")):
                if not os.path.exists(current_path + "/archives"):
                    os.mkdir(current_path + "/archives")
                source=os.path.join(current_path,filename)    
                shutil.copy(source,current_path + "/archives")
                os.remove(source)
                print("done archives")
                
        ## organize apps into apps folder 
        for filename in os.listdir(current_path):
            if filename.endswith((".exe",".dmg")):
                if not os.path.exists(current_path + "/apps"):
                    os.mkdir(current_path + "/apps")
                source=os.path.join(current_path,filename)    
                shutil.copy(source,current_path + "/apps")
                os.remove(source)
                print("done apps")

                
        ## organize videos into videos folder 
        for filename in os.listdir(current_path):
            if filename.endswith((".mp4","webm","gif")):
                if not os.path.exists(current_path + "/videos"):
                    os.mkdir(current_path + "/videos")
                source=os.path.join(current_path,filename)    
                shutil.copy(source,current_path + "/videos")
                os.remove(source)
                print("done videos")
                
        ## organize songs into songs folder 
        for filename in os.listdir(current_path):
            if filename.endswith((".mp3")):
                if not os.path.exists(current_path + "/songs"):
                    os.mkdir(current_path + "/songs")
                source=os.path.join(current_path,filename)    
                shutil.copy(source,current_path + "/songs")
                os.remove(source)
                print("done songs")
                
        # organize codes into codes folder 
        for filename in os.listdir(current_path):
            if filename.endswith((".py",".css",".js",".cpp","c",".ipynb",".C#",".R",".php",".go",".html",".java",".swift")):
                if not os.path.exists(current_path + "/codes"):
                    os.mkdir(current_path + "/codes")
                source= os.path.join(current_path,filename)    
                shutil.copy(source,current_path + "/codes")
                os.remove(source)
                print("done codes")
                
        for i in range(100):
            time.sleep(0.1)
            self.progressBar.setValue(i+1)
        self.label_3.setText("Done Organizing this folder successfully !!")    
        print("Done organizing this folder")
        
         
        
app = 0
app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
app.exec_()       
