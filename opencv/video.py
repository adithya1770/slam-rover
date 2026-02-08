import cv2 as cv
cv.waitKey(0)
capture = cv.VideoCapture('video/sample.mp4')
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
# make a function which takes frame and scale factor as paramters and frame.shape[0], frame.shape[1] will give height and width which can be multiplied to the height and width and it can be scaled down and use the cv.resize function to resize frames and return it.
# for live video use capture.set(3, width), capture.set(4, length)
cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
capture.release()
cv.destroyAllWindows()