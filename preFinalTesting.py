import argparse as ap
import sys
sys.path.append('/home/narya/cities-env/lib/python3.4/site-packages')
import numpy as np
import cv2
from imutils import paths
import os
from sklearn.svm import LinearSVC
from sklearn.externals import joblib
from scipy.cluster.vq import *
from cv2 import xfeatures2d
from Tools import Tools


# Load the classifier, class names, scaler, number of clusters and vocabulary
clf, classes_names, stdSlr, k, voc = joblib.load("bof.pkl")
tools = Tools()
testingSetPath = "Resources/MajorProjectResources/TestingSet"
testing_names=[]


for i in range(1,len(sys.argv)):
    testing_names.append(sys.argv[i])


image_paths = []
image_classes=[]
# testing_names = os.listdir(testingSetPath)

def gen_sift_features(gray_img):
    sift = xfeatures2d.SIFT_create()
    # kp is the keypoints
    # desc is the SIFT descriptors, they're 128-dimensional vectors
    # that we can use for our final features
    kp, desc = sift.detectAndCompute(gray_img, None)
    return kp, desc

for testing_name in testing_names:

    dir = os.path.join(testingSetPath, testing_name)
    class_path = list(paths.list_images(dir))
    image_paths += class_path
    image_classes += [testing_name] * len(class_path)

sift = cv2.xfeatures2d.SIFT_create()

# List where all the descriptors are stored
des_list = []

for image_path in image_paths:
    #print(image_path)
    image_path = image_path.replace('\ ', ' ')
    im = cv2.imread(image_path,0)
    kpts, des = gen_sift_features(im)
    des_list.append((image_path, des))

#print(image_classes)

# Stack all the descriptors vertically in a numpy array
descriptors = des_list[0][1]
for image_path, descriptor in des_list[0:]:
    descriptors = np.vstack((descriptors, descriptor))

#
test_features = np.zeros((len(image_paths), k), "float32")
for i in range(len(image_paths)):
    words, distance = vq(des_list[i][1], voc)
    for w in words:
        test_features[i][w] += 1

# Perform Tf-Idf vectorization
nbr_occurences = np.sum((test_features > 0) * 1, axis=0)
idf = np.array(np.log((1.0 * len(image_paths) + 1) / (1.0 * nbr_occurences + 1)), 'float32')

# Scale the features
test_features = stdSlr.transform(test_features)

# Perform the predictions
predictions = [i for i in clf.predict(test_features)]

accuracyCount=0
totalCount = 0
for i in range(0,len(image_paths)):
    #print(predictions[i])
    #print(image_classes[i])
    if predictions[i]== image_classes[i]:
        accuracyCount+=1
    totalCount+=1

print("Succesfull Guess Count: " + str(accuracyCount))
print("Total Guess Count: " + str(totalCount))

print("Ratio is " + str(float(accuracyCount)/totalCount))
print("----------------------------------------------\n")