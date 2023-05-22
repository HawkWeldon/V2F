import cv2
import os
import numpy as np
vid = cv2.VideoCapture('D:/Code2.0/V2frm/Ip/inp.mp4')
success,image = vid.read()
c = 0
while success:
  os.system('cls')
  cv2.imwrite("D:/Code2.0/V2frm/Op/Frame%05d.png" % c, image)     # save frame as JPEG file      
  success,image = vid.read()
  print('Reading frame: ', c)
  c = c + 1
os.system('cls')
print('done')