import cv2 as cv

def nothing(x):
    pass

img = cv.imread('mitsubishi_car.png', cv.IMREAD_GRAYSCALE)
cv.namedWindow('image')

cv.createTrackbar('1_threshold', 'image', 100, 255, nothing)
cv.createTrackbar('2_threshold', 'image', 200, 255, nothing)

while True:
    a = cv.getTrackbarPos('1_threshold', 'image')
    b = cv.getTrackbarPos('2_threshold', 'image')
    edges = cv.Canny(img, a, b)
    cv.imshow('image', edges)
    cv.waitKey(1)
