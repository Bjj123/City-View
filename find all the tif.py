import os
import sys
import tensorflow as tf
import numpy as np
import random
from scipy.misc import imread, imresize
from Classification import class_names

imageset = np.array([])
labelset = np.array([])
i=1
for dirpath, dirnames, filenames in os.walk("/Users/bjj/Documents/Big Data/UCMerced_LandUse/Images"):
    for filename in filenames:
        if os.path.splitext(filename)[1] == '.tif':
            filepath = os.path.join(dirpath, filename)
            img1 = imread(filepath, mode='RGB')
            img1 = imresize(img1, (224, 224))
            imageset = np.append(imageset, img1)
            labelstring = filter(str.isalpha, filename.split('.')[0])
            labels1 = np.zeros([1, 21])
            labels1[0, class_names.index(labelstring)-1] = 1
            labelset = np.append(labelset, labels1).reshape(-1, 21)
            print "Reading picture %d" % i
            i += 1
imageset.reshape(-1,224,224,3)
np.savez("result.npz", imageset, labelset)
