import cv2 as cv
import numpy as np

img = cv.imread('Resources\Photos\cats.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('img ',lap )

sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow('sobelx',sobelx )
cv.imshow('sobely',sobely )
cv.imshow('sobel',sobel )

cv.waitKey(0)
#python grad.py