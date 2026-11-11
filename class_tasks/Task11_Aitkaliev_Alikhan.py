
import cv2
import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog
from mpl_toolkits.axes_grid1 import make_axes_locatable

# ==========================================
# 1. SELECT IMAGE
# ==========================================

root = Tk()
root.withdraw()

path = filedialog.askopenfilename(
    title="Select an image",
    filetypes=[
        ("Image files", "*.jpg *.jpeg *.png *.bmp"),
        ("All files", "*.*")
    ]
)

root.destroy()

if not path:
    raise SystemExit("No image selected.")

# Supports paths with non-English characters
image = cv2.imdecode(
    np.fromfile(path, dtype=np.uint8),
    cv2.IMREAD_COLOR
)

if image is None:
    raise ValueError("Could not open the image.")

# ==========================================
# 2. CONVERT IMAGE TO HSV
# ==========================================

rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# ==========================================
# 3. CALCULATE 2D HISTOGRAM
# ==========================================

hist = cv2.calcHist(
    [hsv],
    [0, 1],
    None,
    [180, 256],
    [0, 180, 0, 256]
)

# ==========================================
# 4. CREATE FIGURE
# ==========================================

fig, axes = plt.subplots(
    1, 2,
    figsize=(15, 7)
)

# Original image
axes[0].imshow(rgb)
axes[0].set_title("Original Image", fontsize=14)
axes[0].axis("off")

# ==========================================
# 5. 2D HSV HISTOGRAM
# ==========================================

ax = axes[1]

im = ax.imshow(
    np.log1p(hist.T),
    cmap="inferno",
    origin="lower",
    extent=[0, 180, 0, 256],
    aspect="auto"
)

ax.set_title("2D HSV Histogram", fontsize=14)
ax.set_xlabel("Hue (H)")
ax.set_ylabel("Saturation (S)")

divider = make_axes_locatable(ax)

# ==========================================
# 6. HUE COLOR BAR (BOTTOM)
# ==========================================

ax_hue = divider.append_axes(
    "bottom",
    size="7%",
    pad=0.55
)

hue_hsv = np.zeros(
    (1, 180, 3),
    dtype=np.uint8
)

hue_hsv[0, :, 0] = np.arange(180)
hue_hsv[0, :, 1] = 255
hue_hsv[0, :, 2] = 255

hue_rgb = cv2.cvtColor(
    hue_hsv,
    cv2.COLOR_HSV2RGB
)

ax_hue.imshow(
    hue_rgb,
    aspect="auto",
    extent=[0, 180, 0, 1]
)

ax_hue.set_yticks([])
ax_hue.set_xticks(
    [0, 30, 60, 90, 120, 150, 179]
)
ax_hue.set_xlabel("Hue Color Scale")

# ==========================================
# 7. SATURATION BAR (LEFT)
# ==========================================

ax_sat = divider.append_axes(
    "left",
    size="7%",
    pad=0.55
)

sat_hsv = np.zeros(
    (256, 1, 3),
    dtype=np.uint8
)

# Use green (H=60) to illustrate saturation
sat_hsv[:, 0, 0] = 60
sat_hsv[:, 0, 1] = np.arange(256)
sat_hsv[:, 0, 2] = 255

sat_rgb = cv2.cvtColor(
    sat_hsv,
    cv2.COLOR_HSV2RGB
)

ax_sat.imshow(
    sat_rgb,
    origin="lower",
    aspect="auto",
    extent=[0, 1, 0, 256]
)

ax_sat.set_xticks([])
ax_sat.set_yticks([0, 128, 255])
ax_sat.set_ylabel("Saturation Scale")

# ==========================================
# 8. PIXEL COUNT BAR (RIGHT)
# ==========================================

ax_count = divider.append_axes(
    "right",
    size="5%",
    pad=0.18
)

plt.colorbar(
    im,
    cax=ax_count,
    label="log(1 + Pixel Count)"
)

# ==========================================
# 9. DISPLAY RESULTS
# ==========================================

plt.subplots_adjust(
    left=0.05,
    right=0.95,
    bottom=0.19,
    top=0.88,
    wspace=0.55
)

plt.show()
