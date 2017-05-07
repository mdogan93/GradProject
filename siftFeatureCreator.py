import cv2
import numpy as np
import matplotlib.pyplot as plt


# I cropped out each stereo image into its own file.
# You'll have to download the images to run this for yourself
octo_front = cv2.imread('Resources/MajorProjectResources/LearningSet/Gothic/02_0018.jpg')

def show_rgb_img(img):
    """Convenience function to display a typical color image"""
    return plt.imshow(cv2.cvtColor(img, cv2.CV_32S))

show_rgb_img(octo_front);

def to_gray(color_img):
    gray = cv2.cvtColor(color_img, cv2.COLOR_BGR2GRAY)
    return gray

octo_front_gray = to_gray(octo_front)

plt.imshow(octo_front_gray, cmap='gray');

def gen_sift_features(gray_img):
    sift = cv2.SIFT()
    # kp is the keypoints
    #
    # desc is the SIFT descriptors, they're 128-dimensional vectors
    # that we can use for our final features

    kp, desc = sift.detectAndCompute(gray_img, None)
    print(desc)
    print(kp)
    return kp, desc

gen_sift_features(octo_front_gray)












