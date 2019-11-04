import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as Image
import numpy as np
import cv2
import os

path = "images/input1"
img_paths = os.listdir(path)

# print(img_paths)

imgs = []
for i in range(len(img_paths)):
	igm = Image.imread(path + "/" + img_paths[i])
	
	if igm.dtype == np.float32:
		igm = -igm
		igm += 1.0
	elif igm.dtype == np.uint8:
		igm = 255 - igm
		if igm.shape[-1] == 4:
			igm[:,:,3] = 255




	imgs.append(igm)

# newdir = "images/output"
# for i in range(len(imgs)):
# 	naz = img_paths[i].split(".")
# 	print(naz)
# 	plt.imsave(newdir + "/" + naz[0] + "2." + naz[1], imgs[i], cmap="gray")

wh = 4

fig = plt.figure(figsize=(wh, wh))

# plt.imshow(imgs[7], cmap='gray')

for i in range(len(imgs)):
	a = fig.add_subplot(wh, wh, i + 1)
	# a.set_xlabel(img_paths[i])
	# plt.axis('off')
	plt.imshow(imgs[i], cmap='gray')
	# x += 1
	# if x > 3:
	# 	x = 0
	# 	y += 1
plt.show()