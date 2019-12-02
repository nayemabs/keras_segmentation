import numpy as np
def unknown_gen(tar_img, org_img):
   
    height, width, channel = org_img.shape

    #to remove the alpha channel
    if channel == 4:
        org_img = org_img[:,:,:3]
    
    gen_img = np.zeros((height, width, channel))

    print(org_img.shape)
    for h in range(height):
        for w in range(width):
            if tar_img[h, w].any() == 0:
                gen_img[h, w, 0] = 0
                gen_img[h, w, 1] = 0
                gen_img[h, w, 2] = 0
            else:
                gen_img[h, w, 0] = org_img[h, w, 0]
                gen_img[h, w, 1] = org_img[h, w, 1]
                gen_img[h, w, 2] = org_img[h, w, 2]

    return gen_img
