import cv2 as cv
import numpy as np

drawing= False
is_pen=True
paint=np.ones((600, 900, 3),np.uint8) * 255

def nothing(x):
    pass

def draw(event,x,y,flags,param):
    global drawing,paint
    brush_size = max(cv.getTrackbarPos('Brush', 'Settings'), 1)
    eraser_size=max(cv.getTrackbarPos('Eraser',"Settings"),1)

    color=(b,g,r) if is_pen else (255,255,255)
    size=brush_size if is_pen else eraser_size

    if event == cv.EVENT_LBUTTONDOWN:
        drawing=True
        cv.circle(paint,(x,y),size,color,-1)
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing:
            cv.circle(paint,(x,y),size,color,-1)
    elif event == cv.EVENT_LBUTTONUP:
        drawing=False

cv.namedWindow("Settings")
cv.resizeWindow("Settings",420,300)
cv.createTrackbar("R","Settings",0,255,nothing)
cv.createTrackbar("G","Settings",0,255,nothing)
cv.createTrackbar("B","Settings",0,255,nothing)
cv.createTrackbar("Brush","Settings",2,50,nothing)
cv.createTrackbar("Eraser","Settings",0,50,nothing)

cv.namedWindow("Paint")
cv.setMouseCallback("Paint",draw)

while True:
    r = cv.getTrackbarPos('R', 'Settings')
    g = cv.getTrackbarPos('G', 'Settings')
    b = cv.getTrackbarPos('B', 'Settings')
    settings = np.zeros((200, 400, 3), np.uint8)
    settings[:] = (b, g, r)
    cv.imshow('Settings', settings)

    cv.imshow('Paint', paint)

    key = cv.waitKey(1) & 0xFF
    if key == 27:
        break
    elif key == ord('m'):
        is_pen = not is_pen

cv.destroyAllWindows()
