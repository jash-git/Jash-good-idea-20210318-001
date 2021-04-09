#coding:utf-8

import cv2
import numpy as np
import random

img = cv2.imread('test.jpg',1)
shape = img.shape
h = shape[0]
w = shape[1]
dst = np.zeros((h,w,3),np.uint8)
mm = 8          
for m in range(h-mm):             
    for n in range(w-mm):
        index = int(random.random()*8)
        (b,g,r) = img[m+index,n+index]
        dst[m,n] = (b,g,r)
cv2.imwrite("result.jpg", dst)