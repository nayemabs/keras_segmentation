import numpy as np

def im2index(im):
    
    """
    turn a 3 channel RGB image to 1 channel index image
    """
    counter = 0
    counter1 = 0
    print(im.shape)
    assert len(im.shape) == 3
    height, width, ch = im.shape
    assert ch == 3
    m_lable = np.zeros((height, width), dtype=np.uint8)
    for h in range(height):
        for w in range(width):
            if im[h, w, 0] == 0 and im[h, w, 1] == 0 and im[h, w, 2] == 0:
                m_lable[h, w] = 0
                counter1 = counter1 +1
            elif im[h, w, 0] == 0 and im[h, w, 1] == 255 and im[h, w, 2] == 255:
                m_lable[h, w] = 1
                counter1 = counter1 +1
            elif im[h, w, 0] == 255 and im[h, w, 1] == 0 and im[h, w, 2] == 0:
                m_lable[h, w] = 2
                counter1 = counter1 +1
            elif im[h, w, 0] == 0 and im[h, w, 1] == 0 and im[h, w, 2] == 255:
                m_lable[h, w] = 3
                counter1 = counter1 +1
            elif im[h, w, 0] == 0 and im[h, w, 1] == 255 and im[h, w, 2] == 0:
                m_lable[h, w] = 4
                counter1 = counter1 +1
            elif im[h, w, 0] == 255 and im[h, w, 1] == 255 and im[h, w, 2] == 0:
                m_lable[h, w] = 5
                counter1 = counter1 +1
            else:
                m_lable[h, w] = 0
                counter = counter +1
    print(counter)
    print(counter1)
    return m_lable
