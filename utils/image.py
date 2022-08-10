import cv2
import numpy as np
from PyQt5.QtCore import pyqtSignal, QThread
import time

class Image(QThread):
    change_pixel_signal = pyqtSignal(np.ndarray)
    
    def __init__(self, path_img):
        super().__init__()
        self.image = cv2.imread(path_img)
        
    
    def run(self):
        while True:
            if self.image is not None:
                time.sleep(1/30)
                self.change_pixel_signal.emit(self.image)