import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("mitsubishi_car.png", 0)

d = cv.convertScaleAbs(img, alpha=0.5, beta=0)
b = cv.convertScaleAbs(img, alpha=1.5, beta=40)

d_eq = cv.equalizeHist(d)
b_eq = cv.equalizeHist(b)

def showing(photos, name):
    plt.figure(name, figsize=(7, 6))

    for i, pic in enumerate(photos):
        plt.subplot(3, 2, i * 2 + 1)
        plt.imshow(pic, cmap="gray", vmin=0, vmax=255)
        plt.axis("off")

        plt.subplot(3, 2, i * 2 + 2)
        plt.hist(pic.ravel(), bins=256, range=(0, 256))
        plt.xlim(0, 256)

    plt.tight_layout()


showing([img, d, d_eq], "Dark")
showing([img, b, b_eq], "Bright")
plt.show()