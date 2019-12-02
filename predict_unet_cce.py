import LoadBatches
from keras.models import load_model
from Models import FCN32, FCN8, SegNet, UNet
import glob,os
import cv2
import numpy as np
import random
from PIL import Image
from scipy.misc import toimage
import matplotlib.pyplot as plt
from decode_segmap import decode_segmap

n_classes = 6

key = "unet"

method = {
    "fcn32": FCN32.FCN32,
    "fcn8": FCN8.FCN8,
    "segnet": SegNet.SegNet,
    'unet': UNet.UNet}

images_path = "data/dataset/test/org_grid/"
segs_path = "data/dataset/test/gt_indx/"
run_dir = "output/"
# output_dir = run_dir + "/rgb/"
indexed_dir = run_dir + "/indexed_unet/"

input_height = 224
input_width = 224

colors = [
    (random.randint(
        0, 255), random.randint(
            0, 255), random.randint(
                0, 255)) for _ in range(n_classes)]

##########################################################################


def label2color(colors, n_classes, seg):
    seg_color = np.zeros((seg.shape[0], seg.shape[1], 3))
    for c in range(n_classes):
        seg_color[:, :, 0] += ((seg == c) *
                               (colors[c][0])).astype('uint8')
        seg_color[:, :, 1] += ((seg == c) *
                               (colors[c][1])).astype('uint8')
        seg_color[:, :, 2] += ((seg == c) *
                               (colors[c][2])).astype('uint8')
    seg_color = seg_color.astype(np.uint8)
    return seg_color


def getcenteroffset(shape, input_height, input_width):
    short_edge = min(shape[:2])
    xx = int((shape[0] - short_edge) / 2)
    yy = int((shape[1] - short_edge) / 2)
    return xx, yy


images = sorted(
    glob.glob(
        images_path +
        "*.jpg") +
    glob.glob(
        images_path +
        "*.png") +
    glob.glob(
        images_path +
        "*.jpeg"))
segmentations = sorted(glob.glob(segs_path + "*.jpg") +
                       glob.glob(segs_path + "*.png") + glob.glob(segs_path + "*.jpeg"))


# m = load_model("output/%s_model.h5" % key)
m = method[key](6, 224, 224)  # 有自定义层时，不能直接加载模型
m.load_weights("output/%s_model_sgd_cce.h5" % key)

for i, (imgName, segName) in enumerate(zip(images, segmentations)):

    print("%d/%d %s" % (i + 1, len(images), imgName))
    fileName = os.path.basename(imgName)
    # print("HAHAHA"+fileName)

    im = cv2.imread(imgName, 1)
    # im=cv2.resize(im,(input_height,input_width))
    xx, yy = getcenteroffset(im.shape, input_height, input_width)
    im = im[xx:xx + input_height, yy:yy + input_width, :]

    seg = cv2.imread(segName, 0)
    # seg= cv2.resize(seg,interpolation=cv2.INTER_NEAREST)
    seg = seg[xx:xx + input_height, yy:yy + input_width]

    pr = m.predict(np.expand_dims(LoadBatches.getImageArr(im), 0))[0]
    pr = pr.reshape((input_height, input_width, n_classes)).argmax(axis=2)
    print("before PIL")
    print(type(pr))
    print(pr.shape)
    # pr = np.uint8(pr)
    # plt.imsave(indexed_dir+fileName, pr)

    # cv2.imshow("img", im)
    pr = decode_segmap(pr)
    plt.imsave(indexed_dir+fileName, pr)
    # cv2.imwrite(indexed_dir+fileName, pr)
    # cv2.imwrite(output_dir+fileName, label2color(colors, n_classes, pr))
    # pr = Image.fromarray(pr)
    # print("PIL shape")
    # print(pr.shape)

    # pr.save(indexed_dir+fileName)
    # toimage(label2color(colors, n_classes,pr)).save(output_dir+fileName)
    
    # cv2.imshow("seg_predict_res", label2color(colors, n_classes, pr))
    # cv2.imshow("seg", label2color(colors, n_classes, seg))

    cv2.waitKey()

