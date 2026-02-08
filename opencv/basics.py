import cv2 as cv
img = cv.imread('photos/cat.jpeg')
cv.imshow('Cat', img)

#Conv. to Grayscale

gray = cv.cvtColor(img, cv.COLOR_BGR2HLS)
cv.imshow('gray', gray)

#Blur
blur = cv.GaussianBlur(img, (11, 11), cv.BORDER_DEFAULT)
cv.imshow('BLur', blur)

#Edge Cascade
canny2 = cv.Canny(blur, 125, 175)
cv.imshow('Canny', canny2)
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)

dilate = cv.dilate(canny, (3,3), iterations=1)
cv.imshow('Diltaed', dilate)
#increasese the size of edges i.e from the canny it increases the border size

eroded = cv.erode(dilate, (3, 3), iterations=3)
cv.imshow('Eroded', eroded)


reszed = cv.resize(img, (500, 500))
cv.imshow('resize', reszed)


crop = img[1:2, 1:2]
cv.imshow('Crop', crop)

flip = cv.flip(img, 0)
cv.imshow('flip', flip)

cv.waitKey(0)