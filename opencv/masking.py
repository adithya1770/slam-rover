import cv2 as cv
import numpy as np
img = cv.imread('photos/cat.jpeg')
cv.imshow('Cat', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank', blank)

circle = cv.circle(blank.copy(), (60, 60), 150, 0)
cv.imshow('Circle', circle)

mask = cv.bitwise_and(img, img, mask=circle)
cv.imshow("masked image", mask)

cv.waitKey(0)