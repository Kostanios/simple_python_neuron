import cv2 as cv

img = cv.imread('cropped_parking_lot_5.JPG')


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