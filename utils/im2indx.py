import cv2, os
import numpy as np
def rgb2label(img, color_codes = None, one_hot_encode=False):
    if color_codes is None:
        color_codes = {val:i for i,val in enumerate(set( tuple(v) for m2d in img for v in m2d ))}
    n_labels = len(color_codes)
    result = np.ndarray(shape=img.shape[:2], dtype=int)
    result[:,:] = -1
    for rgb, idx in color_codes.items():
        result[(img==rgb).all(2)] = idx

    if one_hot_encode:
        one_hot_labels = np.zeros((img.shape[0],img.shape[1],n_labels))
        # one-hot encoding
        for c in range(n_labels):
            one_hot_labels[: , : , c ] = (result == c ).astype(int)
        result = one_hot_labels

    return result, color_codes



import glob, os

fSave = open('Train.txt', 'w')

# input_dir = "\"
output_dir = "/home/akmmrahman/ss-master/FCN/dataset/test"
for infile in glob.glob("*.png"):
    fName, ext = os.path.splitext(infile)
    fSave.write(fName+ext+'\n') 
    img = cv2.imread(fName+ext)
    img_labels, color_codes = rgb2label(img)
    cv2.imwrite(os.path.join(output_dir,fName+ext),img_labels)
    print(color_codes) # e.g. to see what the codebook is


    
fSave.close() 


# img1 = os.path.join(os.path.dirname(__file__), 'images', 'main_image.jpg')
# main_image = cv2.imread(img1)

# path = 'D:/OpenCV/Scripts/Images'
# cv2.imwrite(os.path.join(path , 'waka.jpg'), img)
# cv2.waitKey(0)



# img = cv2.imread("0001TP_007170.png")
# img_labels, color_codes = rgb2label(img)
# cv2.imwrite("img2.png",img_labels)
# print(color_codes) # e.g. to see what the codebook is

# img1 = cv2.imread("another_rgb_for_labels.png")
# img1_labels, _ = rgb2label(img1, color_codes) 