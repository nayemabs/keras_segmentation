import numpy as np
# import cv2


def should_i_pass(cropped_image, threshold_area):
    red_pixel = np.count_nonzero((cropped_image == [255, 0, 0]).all(axis=2))
    blue_pixel = np.count_nonzero((cropped_image == [0, 0, 255]).all(axis=2))
    total_pixel = red_pixel + blue_pixel
    target_percentage = 100 * float(blue_pixel) / float(total_pixel)

    """
        print("Non-target red : "+str(redPixel))
        print("Target blue : "+str(bluePixel))
        print("Total : "+str(totalPixel))
        print("Target blue percentage : "+str(target_percentage))
        print("Threshold 5% : "+ str(five_Percentage)) 
    """

    if target_percentage >= threshold_area:
        return 1
    else:
        return 0
