#!/usr/bin/env python3

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

import src.image_processing as imp

def defaultImage():
    image = mpimg.imread( 'images/solidWhiteRight.jpg' )
    plt.imshow(image)
    plt.show()

if __name__ == '__main__':
    print( imp.get_canny_filter() )

    defaultImage()
    
    
