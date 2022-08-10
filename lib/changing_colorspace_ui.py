import sys
sys.path.append('../.')

import cv2

from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QComboBox, QSlider, QRadioButton
from PyQt5 import uic
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt
from lib.changing_colorspace import ChangeColorSpace
from utils.webcam import Webcam
from utils.image import Image
from utils.video import Video

class ChangingColorspacesUI(QMainWindow):
    def __init__(self, main_window, mode=0):
        super(ChangingColorspacesUI, self).__init__()
        
        # Load the ui file
        uic.loadUi('./ui/changing_colorspace.ui', self)
        
        # Define widgets
        self.horizontalSliderHL = self.findChild(QSlider, 'horizontalSliderHL')
        self.horizontalSliderSL = self.findChild(QSlider, 'horizontalSliderSL')
        self.horizontalSliderVL = self.findChild(QSlider, 'horizontalSliderVL')
        
        self.horizontalSliderHU = self.findChild(QSlider, 'horizontalSliderHU')
        self.horizontalSliderSU = self.findChild(QSlider, 'horizontalSliderSU')
        self.horizontalSliderVU = self.findChild(QSlider, 'horizontalSliderVU')
        
        self.labelHL = self.findChild(QLabel, 'labelHL')
        self.labelSL = self.findChild(QLabel, 'labelSL')
        self.labelVL = self.findChild(QLabel, 'labelVL')
        
        self.labelHU = self.findChild(QLabel, 'labelHU')
        self.labelSU = self.findChild(QLabel, 'labelSU')
        self.labelVU = self.findChild(QLabel, 'labelVU')
        
        self.radioButtonOriginal = self.findChild(QRadioButton, 'radioButtonOriginal')
        self.radioButtonMask = self.findChild(QRadioButton, 'radioButtonMask')
        
        self.labelShow = self.findChild(QLabel, 'labelShow')
        self.labelShow.setStyleSheet("border: 2px solid gray;")
        
        self.comboBoxSamples = self.findChild(QComboBox, 'comboBoxSamples')
        self.pushButtonApply = self.findChild(QPushButton, 'pushButtonApply')
        self.pushButtonBack = self.findChild(QPushButton, 'pushButtonBack')
        
        
        # Object
        self.changing_colorspace_lib = ChangeColorSpace()
        self.dict_colors = self.changing_colorspace_lib.color_dict_HSV
        self.id_mode = mode # Using define mode image, video, webcam
        self.main_window = main_window
        
        if self.id_mode == 0:
            self.webcam = Webcam()
            self.showWebcam()
        elif self.id_mode == 1:
            self.img = Image(self.main_window.path_media)
            self.showImage()
        else:
            self.video = Video(self.main_window.path_media)
            self.showVideo()
            
        self.disply_width = 640
        self.display_height = 480
        
        self.set_value_combox_samples()
        
        # Action
        self.pushButtonApply.clicked.connect(self.evt_btApply_clicked)
        self.pushButtonBack.clicked.connect(self.evt_btBack_clicked)
        self.horizontalSliderHL.valueChanged.connect(self.valueChangeHueLow)
        self.horizontalSliderSL.valueChanged.connect(self.valueChangeSaturationLow)
        self.horizontalSliderVL.valueChanged.connect(self.valueChangeValueLow)
        self.horizontalSliderHU.valueChanged.connect(self.valueChangeHueUpper)
        self.horizontalSliderSU.valueChanged.connect(self.valueChangeSaturationUpper)
        self.horizontalSliderVU.valueChanged.connect(self.valueChangeValueUpper)
        
        
        
        # Show the app
        self.show()
        
    def getValueHSVRange(self):
        h_low = self.horizontalSliderHL.value()
        s_low = self.horizontalSliderSL.value()
        v_low = self.horizontalSliderVL.value()
        
        h_upper = self.horizontalSliderHU.value()
        s_upper = self.horizontalSliderSU.value()
        v_upper = self.horizontalSliderVU.value()
        
        return [h_low, s_low, v_low, h_upper, s_upper, v_upper]

    def set_value_combox_samples(self):
        example_colors = []
        for key_ in self.dict_colors:
            example_colors.append('{}: {}-{}'.format(key_, self.dict_colors[key_][1], self.dict_colors[key_][0]))
        self.comboBoxSamples.addItems(example_colors)
    
    def evt_btApply_clicked(self):
        value = self.comboBoxSamples.currentText()
        key_ = value.split(':')[0]
        
        hl, sl, vl = self.dict_colors[key_][1]
        hu, su, vu = self.dict_colors[key_][0]
        
        self.horizontalSliderHL.setSliderPosition(hl)
        self.horizontalSliderSL.setSliderPosition(sl)
        self.horizontalSliderVL.setSliderPosition(vl)
        self.horizontalSliderHU.setSliderPosition(hu)
        self.horizontalSliderSU.setSliderPosition(su)
        self.horizontalSliderVU.setSliderPosition(vu)
        
        self.labelHL.setText(str(hl))
        self.labelSL.setText(str(sl))
        self.labelVL.setText(str(vl))
        self.labelHU.setText(str(hu))
        self.labelSU.setText(str(su))
        self.labelVU.setText(str(vu))
        
        hl, sl, vl, hu, su, vu = self.get_spacecolor_from_slider()
        self.changing_colorspace_lib.update_colorspaces(hl, sl, vl, hu, su, vu)
        
    def evt_btBack_clicked(self):
        self.close()
        self.main_window.show()
        self.main_window.pushButtonApplyMode.setDisabled(False)
        
    
    def get_spacecolor_from_slider(self):
        hl = int(self.horizontalSliderHL.value())
        sl = int(self.horizontalSliderSL.value())
        vl = int(self.horizontalSliderVL.value())
        hu = int(self.horizontalSliderHU.value())
        su = int(self.horizontalSliderSU.value())
        vu = int(self.horizontalSliderVU.value())
        return hl, sl, vl, hu, su, vu
    
    def valueChangeHueLow(self):
        text = str(self.horizontalSliderHL.value())
        self.labelHL.setText(text)
        hl, sl, vl, hu, su, vu = self.get_spacecolor_from_slider()
        self.changing_colorspace_lib.update_colorspaces(hl, sl, vl, hu, su, vu)
        
    def valueChangeHueUpper(self):
        text = str(self.horizontalSliderHU.value())
        self.labelHU.setText(text)
        hl, sl, vl, hu, su, vu = self.get_spacecolor_from_slider()
        self.changing_colorspace_lib.update_colorspaces(hl, sl, vl, hu, su, vu)
        
    def valueChangeSaturationLow(self):
        text =  str(self.horizontalSliderSL.value())
        self.labelSL.setText(text)
        hl, sl, vl, hu, su, vu = self.get_spacecolor_from_slider()
        self.changing_colorspace_lib.update_colorspaces(hl, sl, vl, hu, su, vu)
    
    def valueChangeSaturationUpper(self):
        text = str(self.horizontalSliderSU.value())
        self.labelSU.setText(text)
        hl, sl, vl, hu, su, vu = self.get_spacecolor_from_slider()
        self.changing_colorspace_lib.update_colorspaces(hl, sl, vl, hu, su, vu)
    
    def valueChangeValueLow(self):
        text = str(self.horizontalSliderVL.value())
        self.labelVL.setText(text)
        hl, sl, vl, hu, su, vu = self.get_spacecolor_from_slider()
        self.changing_colorspace_lib.update_colorspaces(hl, sl, vl, hu, su, vu)
    
    def valueChangeValueUpper(self):
        text = str(self.horizontalSliderVU.value())
        self.labelVU.setText(text)
        hl, sl, vl, hu, su, vu = self.get_spacecolor_from_slider()
        self.changing_colorspace_lib.update_colorspaces(hl, sl, vl, hu, su, vu)
        
    def update_image(self, cv_img):
        """Updates the image_label with a new opencv image"""
        if not self.radioButtonOriginal.isChecked():
            cv_img = self.changing_colorspace_lib.run(cv_img)
        qt_img = self.convert_cv_qt(cv_img)
        self.labelShow.setPixmap(qt_img)
    
    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        if not self.radioButtonOriginal.isChecked():
            rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_GRAY2RGB)
        else:
            rgb_image =  cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(self.disply_width, self.display_height, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)
        
    def showWebcam(self):
        self.webcam.change_pixel_signal.connect(self.update_image)
        self.webcam.start()
        
    def showImage(self):
        self.img.change_pixel_signal.connect(self.update_image)
        self.img.start()
        
    def showVideo(self):
        self.video.change_pixel_signal.connect(self.update_image)
        self.video.start()

def main():
    app = QApplication(sys.argv)
    UIChaningColorspaces = ChangingColorspacesUI()
    app.exec_()
    
if __name__ == '__main__':
    main()
    