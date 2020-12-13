import os
import matplotlib.pyplot as plt
from matplotlib.pyplot import imread
import numpy as np
import skimage.io as skio
from skimage.color import rgb2gray
from skimage.transform import rescale
import cv2
import pickle


# Generic saving and loading functions slightly modified for my use but found online
# @Source: https://stackoverflow.com/questions/19201290/how-to-save-a-dictionary-to-a-file/32216025

def save_obj(obj, name):
    with open(name + '.pickle', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def load_obj(name):
    with open(name + '.pickle', 'rb') as f:
        return pickle.load(f)

