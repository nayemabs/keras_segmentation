import matplotlib.pyplot as plt
import glob, os
from im2index import im2index
import numpy as np
from scipy.misc import toimage
from PIL import Image

# train_output_dir = "/home/akmmrahman/ss-master/FCN/dataset/train/gt_indx/"
# for infile in glob.glob("/home/akmmrahman/ss-master/FCN/dataset/train/gt_grid/*.png"):
#     file, ext = os.path.splitext(infile)
#     img = Image.open(infile)
#     im = np.asarray(img)
#     print(im.shape)
#     print(type(im))
#     img = im2index(im)
#     toimage(img).save(train_output_dir+str(os.path.basename(infile)))

test_output_dir = "/home/akmmrahman/ss-master/FCN/dataset/test/gt_indx/"
for infile in glob.glob("/home/akmmrahman/ss-master/FCN/dataset/test/gt_grid/*.png"):
    file, ext = os.path.splitext(infile)
    img = Image.open(infile)
    im = np.asarray(img)
    print(im.shape)
    print(type(im))
    img = im2index(im)
    toimage(img).save(test_output_dir+str(os.path.basename(infile)))