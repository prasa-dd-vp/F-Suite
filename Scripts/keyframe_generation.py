# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 08:47:31 2018

@author: Prasad
"""

import numpy as np
import cv2
import time
import os
from PIL import Image

print("Program Started...")

video = cv2.VideoCapture(r'C:\\Users\\Prasad\\Videos\\Glitch.mp4')

counter=0
average_values = []

while(True): 
    
    returnVal, frame = video.read()
    
    if not returnVal:
        break
    
    counter+=1
    if counter==4:
        cv2.imwrite("./sample.png",frame)
        image = Image.fromarray(frame.astype('uint8'), 'RGB')
        temp = list(image.getdata())
        print(temp)
        print(frame)
        
    #average_values.append(np.average(frame))
video.release()

cv2.destroyAllWindows()

print(counter)


#max_value = max(average_values)
#max_frame = average_values.index(mean(average_values))

