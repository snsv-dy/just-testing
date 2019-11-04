import os
from matplotlib import pyplot as plt
import cv2
import numpy as np
import skimage.exposure
import skimage

path = "images/input1"

paths = [os.path.join(path, i) for i in os.listdir(path)]

# a = cv2.imread(paths[1], 0)
a = skimage.data.moon()

# a = np.divide(a, [2])
# a = np.add(a, 255 - np.max(a))

# print(np.divide(a, [2]))

# maxmin = np.min(a)/(np.max(a)-np.min(a))



print(a)

def contrast_stretch(img):
	v_min, v_max = np.percentile(img, (2, 98))

	return skimage.exposure.rescale_intensity(img, in_range=(v_min, v_max))

# b = skimage.exposure.equalize_hist(a)
b = skimage.exposure.equalize_adapthist(a, clip_limit=0.03)
# print(b)



plt.subplot(2, 2, 1)
plt.imshow(a, cmap='gray', vmin=0, vmax=255)

plt.subplot(2, 2, 3)
plt.hist(a.ravel(), bins=256)

# # plt.grid(True)

plt.subplot(2, 2, 2)
plt.imshow(b, cmap='gray')


plt.subplot(2, 2, 4)
plt.hist(b.ravel(), bins=256)

# plt.imshow(b, cmap='gray')
plt.show()