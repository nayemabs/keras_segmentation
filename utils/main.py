from unknown_gen import unknown_gen
import numpy as np
from PIL import Image
import os
from scipy.misc import toimage
current_loc = os.getcwd()
txt_folder= 'readfolder'

txt_filename = 'test.txt'
txt_loc = current_loc+'/'+txt_folder+'/'


list = open(txt_loc+txt_filename,'r')
img_list = list.readlines()

 
org_file_loc ='org/'
tar_file_loc ='gt/'
        

ext = '' 

for fname in img_list:
    fname = fname.rstrip('\n')

    org_img = org_file_loc+fname+ext
    org_img = Image.open(org_img)  
    org_img = np.asarray(org_img)
    
    tar_img = tar_file_loc+fname+ext
    tar_img = Image.open(tar_img)
    tar_img = np.asarray(tar_img)



    gen_img = unknown_gen(tar_img, org_img)
    toimage(gen_img).save('UKremoved/'+fname+ext)
