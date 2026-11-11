import cv2 as cv
import numpy as np

cap=cv.VideoCapture(0)
k=np.ones((3, 3), np.uint8)

while True:
    _, frame = cap.read()
    frame=cv.resize(frame, (480, 340))
    gray=cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    smooth=cv.GaussianBlur(frame, (15, 15), 0)
    thresh=cv.threshold(gray, 90, 255, cv.THRESH_BINARY_INV)[1]
    morph=cv.morphologyEx(gray, cv.MORPH_GRADIENT, k)

    thresh=cv.cvtColor(thresh, cv.COLOR_GRAY2BGR)
    morph=cv.cvtColor(morph, cv.COLOR_GRAY2BGR)

    t=np.hstack((frame, smooth))
    b=np.hstack((thresh, morph))
    cv.imshow("window", np.vstack((t, b)))

    if cv.waitKey(1) & 0xFF == 27:
        break

