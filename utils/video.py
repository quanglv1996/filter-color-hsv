import cv2
import numpy as np
from PyQt5.QtCore import pyqtSignal, QThread
import time

class Video(QThread):
    change_pixel_signal = pyqtSignal(np.ndarray)
    
    def __init__(self, path_video):
        super().__init__()
        self.video = cv2.VideoCapture(path_video)
    
    def run(self):
        while(self.video.isOpened()):
            fps = self.video.get(cv2.CAP_PROP_FPS)
            time.sleep(1/(fps+2))
            ret, img = self.video.read()
            if ret:
                self.change_pixel_signal.emit(img)