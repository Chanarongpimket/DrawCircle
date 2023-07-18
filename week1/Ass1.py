import numpy as np
import cv2 as cv

def blockproc(im, block_sc, func):
    h, w = im.shape
    m, n = block_sc
    for x in range(0, h, m):
        for y in range(0, w, n):
            return 0