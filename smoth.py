import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('Resources\Photos\cat.jpg')

avarage = cv.blur(img, (7,7))

gauss = cv.GaussianBlur(img, (7,7), 0)

median = cv.medianBlur(img, 7)

bilateral = cv.bilateralFilter(img, 10, 35, 25)

cv.imshow('cat', bilateral)

cv.waitKey(0)

# python smoth.py