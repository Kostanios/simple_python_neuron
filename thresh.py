import cv2 as cv


img = cv.imread('Resources\Photos\cats.jpg')
cv.imshow('img ',img )

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)

cv.imshow('thresh', thresh )

cv.waitKey(0)
#python thresh.py