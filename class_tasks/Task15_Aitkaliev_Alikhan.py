import cv2 as cv
import numpy as np
img = cv.imread('shapes.jpg', cv.IMREAD_GRAYSCALE)

panels = []
for name, detector in [('SIFT', cv.SIFT_create(nfeatures=500)),
                       ('ORB', cv.ORB_create(nfeatures=500))]:
    times = []
    for _ in range(20):
        start = cv.getTickCount()
        kp, des = detector.detectAndCompute(img, None)
        times.append((cv.getTickCount() - start) / cv.getTickFrequency() * 1000)

    label = f'{name}: {len(kp)} points, {np.median(times):.2f} ms'
    print(label)

    panel = cv.drawKeypoints(img, kp, None, color=(0, 255, 0))
    cv.putText(panel, label, (10, 25), cv.FONT_HERSHEY_SIMPLEX,
               0.65, (0, 0, 0), 2, cv.LINE_AA)
    panels.append(panel)

cv.imshow('SIFT vs ORB', np.hstack(panels))
cv.waitKey(0)
cv.destroyAllWindows()

