# conding: utf-8
import cv2
import math
import numpy as np

file_src = 'image.jpg'
file_dst = 'dst.jpg'

img_src = cv2.imread(file_src, 1)

cv2.namedWindow('src')
cv2.namedWindow('dst')

img_dst = cv2.flip(img_src, flipCode = 0);

cv2.imshow('src', img_src)
cv2.imshow('dst', img_dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

