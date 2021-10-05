import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt

def read_fits(dirc,file_name):
  print 'reading ' + file_name + ' at ' + dirc
  data = fits.open(dirc+file_name)
  return data

def read_ascii(dirc,file_name,skip_num=0):
  print 'reading ' + file_name + ' at ' + dirc
  val1=[]; val2=[]
  with  open(dirc+file_name,'r') as ascii_data :
    if skip_num >= 1:
      for i in range(skip_num):
        next(ascii_data)
    for line in ascii_data:
      line = line.strip()
      data = line.split()
      val1=np.append(val1,np.float(data[0]))
      val2=np.append(val2,np.float(data[1]))
  return val1, val2

def define_vspace(hdr):
  coords = read_coord_info(hdr)
  min_vel = (coords[9]-(coords[10]-1)*coords[11])*1.0e-3
  max_vel = (coords[9]+(coords[8]-coords[10])*coords[11])*1.0e-3
  vspace = np.linspace(min_vel,max_vel,coords[8])
  return vspace

def show_imshow(data,min_val=None,max_val=None):
  fig = plt.figure(501)
  show = plt.imshow(data, origin='lower',vmin=min_val,vmax=max_val)
  plt.colorbar(show)
  plt.show()
  plt.close(501)
  
    
