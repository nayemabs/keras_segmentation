import numpy as np
from PIL import Image
from scipy.misc import toimage
import matplotlib.pyplot as plt


def zeropad_remove(img):
    output = np.zeros(img.shape, dtype=np.uint8)
    [rows, cols, channels] = img.shape

    for row in range(rows):
        for col in range(cols):
            output[row, col, :] = img[row, col, :]
            if img[row, 4, 0] == 0 and img[row, 4, 1] == 0 and img[row, 4, 2] == 255:
                for kk in range(4):
                    output[row, kk, 0] = 0
                    output[row, kk, 1] = 0
                    output[row, kk, 2] = 255

            if img[4, col, 0] == 0 and img[4, col, 1] == 0 and img[4, col, 2] == 255:
                for kk in range(4):
                    output[kk, col, 0] = 0
                    output[kk, col, 1] = 0
                    output[kk, col, 2] = 255

            if img[row, (cols-1)-4, 0] == 0 and img[row, (cols-1)-4, 1] == 0 and img[row, (cols-1)-4, 2] == 255:
                for kk in range(4):
                    output[row, cols-4+kk, 0] = 0
                    output[row, cols-4+kk, 1] = 0
                    output[row, cols-4+kk, 2] = 255

            if img[(rows-1)-4, col, 0] == 0 and img[(rows-1)-4, col, 1] == 0 and img[(rows-1)-4, col, 2] == 255:
                for kk in range(4):
                    output[rows-4+kk, col, 0] = 0
                    output[rows-4+kk, col, 1] = 0
                    output[rows-4+kk, col, 2] = 255
    return output


# img = Image.open('before_stitch/Forest/output/2015-01-23_0000607681_71.png')
# img = np.array(img)
# out = zeropad_remove(img=img)

# plt.subplot(1,2,1)
# plt.imshow(img)
# plt.subplot(1,2,2)
# plt.imshow(out)
# plt.show()
# toimage(img).show()
# toimage(out).show()
