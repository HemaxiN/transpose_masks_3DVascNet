#directory with the masks
masks_dir = r'D:\iMM\Hemaxi\test\results'

#directory to save the transposed masks to visualize in Fiji
save_dir = r'D:\iMM\Hemaxi\test\transposed'

import os
import tifffile

for msk in os.listdir(masks_dir): #for each mask in "masks_dir"
	mask = tifffile.imread(os.path.join(masks_dir, msk)) #read the mask
	mask = mask.transpose(2,0,1) #the line of code to transpose the channels
	tifffile.imwrite(os.path.join(save_dir, msk), mask) #write the transposed mask in the "save_dir"