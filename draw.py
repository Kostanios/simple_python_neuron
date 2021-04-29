import cv2 as cv 
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
# img = cv.imread('Resources\Photos\cat.jpg')

# cv.imshow('cat', img)
# blank[:] = 0,255,0
# cv.imshow('green', blank)

cv.rectangle(blank, (0,0), (blank.shape[1]//2,blank.shape[0]//2), (0,255,0), thickness=cv.FILLED)
cv.circle(blank, (blank.shape[1]//2,blank.shape[0]//2), 40, (0,0,255), thickness=-1)
cv.line(blank, (blank.shape[1]//2,blank.shape[0]//2), (blank.shape[1],blank.shape[0]), (255,0,0), thickness=5)
cv.putText(blank, 'hello world', (0,blank.shape[0]//2) , cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,0), thickness=2)
cv.imshow('blank', blank)


cv.waitKey(0)