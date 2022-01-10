# Importing the libraries
import cv2
import argparse

#import color_detection

import numpy as np
import pandas as pd


def preview_image(img):
    cv2.imshow("Preview", img)
    cv2.waitKey(0)

def detect_color():
    pass

# Creating an argument parser to take image from the command line
argp = argparse.ArgumentParser()
argp.add_argument('-i', '--image', required=True, help="Image Path")
args = vars(argp.parse_args())
img_path = args['image']

in_img = cv2.imread(img_path)  # reading image from the given path
img = cv2.resize(in_img, (1000, 800))

preview_image(img)