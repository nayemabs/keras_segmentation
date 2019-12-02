# tif to png convert
from PIL import Image
import glob
import os
Image.MAX_IMAGE_PIXELS = None

for name in glob.glob('*.tif'):
    im = Image.open(name)
    region = im.crop((0, 0, 16304, 16304))
    name = str(name).rstrip(".tif")
    region.save(name + '.png', 'PNG')


def crop_to_selection(src, dst, name):
    os.makedirs(dst)
    img = Image.open(src)
    region = img.crop((0, 0, 16304, 16304))
    img_path = dst + '/' + name + '.png'
    region.save(img_path, 'PNG')
    return img_path