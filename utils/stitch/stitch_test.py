import numpy as np
from PIL import Image
from PIL import ImageFilter
import os
from shutil import rmtree
import matplotlib.pyplot as plt
import pandas as pd
from scipy.misc import toimage

# to remove zeropadding
from  zeropad_remove import zeropad_remove


# 2014-12-05_0000718813_1.png

def stitch(input_dir, output_dir, total_grid):
    images = []
    unique_name = []
    for img in os.listdir(input_dir):
        images.append(img)

        date, name, ext = img.split('_', 3)[:3]
        num, format = ext.split('.')
        
        # Take the unique instances of all occurance matches only on date_name
        if date + '_' + name in img:
            if date + '_' + name not in unique_name:
                unique_name.append(date + '_' + name)
        # print(date + '_' + name + '_' + num + '.' + format)

    # Sorting image list using 2nd occurance of _ to .png 
    images.sort(key=lambda x: int(x[x.find('_', 15) + len('_'): x.rfind('.png')]))

    # Iterates through number of main images
    for kk in range(len(unique_name)):
        # Iterate through number of total grid images
        list_image = []
        for ii in range(len(images)):
            # Iterates through number of grid images for each image
            for jj in range(total_grid+1):
                date, name, ext = (unique_name[kk] + '_' + str(jj) + '.' + format).split('_', 3)[:3]
                num, format = ext.split('.')
                if images[ii] == date + '_' + name + '_' + str(jj) + '.' + format:
                    print('Image: {}'.format(images[ii]))
                    list_image.append(os.path.join(input_dir, images[ii]))

        comb_width = int(513 * 14)
        comb_height = int(513 * 12)

        new_im = Image.new('RGB', (comb_width, comb_height))

        x_offset = 0
        y_offset = 0
        for img in list_image:
            image = Image.open(img)
            # image = zeropad_remove(np.array(image))
            image = toimage(image)
            new_im.paste(image, (x_offset, y_offset))
            x_offset += image.size[0]
            if x_offset == comb_width:
                x_offset = 0
                y_offset += image.size[0]
        
        new_im.save(output_dir + '/' + unique_name[kk] + '.png')

stitch('/home/akmmrahman/ss-master/FCN/dataset/train/GroundTruth/','/home/akmmrahman/ss-master/FCN/dataset/train/train_gt/',168)
