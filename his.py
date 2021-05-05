import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Resources\Photos\cats 2.jpg')

colored = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('colored', colored)

gray_hist = cv.calcHist([colored], [0], None, [256], [0, 256])

plt.figure()
plt.title('label')
plt.xlabel('bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()
cv.waitKey(0)

# python his.py