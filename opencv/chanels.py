import cv2 as cv
import numpy as np
img = cv.imread('photos/cat.jpeg')
cv.imshow('Cat', img)
b, g, r = cv.split(img)
cv.imshow('Blue', b)
# the places which are lighter have more conc. of blue, whereas where its dark has less conc.
cv.imshow('Green', g)
cv.imshow('Red', r)

merge = cv.merge([b, g ,r])
cv.imshow('merge', merge)

print(img.shape)
print(b.shape)
cv.waitKey(0)