import cv2 as cv

img = cv.imread('Resources\Photos\cat_large.jpg')


cv.imshow('Cat', img)

cv.waitKey(0)

capture = cv.VideoCapture('Resources/Videos/dog.mp4')

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimentions = (width, height)
    return cv.resize(frame, dimentions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    capture.set(3, width)
    capture.set(4, height)
while True:
    isTrue, frame = capture.read()

    resized_frame = rescaleFrame(frame)

    cv.imshow('video', frame)
    cv.imshow('resized video', resized_frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break


capture.release()
cv.destroyAllWindows()