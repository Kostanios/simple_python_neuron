import cv2 as cv


img = cv.imread('Resources\Photos\cats.jpg')

colored = cv.cvtColor(img, cv.COLOR_BGR2HLS)


blur = cv.GaussianBlur(colored, (7,7), cv.BORDER_DEFAULT)

canny = cv.Canny(blur, 125, 175)

dilated = cv.dilate(canny, (7, 7), iterations=3)

eroded = cv.erode(dilated, (7, 7), iterations=3)

resized = cv.resize(eroded, (900, 900), interpolation=cv.INTER_CUBIC)

cropped = img[50:200, 200:400]
cv.imshow('eroded', resized)


cv.waitKey(0)