import cv2 as cv

img = cv.imread('Resources\Photos\cat_large.jpg')


cv.imshow('Cat', img)

cv.waitKey(0)

capture = cv.VideoCapture('Resources/Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()