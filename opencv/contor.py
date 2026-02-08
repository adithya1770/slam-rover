import cv2 as cv
import numpy as np

img = cv.imread('photos/cat.jpeg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

canny = cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)

blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
cv.imshow('BLur', blur)

contours, hierarchies = cv.findContours(gray, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found')

ret, thresh = cv.threshold(gray, 50, 100, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)

cv.drawContours(blank, contours, -1, (0,0,255), 2)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)