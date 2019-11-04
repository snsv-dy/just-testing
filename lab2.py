import skimage.io as sk
import os
from matplotlib import pyplot as plt

path = "images/input1"

paths = [os.path.join(path, i) for i in os.listdir(path)]

a = [sk.imread(i) for i in paths]
b = [i[:, ::-1] for i in a]


# plt.subplot(1, 2, 1)
# plt.imshow(a, cmap='gray')

# plt.subplot(1, 2, 2)
# plt.imshow(b, cmap='gray')

# plt.show()

folname = "flipped"

if not os.path.isfile(folname):
	os.mkdir(folname)

for i, j in zip(range(len(b)), os.listdir(path)):
	sk.imsave(os.path.join(folname, j), b[i])