import cv2
import numpy as np
import matplotlib.pyplot as plt
from cv2 import xfeatures2d


octo_front = cv2.imread('Resources/MajorProjectResources/LearningSet/Gothic/02_0018.jpg')

def show_rgb_img(img):
    """Convenience function to display a typical color image"""
    return plt.imshow(cv2.cvtColor(img, cv2.CV_32S))


def to_gray(color_img):
    gray = cv2.cvtColor(color_img, cv2.COLOR_BGR2GRAY)
    return gray

octo_front_gray = to_gray(octo_front)


def gen_sift_features(gray_img):
    sift = xfeatures2d.SIFT_create()
    # kp is the keypoints
    #
    # desc is the SIFT descriptors, they're 128-dimensional vectors
    # that we can use for our final features

    kp, desc = sift.detectAndCompute(gray_img, None)
    # print(desc)
    # print(kp)
    return kp, desc


octo_front_kp, octo_front_desc = gen_sift_features(octo_front_gray)

# print(octo_front_desc[0])
# print(len(octo_front_kp), 'keypoints in the list')
# print(octo_front_kp[0])

def explain_keypoint(kp):
    print('angle\n', kp.angle)
    print('\nclass_id\n', kp.class_id)
    print('\noctave (image scale where feature is strongest)\n', kp.octave)
    print('\npt (x,y)\n', kp.pt)
    print('\nresponse\n', kp.response)
    print('\nsize\n', kp.size)

# explain_keypoint(octo_front_kp[0])










