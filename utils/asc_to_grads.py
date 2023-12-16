#!/usr/bin/env python

import numpy as np
# from xgrads import CtlDescriptor,open_CtlDataset
import struct
import os, sys

# print(sys.argv)

if len(sys.argv)>1:
	input_file = sys.argv[1]
else:
	raise ValueError('Use this script like: python asc_to_grads.py grid_lon.asc grid_lon.gdat')

# input_file = '/Volumes/T7/Irtysh_river_basin_parallel/extra_met/grid_lon.asc'

topo_values = np.loadtxt(input_file, skiprows=6)

n_y = topo_values.shape[0]
n_x = topo_values.shape[1]

if len(sys.argv)>2:
    gdat_file = sys.argv[2]
else:
    gdat_file = 'grid_lon.gdat'

ctrl_file = os.path.basename(gdat_file).split('.')[0]+'.ctl'

with open(gdat_file, 'wb') as file:
    
    for ix in np.flipud(topo_values).flatten():
    
        binary_data = struct.pack("f", ix)
    
        file.write(binary_data)
        
fid = open(os.path.join(os.path.dirname(gdat_file), ctrl_file), 'wt')
fid.write('DSET ^'+gdat_file+'\n')
fid.write('TITLE '+'topography and landcover for SnowModel'+'\n')
fid.write('UNDEF '+str(-9999.0)+'\n')
fid.write('XDEF '+str(int(n_x))+' LINEAR 1.0 1.0\n')
fid.write('YDEF '+str(int(n_y))+' LINEAR 1.0 1.0\n')
fid.write('ZDEF 1 LINEAR 1 1' + '\n')
fid.write('TDEF 1 LINEAR 1jan1999 1yr'+'\n')
fid.write('VARS 1' + '\n')
fid.write('data 0 0 topography (m)' + '\n')
fid.write('ENDVARS' + '\n')
fid.close()