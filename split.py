import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('Resources\Photos\cat.jpg')

blank = np.zeros(img.shape[:2], dtype='uint8')

b,r,g = cv.split(img)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('blue', blue)
cv.imshow('green', green)
cv.imshow('red', red)

cv.waitKey(0)
# python split.py