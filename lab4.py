import os
from matplotlib import pyplot as plt
import cv2
import numpy as np
import skimage.exposure

path = "images/input1"

paths = [os.path.join(path, i) for i in os.listdir(path)]

a = cv2.imread(paths[1], 0)

# a = np.divide(a, [2])
# a = np.add(a, 255 - np.max(a))

# print(np.divide(a, [2]))

# maxmin = np.min(a)/(np.max(a)-np.min(a))



print(a)

def contrast_stretch(img):
	# return np.array([perc * 255.0 * (i - np.min(a))/(np.max(a)-np.min(a)) for i in a.reshape(1, a.shape[0] * a.shape[1])]) \
	# .reshape(a.shape)
	# perc /= 2.0
	# rangge = (255 * (0.5 - perc / 2), (perc / 2 + 0.5) * 255)
	# print(rangge)
	# rangge = (0.1, 0.9)
	v_min, v_max = np.percentile(img, (2, 98))

	return skimage.exposure.rescale_intensity(img, in_range=(v_min, v_max))

b = contrast_stretch(a)
# print(b)



plt.subplot(2, 2, 1)
plt.imshow(a, cmap='gray', vmin=0, vmax=255)

plt.subplot(2, 2, 3)
plt.hist(a.ravel(), bins=256)

# # plt.grid(True)

plt.subplot(2, 2, 2)
plt.imshow(b, cmap='gray', vmin=0, vmax=255)


plt.subplot(2, 2, 4)
plt.hist(b.ravel(), bins=256)

# plt.imshow(b, cmap='gray')
plt.show()