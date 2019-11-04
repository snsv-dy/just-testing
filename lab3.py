import skimage.io as sk
import os
from matplotlib import pyplot as plt
import cv2


path = "images/input1"

paths = [os.path.join(path, i) for i in os.listdir(path)]

a = [cv2.imread(i) for i in paths]



b = [cv2.flip(i, 1) for i in a]


# plt.subplot(1, 2, 1)
# plt.imshow(a, cmap='gray')

# plt.subplot(1, 2, 2)
# plt.imshow(b, cmap='gray')

# plt.show()

folname = "flippedcv2"

# if not os.path.isfile(folname):
# 	os.mkdir(folname)

print("listing ")
for i in paths:
	print(i)
print("listed")

for i, j in zip(range(len(b)), os.listdir(path)):
	cv2.imwrite(os.path.join(folname, j), b[i])
	print("wirtted: ", j)
	cv2.imwrite(os.path.join(folname, "gray" + j), cv2.cvtColor(b[i], cv2.COLOR_BGR2GRAY))
	print("wirtted: ", j, " gray")