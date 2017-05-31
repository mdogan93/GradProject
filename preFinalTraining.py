import sys
sys.path.append('/home/narya/cities-env/lib/python3.4/site-packages')
import cv2
from imutils import paths
import numpy as np
import os
from sklearn.svm import LinearSVC
from sklearn.externals import joblib
from scipy.cluster.vq import *
from sklearn.preprocessing import StandardScaler
from cv2 import xfeatures2d
import time

now = time.time()

def gen_sift_features(gray_img):
    sift = xfeatures2d.SIFT_create()
    # kp is the keypoints
    # desc is the SIFT descriptors, they're 128-dimensional vectors
    # that we can use for our final features
    kp, desc = sift.detectAndCompute(gray_img, None)
    return kp, desc

# Get the training classes names and store them in a list
train_path = "Resources/MajorProjectResources/LearningSet"


testing_names=[]
kVal = sys.argv[1]
isEqualWeight = sys.argv[2]
for i in range(3,len(sys.argv)):
    testing_names.append(sys.argv[i])

print('Training with k={0} and equal-sized dataset={1} with instance of {2} architectures'.format(kVal,isEqualWeight,testing_names))

# Get all the path to the images and save them in a list
# image_paths and the corresponding label in image_paths
image_paths = []
image_classes = []
# print(testing_names)
for training_name in testing_names:
    dir = os.path.join(train_path, training_name)
    class_path = list(paths.list_images(dir))
    # print(class_path)
    if isEqualWeight=='True':
        image_paths += [class_path[i] for i in range(0,90)]
        image_classes += [training_name] * 90
    else:
        image_paths += class_path
        image_classes += [training_name] * len(class_path)

sift = cv2.xfeatures2d.SIFT_create()

# List where all the descriptors are stored
des_list = []

for image_path in image_paths:
    image_path = image_path.replace('\ ', ' ')
    im = cv2.imread(image_path,0)
    kpts, des = gen_sift_features(im)
    des_list.append((image_path, des))

# print(image_classes)
# Stack all the descriptors vertically in a numpy array
descriptors = des_list[0][1]
for image_path, descriptor in des_list[1:]:
    descriptors = np.vstack((descriptors, descriptor))

# Perform k-means clustering
k = int(kVal)
voc, variance = kmeans(descriptors, k, 1)

# Calculate the histogram of features
im_features = np.zeros((len(image_paths), k), "float32")
for i in range(len(image_paths)):
    words, distance = vq(des_list[i][1], voc)
    for w in words:
        im_features[i][w] += 1

# Perform Tf-Idf vectorization
nbr_occurences = np.sum((im_features > 0) * 1, axis=0)
idf = np.array(np.log((1.0 * len(image_paths) + 1) / (1.0 * nbr_occurences + 1)), 'float32')

# Scaling the words
stdSlr = StandardScaler().fit(im_features)
im_features = stdSlr.transform(im_features)

# Train the Linear SVM
clf = LinearSVC()
clf.fit(im_features, np.array(image_classes))

# Save the SVM
joblib.dump((clf, testing_names, stdSlr, k, voc), "bof.pkl", compress=3)

print("Training Run Time in seconds :" +  str(time.time()-now))