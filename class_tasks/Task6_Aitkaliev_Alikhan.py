import cv2 as cv
import numpy as np

img=cv.imread('mitsubishi_car.png')
p=[]

def points(event, x,y,flags,param):
    if event==cv.EVENT_LBUTTONDOWN and len(p)<4:
        p.append([x,y])

cv.imshow('Photo',img)
cv.setMouseCallback('Photo',points)

while len(p)<4:
    cv.waitKey(1)
p1 = np.float32(p)
p2 = np.float32([[0, 0], [500, 0], [500, 500], [0, 500]])

m=cv.getPerspectiveTransform(p1,p2)
r=cv.warpPerspective(img,m,(500,500))

cv.imshow('Result',r)
cv.waitKey(0)
cv.destroyAllWindows()

