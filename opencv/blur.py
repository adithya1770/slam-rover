import cv2 as cv
img = cv.imread('photos/cat.jpeg')
cv.imshow('Cat', img)

#averaging
avg = cv.blur(img, (3,3))
cv.imshow('Avergae', avg)

#Gaussian Blur
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gauss', gauss)

#Median Blur
median = cv.medianBlur(img, 7)
cv.imshow('Median', median)

#Bilateral
bil = cv.bilateralFilter(img, 1, 2 ,1)
cv.imshow("bilateral", bil)

cv.waitKey(0)