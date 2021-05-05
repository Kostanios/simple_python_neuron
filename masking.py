import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('Resources\Photos\cat.jpg')

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank Image', blank)

mask = cv.circle(blank, (img.shape[1]//2 + 100, img.shape[0]//2 + 100), 100, 255, -1)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('mask', masked)
cv.waitKey(0)
# python masking.py