import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("r1.png", 0)

f= np.fft.fft2(img)
fshift = np.fft.fftshift(f) #f是一个复数数组 
fft_img = 20 * np.log(np.abs(fshift))

fig, ax = plt.subplots(1,2) #row = 1, col = 2

ax[0].imshow(img, cmap = "gray") 
ax[1].imshow(fft_img, cmap = "gray")


ax[0].axis("off"), ax[1].axis("off")

# plt.savefig("result.jpg", dpi = 300, bbox_inches = "tight")
plt.show()
