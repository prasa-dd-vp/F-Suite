# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 17:37:19 2018

@author: Prasad
"""


import cv2
import os
import time



time.sleep(3)
video = cv2.VideoCapture(r'D:/Download here!/blade3.mp4')
path = r'F:/MRV/bwm/dataset/train_data/video2/'
ret, image = video.read()
i=1669

while ret:
    cv2.imwrite(os.path.join(path+"damage"+str(i+1)+".jpg"), image)
    ret, image = video.read()
    i+=1
	
video.release()
cv2.destroyAllWindows()