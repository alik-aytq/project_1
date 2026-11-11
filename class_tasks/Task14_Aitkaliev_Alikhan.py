import cv2 as cv
import numpy as np

img = cv.imread("shapes.jpg")
zoom_img = cv.imread("Corner_part.png")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
corners = cv.cornerHarris(np.float32(gray), 9, 3, 0.04)

harris1 = img.copy()
harris1[corners > 0.01 * corners.max()] = [0, 0, 255]

gray2 = cv.cvtColor(zoom_img, cv.COLOR_BGR2GRAY)
corners2 = cv.cornerHarris(np.float32(gray2), 2, 3, 0.04)

harris2 = zoom_img.copy()
harris2[corners2 > 0.01 * corners2.max()] = [0, 0, 255]



sift = cv.SIFT_create()

kp1 = sift.detect(gray, None)
sift1 = cv.drawKeypoint


s(img, kp1, None, (0, 0, 255))

kp2 = sift.detect(gray2, None)
sift2 = cv.drawKeypoints(zoom_img, kp2, None, (0, 0, 255))



harris1 = cv.resize(harris1, (500, 400))
harris2 = cv.resize(harris2, (500, 400))
sift1 = cv.resize(sift1, (500, 400))
sift2 = cv.resize(sift2, (500, 400))

t = np.hstack((harris1, harris2))
b = np.hstack((sift1, sift2))

res = np.vstack((t, b))

cv.imshow("window", res)

cv.waitKey(0)