import os
import sys
import shutil
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QFileDialog
from PySide2.QtWidgets import QLayout, QPushButton, QHBoxLayout, QVBoxLayout, QSizePolicy
from PySide2.QtCore import Qt, Slot

#import platform
#import getpass
class WPhelper:
    userPATH=os.path.expanduser('~')
    wallAddPATH="\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets"#win10聚焦壁纸目录
    desktopAddPATH="\\Desktop"
    desktopPATH=""
    wallpaperPATH=""
    tempPATH=""#输出壁纸的目录

    def __init__(self):
        #确定环境变量
        self.wallpaperPATH=self.userPATH+self.wallAddPATH
        self.desktopPATH=self.userPATH+self.desktopAddPATH
        self.tempPATH=os.path.join(self.desktopPATH,"WP")
        pass

    def getTempPAHT(self):
        return(self.tempPATH)
    
    def addTempPATH(self):
        #增加WP文件夹到桌面
        if not (os.path.exists(self.tempPATH)):
            os.mkdir(self.tempPATH)

    def movToTempPATH(self,PATH):
        #移动默认壁纸到tempPATH
        for one in os.listdir(self.wallpaperPATH):
            self.imgPATH=self.wallpaperPATH+'\\'+one
            shutil.copyfile(self.imgPATH,self.tempPATH+'\\'+one+".jpg")
    
class Ui(QWidget):
    app=QApplication(sys.argv)
    WPtool = WPhelper()

    #布局
    mainLayout=QVBoxLayout()
    opLayout=QHBoxLayout()
    textDisLayer=QVBoxLayout()
    folderSelectionLayer=QHBoxLayout()
    tempDirPATH=WPtool.getTempPAHT()

    #组件 
    textDisLabel=QLabel("说明: 该工具仅支持Windows 10 \n\n选择文件夹后, 点击导出, 即可将Windows 10锁屏的聚焦壁纸导出. \n\n\n\tFox \n\tv1.0")
    pathLineEdit=QLineEdit(tempDirPATH)
    pathLineEdit.setReadOnly(1)
    # pathLineEdit.setPlaceholderText(tempDirPATH)
    pathLabel=QLabel("路径:")
    addFolderBotton=QPushButton("选择文件夹")
    tempBotton=QPushButton("导出")

    #布局政策
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("获取壁纸工具")
        self.setMinimumSize(400,200)

        self.mainLayout.setAlignment(Qt.AlignCenter)
        self.mainLayout.setContentsMargins(0,0,0,0)

        #添加布局层和组件
        self.mainLayout.addLayout(self.textDisLayer,1)
        self.mainLayout.addLayout(self.opLayout,1)
        self.textDisLayer.addWidget(self.textDisLabel)
        self.opLayout.addLayout(self.folderSelectionLayer)
        self.opLayout.addWidget(self.tempBotton)
        self.folderSelectionLayer.addWidget(self.pathLabel)
        self.folderSelectionLayer.addWidget(self.pathLineEdit)
        self.folderSelectionLayer.addWidget(self.addFolderBotton)
        self.addFolderBotton.clicked.connect(self.openDia)#点击后打开文件夹对话框
        self.tempBotton.clicked.connect(self.moveWP)

        self.setLayout(self.mainLayout)
        
        self.show()
        sys.exit(self.app.exec_())

    def openDia(self):
        diaBrowser=QFileDialog.getExistingDirectory(self,"选择文件夹",self.tempDirPATH.replace('\\','\\\\'))
        if(diaBrowser):
            self.pathLineEdit.setText(diaBrowser)
        else:
            self.pathLineEdit.setText(self.WPtool.getTempPAHT())
        
        return diaBrowser

    def moveWP(self):
        self.WPtool.movToTempPATH(self.pathLineEdit.text())
def main():
    if __name__ == "__main__":
        ui=Ui()

main()
