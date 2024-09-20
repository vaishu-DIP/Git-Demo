from skimage import io,color

import matplotlib.pyplot as plt

im = io.imread("image2.jpg")

grayim= color.rgb2gray(im)

plt.subplot(1,2,1)

#display the image using io
io.imshow(grayim)

plt.subplot(1,2,2)

io.imshow(im)

plt.show()
