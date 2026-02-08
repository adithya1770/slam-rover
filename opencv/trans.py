import cv2 as cv
import numpy as np

img = cv.imread("photos/dog.jpeg")

cv.imshow('Cat', img)

# Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)
translated = translate(img, -100, 100)
cv.imshow('Translated', translated)

#Rotation
def rotate(img, angle, rotPoint=(10, 50)):
    (height, width) = img.shape[:2]
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimension = (width, height)

    return cv.warpAffine(img, rotMat, dimension)

rotated = rotate(img, 45)
cv.imshow('Rotated', rotated)

cv.waitKey(0)