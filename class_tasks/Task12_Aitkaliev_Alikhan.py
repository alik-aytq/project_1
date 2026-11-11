import cv2 as cv
import numpy as np

img = cv.imread("mitsubishi_car.png")
original = img.copy()

start = None
rect = None
result = None
mask = None


def mouse(event, x, y, flags, param):
    global start, rect

    if event == cv.EVENT_LBUTTONDOWN:
        start = (x, y)

    if event == cv.EVENT_LBUTTONUP:
        if start is not None:
            x1, y1 = start
            x2, y2 = x, y

            x = min(x1, x2)
            y = min(y1, y2)
            w = abs(x2 - x1)
            h = abs(y2 - y1)

            if w > 1 and h > 1:
                rect = (x, y, w, h)
            start = None


cv.namedWindow("Original")
cv.setMouseCallback("Original", mouse)

print("G - GrabCut")
print("I - Invert colors")
print("S - Save")

while True:
    show = original.copy()

    if rect is not None:
        x, y, w, h = rect
        cv.rectangle(show, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv.imshow("Original", show)

    k = cv.waitKey(1) & 0xFF

    if k == ord("g") and rect is not None:
        mask = np.zeros(img.shape[:2], np.uint8)
        bg = np.zeros((1, 65), np.float64)
        fg = np.zeros((1, 65), np.float64)

        cv.grabCut(img, mask, rect, bg, fg, 5, cv.GC_INIT_WITH_RECT)

        mask = np.where((mask == 0) | (mask == 2), 0, 1).astype("uint8")

        result = img * mask[:, :, None]
        cv.imshow("Result", result)

    if k == ord("i") and result is not None:
        result = cv.bitwise_not(result)
        cv.imshow("Result", result)

    if k == ord("s") and result is not None:
        cv.imwrite("result.png", result)
        print("Saved!")

    if k == 27:
        break
