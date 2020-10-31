import os
import numpy as np 
from PIL import Image  
import glob 
import pickle
filelist1 = glob.glob('train/aircrafts/*.png')
filelist2 = glob.glob('train/none/*.png')
filelist3 = glob.glob('train/ships/*.png')

x = np.array([np.array([np.array(Image.open(fname)),[1,0,0]]) for fname in filelist1])
y = np.array([np.array([np.array(Image.open(fname)).astype('float32'),[0,1,0]]) for fname in filelist2])
z = np.array([np.array([np.array(Image.open(fname)).astype('float32'),[0,0,1]]) for fname in filelist3])
w = np.concatenate((x,y,z),axis=0)
np.random.shuffle(w)
print(type(w[0][0]))
w.dump('train_data.npy')

# filelist1 = glob.glob('test/aircrafts/*.png')
# filelist2 = glob.glob('test/none/*.png')
# filelist3 = glob.glob('test/ships/*.png')

# x = np.array([[[np.array(Image.open(fname))],[1,0,0]] for fname in filelist1])
# y = np.array([[[np.array(Image.open(fname))],[0,1,0]] for fname in filelist2])
# z = np.array([[[np.array(Image.open(fname))],[0,0,1]] for fname in filelist3])
# w = np.concatenate((x,y,z),axis=0)
# np.random.shuffle(w)
# print(w.shape)
# w.dump('test_data.npy')