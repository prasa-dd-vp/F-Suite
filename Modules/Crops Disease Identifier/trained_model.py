# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 01:56:41 2018

@author: prasad
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 18:05:05 2018

@author: Prasad
"""

# Step 1: Import the packages
from keras.models import model_from_json
import cv2
import numpy as np

# Step 2: Load the Model from Json File
json_file = open('./model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)

# Step 3: Load the weights
loaded_model.load_weights("./model.h5")
print("Loaded model from disk")

# Step 4: Compile the model
loaded_model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# Step 5: load the image you want to test
img = cv2.imread("./crowdai/c_7/3b9cce3e-5b77-444d-957d-71e3a105d66e___RS_GLSp 7289.jpg")
img = cv2.resize(img, (50,50))
img = img.reshape(1, 50, 50, 3)

# Step 6: Predict to which class your input image has been classified
result = loaded_model.predict_classes(img)
if(result[0] == 1):
    print("Crop is affected")
else:
    print("Crop is not affected")
