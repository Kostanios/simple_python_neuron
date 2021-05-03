import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Resources\Photos\cat.jpg')

rbg = cv.cvtColor(img, cv.COLOR_BGR2RGB)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
plt.imshow(rbg)
plt.show()
cv.imshow('Cat', rbg)

cv.waitKey(0)
#python spaces.py