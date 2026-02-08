import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)

#blank[200:300] = 0, 255 ,0
#cv.imshow('Green', blank)

cv.rectangle(blank, (10,0), (250, 250), (0, 255, 0), thickness=2)
cv.imshow('Rect', blank)
cv.circle(blank, (40,100), 25, (0, 255, 0))
cv.imshow('Circle', blank)
cv.line(blank, (0,0), (10, 25), (0, 255, 255), thickness=3)
cv.imshow('Line', blank)

cv.putText(blank, 'Hello' ,(30, 60), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), thickness=3)
cv.imshow('Text', blank)
cv.waitKey(0)