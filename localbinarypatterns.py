import sys
sys.path.append('/home/narya/cities-env/lib/python3.4/site-packages')
from skimage import feature
import numpy as np




class LocalBinaryPatterns:
    def __init__(self, numPoints, radius):
        # store the numb of points and radius
        self.numPoints = numPoints
        self.radius = radius



    def describe(self,image,eps=1e-17):
        # compute the LBP of the image and use the LBP representation to build histogram
        lbp = feature.local_binary_pattern(image,self.numPoints,self.radius, method="uniform")
        (hist,_) = np.histogram(lbp.ravel(),bins = np.arange(0,self.numPoints+3),range=(0,self.numPoints+2))

        hist = hist.astype("float")
        hist /= (hist.sum()+eps)


        return hist


