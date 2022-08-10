import sys
sys.path.append('../.')

import os
from pathlib import Path

from PyQt5.QtWidgets import QMainWindow, QApplication,QInputDialog, QFileDialog, QPushButton, QTextBrowser, QLabel, QRadioButton
from PyQt5 import uic
from PyQt5 import QtWidgets

from lib.changing_colorspace_ui import ChangingColorspacesUI

class MainUI(QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        
        # Load the ui file
        uic.loadUi('./ui/main.ui', self)
        
        # Define widgets
        self.radioButtonWebcam = self.findChild(QRadioButton, 'radioButtonWebcam')
        self.radioButtonVideo = self.findChild(QRadioButton, 'radioButtonVideo')
        self.radioButtonImage = self.findChild(QRadioButton, 'radioButtonImage')
        
        self.textBrowserChooseFile = self.findChild(QTextBrowser, 'textBrowserChooseFile')
        self.pushButtonChooseFile = self.findChild(QPushButton, 'pushButtonChooseFile')
        self.pushButtonApplyMode = self.findChild(QPushButton, 'pushButtonApplyMode')
        
        # Object
        self.radioButtonWebcam.toggled.connect(self.chooseMode)
        self.radioButtonImage.toggled.connect(self.chooseMode)
        self.radioButtonVideo.toggled.connect(self.chooseMode)
        
        self.pushButtonChooseFile.clicked.connect(self.openFileNameDialog)
        self.pushButtonApplyMode.clicked.connect(self.open_window)
        self.textBrowserChooseFile.setDisabled(True)
        self.pushButtonChooseFile.setDisabled(True)
        
        # Action
        self.id_mode = 0
        self.path_media = ''
        
        # Show the app
        self.show()
        
    def open_window(self):
        self.window = QMainWindow()
        self.ui = ChangingColorspacesUI(self, mode=self.id_mode)
        self.hide()
        
    def lock_video_image(self, lock=True):
        self.textBrowserChooseFile.setDisabled(lock)
        self.pushButtonChooseFile.setDisabled(lock)
        
    def set_text_browser(self, text=''):
        self.textBrowserChooseFile.setText(text)

        
    def chooseMode(self):
        if self.radioButtonWebcam.isChecked():
            self.lock_video_image(True)
            self.set_text_browser('')
            self.pushButtonApplyMode.setDisabled(False)
            self.id_mode = 0
        elif self.radioButtonImage.isChecked():
            self.lock_video_image(False)
            self.set_text_browser('.jpg, .jpeg, .png')
            self.pushButtonApplyMode.setDisabled(True)
            self.id_mode = 1
        else:
            self.lock_video_image(False)
            self.set_text_browser('.mp4')
            self.pushButtonApplyMode.setDisabled(True)
            self.id_mode = 2
            
    def openFileNameDialog(self):
        current_path = Path(os.path.abspath(os.getcwd()))
        # parrent_path = current_path.parent.absolute()
        # print(parrent_path)
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        if self.radioButtonVideo.isChecked():
            fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", os.path.join(current_path, 'media'),"MP4 Files (*.mp4)", options=options)
        elif self.radioButtonImage.isChecked():
            fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", os.path.join(current_path, 'media'),"Images Files (*.png *.jpeg *.jpg)", options=options)
        else:
            fileName = ''
        if fileName:
            self.textBrowserChooseFile.setText(fileName)
            self.path_media = fileName
            self.pushButtonApplyMode.setDisabled(False)
        
def main():
    app = QApplication(sys.argv)
    UIMain = MainUI()
    app.exec_()
    
if __name__ == '__main__':
    main()