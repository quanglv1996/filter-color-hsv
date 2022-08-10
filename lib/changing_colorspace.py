import sys
sys.path.append('../.')

import cv2
import numpy as np

class ChangeColorSpace(object):
    def __init__(self):
        self.color_dict_HSV = {'black': [[180, 255, 30], [0, 0, 0]],
                                'white': [[180, 18, 255], [0, 0, 231]],
                                'red1': [[180, 255, 255], [159, 50, 70]],
                                'red2': [[9, 255, 255], [0, 50, 70]],
                                'green': [[89, 255, 255], [36, 50, 70]],
                                'blue': [[128, 255, 255], [90, 50, 70]],
                                'yellow': [[35, 255, 255], [25, 50, 70]],
                                'purple': [[158, 255, 255], [129, 50, 70]],
                                'orange': [[24, 255, 255], [10, 50, 70]],
                                'gray': [[180, 18, 230], [0, 0, 40]]} # upper, lower
        
        self.h_lower = 0
        self.s_lower = 0
        self.v_lower = 0
        
        self.h_upper = 0
        self.s_upper = 0
        self.v_upper = 0
        
    def get_colorspaces_sample(self, name='Default'):
        return self.color_dict_HSV[name]
        
        
    def update_colorspaces(self, h_lower, s_lower, v_lower, h_upper, s_upper, v_upper):
        self.h_lower = h_lower
        self.s_lower = s_lower
        self.v_lower = v_lower
        self.h_upper = h_upper
        self.s_upper = s_upper
        self.v_upper = v_upper
    
    def get_colorspaces(self):
        return self.h_lower, self.s_lower, self.v_lower, self.h_upper, self.s_upper, self.v_upper
    
    def show_info(self):
        print('Colorspaces|HL:{}|SL:{}|VL:{}|HU:{}|SU:{}|VU:{}|'.format(self.h_lower, 
                                                                        self.s_lower, 
                                                                        self.v_lower, 
                                                                        self.h_upper, 
                                                                        self.s_upper, 
                                                                        self.v_upper))

    
    def run(self, frame):
        hsvImg = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        color_lower = np.array([self.h_lower, self.s_lower, self.v_lower], np.uint8)
        color_upper = np.array([self.h_upper, self.s_upper, self.v_upper], np.uint8)
        frame = cv2.inRange(hsvImg, color_lower, color_upper)
        return frame