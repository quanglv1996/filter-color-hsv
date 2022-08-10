import cv2
import numpy as np
from PyQt5.QtCore import pyqtSignal, QThread
import time

class Webcam(QThread):
    change_pixel_signal = pyqtSignal(np.ndarray)

    def __init__(self):
        super().__init__()
        self.camera = cv2.VideoCapture(0)
        
        
    def run(self):
        while True:
            ret, cv_img = self.camera.read()
            if ret:
                self.change_pixel_signal.emit(cv_img)