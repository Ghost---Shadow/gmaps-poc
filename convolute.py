import numpy as np
##import matplotlib.pyplot as plt
import cv2

##from helpers import *

data = np.load('./data/result_matrix.npy')

data = cv2.resize(data, (500,500))

##data = cv2.blur(data,(5,5))
data = cv2.GaussianBlur(data,(5,5),0)

data /= np.max(data)
cv2.imshow('window',data * 255)
