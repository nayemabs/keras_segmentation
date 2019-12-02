from image_slicer import ImageSlicer
from PIL import Image
import glob
import os
import gc


def grid_save_image(src, dst, shape):
    # img_name = str(src).rstrip('.jpg')
    # Provide image path and slice size you desire
    img_name = str(os.path.basename(src)).rstrip('.tif')
    slicer = ImageSlicer(src, shape)
    transformed_image = slicer.transform()
    slicer.save_images(transformed_image, dst, img_name)
    gc.collect()

# train_input_gt_dir = '/home/akmmrahman/ss-master/FCN/dataset/source/org/'
# output_dir = '/home/akmmrahman/ss-master/FCN/dataset/source/grid_test/'
train_org = '/home/akmmrahman/ss-master/FCN/dataset/train/org'
train_org_grid = '/home/akmmrahman/ss-master/FCN/dataset/train/org_grid/'
train_gt = '/home/akmmrahman/ss-master/FCN/dataset/train/gt'
train_gt_grid = '/home/akmmrahman/ss-master/FCN/dataset/train/gt_grid/'

test_org = '/home/akmmrahman/ss-master/FCN/dataset/test/org'
test_org_grid = '/home/akmmrahman/ss-master/FCN/dataset/test/org_grid/'
test_gt = '/home/akmmrahman/ss-master/FCN/dataset/test/gt'
test_gt_grid = '/home/akmmrahman/ss-master/FCN/dataset/test/gt_grid/'

# print(output_dir)
for file in os.listdir(train_org):
    print(os.path.join(train_org, file))
    grid_save_image(src=os.path.join(train_org, file), dst=train_org_grid, shape=(224, 224))
    
for file in os.listdir(train_gt):
    print(os.path.join(train_gt, file))
    grid_save_image(src=os.path.join(train_gt, file), dst=train_gt_grid, shape=(224, 224))

for file in os.listdir(test_org):
    print(os.path.join(test_org, file))
    grid_save_image(src=os.path.join(test_org, file), dst=test_org_grid, shape=(224, 224))
    
for file in os.listdir(test_gt):
    print(os.path.join(test_gt, file))
    grid_save_image(src=os.path.join(test_gt, file), dst=test_gt_grid, shape=(224, 224))
