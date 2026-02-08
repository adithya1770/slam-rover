import cv2 as cv

img = cv.imread("photos/dog.jpeg")

cv.imshow('Cat', img)


cv.waitKey(0)