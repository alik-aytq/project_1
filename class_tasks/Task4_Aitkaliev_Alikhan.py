import cv2 as cv
import numpy as np
import os
from math import ceil

dst='./slides/'
slides=os.listdir(dst)
l=len(slides)

slideshow=np.zeros((700,1200,3),np.uint8)
i=1
a=1.0
b=0.0

slide=cv.imread(dst+slides[i])
slide=cv.resize(slide,(1200,700))

while True:
    if(ceil(a)==0):
        a=1.0
        b=0.0
        i=(i+1)%l
        slide=cv.imread(dst+slides[i])
        slide=cv.resize(slide,(1200,700))

    a-=0.003
    b+=0.003

    slideshow=cv.addWeighted(slideshow,a,slide,b,0)
    cv.imshow("Slideshow",slideshow)
    key=cv.waitKey(1)&0xff
    if key==27:
        break
cv.destroyAllWindows()
