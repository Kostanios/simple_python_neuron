import cv2 as cv
import pytesseract
from imutils import contours
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

image = cv.imread("Resources/cars/bentley.jpg")


height, width, _ = image.shape


gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
thresh = cv.threshold(gray, 0, 255, cv.THRESH_OTSU)[1]


cnts = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
cnts, _ = contours.sort_contours(cnts[0])
for c in cnts:
    area = cv.contourArea(c)
    x, y, w, h = cv.boundingRect(c)
    if area > 5000:
        img = image[y: y+h, x: x+w]
        result = pytesseract.image_to_string(img, lang="rus+eng")
        if len(result) > 7:
            print(result, "-result")


cv.waitKey(0)