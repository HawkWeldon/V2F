import cv2
import os
import numpy as np
vid = cv2.VideoCapture('')
success,image = vid.read()
c = 0
while success:
  os.system('cls')
  cv2.imwrite("......./Op/Frame%05d.png" % c, image)    
  success,image = vid.read()
  print('Reading frame: ', c)
  c = c + 1
os.system('cls')
print('done')
