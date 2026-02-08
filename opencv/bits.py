import cv2 as cv
import numpy as np

blank = np.zeros((400, 400), dtype='uint8')
rect = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
circle = cv.circle(blank.copy(), (60, 100), (100), 255, -1)
cv.imshow('rect', rect)
cv.imshow('circle', circle)
bitwise = cv.bitwise_and(rect, circle)
cv.imshow('bitwise', bitwise)
cv.waitKey(0)