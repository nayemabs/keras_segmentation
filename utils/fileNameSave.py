
from glob import glob
import os
fSave = open('test.txt', 'w')

for infile in glob("/home/akmmrahman/ss-master/FCN/dataset/test/org_grid/*.png"):
    fName = os.path.basename(infile)
    fSave.write(fName+'\n') 
fSave.close() 
