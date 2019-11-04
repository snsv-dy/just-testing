import os
from matplotlib import pyplot as plt
import cv2
import numpy as np
import skimage.exposure
import pydicom as dic

path = "images/input2"
files = os.listdir(path)
print(files)

def contrast_stretch(img):
	v_min, v_max = np.percentile(img, (2, 98))

	return skimage.exposure.rescale_intensity(img, in_range=(v_min, v_max))


# img = plt.imread(os.path.join(path, files[0]))
img = dic.read_file(os.path.join(path, files[2]))
# print(img.pixel_array)
plt.subplot(2, 2, 1)
plt.imshow(img.pixel_array[0], cmap='gray')

plt.subplot(2, 2, 3)
plt.hist(img.pixel_array[0].ravel(), bins=256)

streched = contrast_stretch(img.pixel_array[0])

plt.subplot(2, 2, 2)
plt.imshow(streched, cmap='gray')

plt.subplot(2, 2, 4)
plt.hist(streched.ravel(), bins=256)

plt.show()