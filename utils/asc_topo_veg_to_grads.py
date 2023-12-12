#!/usr/bin/env python

import numpy as np
# from xgrads import CtlDescriptor,open_CtlDataset
import struct
import os

if len(sys.argv)==4:
	topo_file   =  sys.argv[1]
	veg_values  =  sys.argv[2]
	gdat_file   =  sys.argv[3]
else:
	raise ValueError('Use this script like: python asc_to_grads.py Basin_DEM.asc Basin_VEG.asc topo_veg.gdat')

topo_values = np.loadtxt(topo_file, skiprows=6)
veg_values  = np.loadtxt(veg_file , skiprows=6)

n_x = topo_values.shape[0]
n_y = topo_values.shape[1]

# gdat_file = 'test.gdat'
ctrl_file = os.path.basename(gdat_file).split('.')[0]+'.ctl'

with open(gdat_file, 'wb') as file:
    
    for ix in np.fliplr(topo_values.transpose()).flatten():
    
        binary_data = struct.pack("f", ix)
    
        file.write(binary_data)
        
    for iy in np.fliplr(veg_values.transpose()).flatten():
        
        binary_data = struct.pack("f", iy)
        
        file.write(binary_data)
        
fid = open(ctrl_file, 'wt')
fid.write('DSET ^'+gdat_file+'\n')
fid.write('TITLE '+'topography and landcover for SnowModel'+'\n')
fid.write('UNDEF '+str(-9999.0)+'\n')
fid.write('XDEF '+str(int(n_x))+' LINEAR 1.0 1.0\n')
fid.write('YDEF '+str(int(n_y))+' LINEAR 1.0 1.0\n')
fid.write('ZDEF 1 LINEAR 1 1' + '\n')
fid.write('TDEF 1 LINEAR 1jan1999 1yr'+'\n')
fid.write('VARS 2' + '\n')
fid.write('topo 0 0 topography (m)' + '\n')
fid.write('vege 0 0 land cover (SnowModel classes)' + '\n')
fid.write('ENDVARS' + '\n')
fid.close()

# ctl = open_CtlDataset(ctrl_file)
# 
# # print(ctl)
# a = ctl['topo'][0,:,:]
# a.plot()
# 
# b = ctl['vege'][0,:,:]
# b.plot()