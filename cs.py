import cv2 as cv
import numpy as np

img = cv.imread('Resources\Photos\cats.jpg')

blank = np.zeros(img.shape, dtype='uint8')


colored = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

ret, tresh = cv.threshold(colored, 125, 255, cv.THRESH_BINARY)

blur = cv.GaussianBlur(tresh, (5,5), cv.BORDER_DEFAULT)



canny = cv.Canny(blur, 125, 175)

dilated = cv.dilate(canny, (7, 7), iterations=3)

eroded = cv.erode(dilated, (7, 7), iterations=3)

contours, hierarchies = cv.findContours(eroded, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

print(f'{len(contours)} contour(s) found')

# resized = cv.resize(eroded, (900, 900), interpolation=cv.INTER_CUBIC)

# cropped = img[50:200, 200:400]

cv.drawContours(blank, contours, -1, (0,0,255), 2)

cv.imshow('blank', blank)

cv.imshow('eroded', eroded)


cv.waitKey(0)