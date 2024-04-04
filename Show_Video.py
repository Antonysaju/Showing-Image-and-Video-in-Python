import cv2 as cv
import os

capture=cv.VideoCapture("video.mp4")

while True:
    isTrue, frame=capture.read()
    cv.imshow("Video",frame)
    if cv.waitKey(20) & 0xFF==ord('q'):
        break
capture.release()
cv.destroyAllWindows()
cv.waitKey(0)
