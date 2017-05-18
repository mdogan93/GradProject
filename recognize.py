from localbinarypatterns import LocalBinaryPatterns
from sklearn.svm import LinearSVC
from PIL import Image
from sklearn.externals import joblib
import os
from Tools import Tools
from imutils import paths
import argparse
import cv2



tools = Tools()
desc = LocalBinaryPatterns(20, 1)
data = []
labels = []


learningSetPath = "Resources/MajorProjectResources/LearningSet"
testingSetPath = "Resources/MajorProjectResources/TestingSet"



ClassList=(tools.getClassNames("Resources/MajorProjectResources/LearningSet"))
# print(ClassList)



for cl in ClassList:
    clLearningFolder = learningSetPath+'/'+cl
    tools.getAllImagesResized(clLearningFolder)
    clPathListLearning = tools.getImagePaths(clLearningFolder)

    for i in range(90):
        image = cv2.imread(clPathListLearning[i])
        gry = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        hist = desc.describe(gry)
        labels.append(cl)
        data.append(hist)

print(data)
model = LinearSVC(C=100.0, random_state=42)
model.fit(data, labels)
joblib.dump(model, 'model.pkl')

accuracyCount=0
totalCount = 0
for cl in ClassList:
    clTestingFolder = testingSetPath+'/'+cl
    tools.getAllImagesResized(clTestingFolder)
    clPathListTesting = tools.getImagePaths(clTestingFolder)
    for i in range(0,len(clPathListTesting)):
        image = cv2.imread(clPathListTesting[i])
        gry = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        hist = desc.describe(gry)
        hist = hist.reshape(1,-1)

        prediction = model.predict(hist)[0]

        print(prediction)
        if prediction==cl:
            accuracyCount+=1
            print("hit")
        else: print("miss")
        totalCount+=1

print("acc Count " + str(accuracyCount))
print("total Count " + str(totalCount))

print(float(accuracyCount/totalCount))






# catsPathListLearning = (tools.getImagePaths(learningSet1))
# dogsPathListLearning = (tools.getImagePaths(learningSet2))
# allPathListTesting = (tools.getImagePaths(testingSet))

# # catsPathListTraining = (tools.getImagePaths("Resources/SubResources/TrainingSet/CatPhotos"))
# # carsPathListTraining = (tools.getImagePaths("Resources/SubResources/TrainingSet/CarPhotos"))
#
# #resizing photos
# tools.getAllImagesResized(learningSet1)
# tools.getAllImagesResized(learningSet2)
# tools.getAllImagesResized(testingSet)
#
# ############### LEARNING ##############
#
# for i in range(0,len(catsPathListLearning)):
#     image = cv2.imread(catsPathListLearning[i])
#     gry = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     hist = desc.describe(gry)
#
#     labels.append("cat")
#     data.append(hist)
#
#
# for i in range(0, len(dogsPathListLearning)):
#     image = cv2.imread(dogsPathListLearning[i])
#     gry = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     hist = desc.describe(gry)
#     labels.append("dog")
#     data.append(hist)
#
# # outfile.close()
#
# model = LinearSVC(C=100.0, random_state=42)
# model.fit(data, labels)
#
#
# ############### TESTING ##############
#
#
# for i in range(0,len(allPathListTesting)):
#     image = cv2.imread(allPathListTesting[i])
#     gry = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     hist = desc.describe(gry)
#     hist = hist.reshape(1,-1)
#     # feature = "-1 "
#     # for j in range(0,hist.size):
#     #     feature += str(j+1) + ":" + str(hist[j]) + " "
#     # outfile.write(feature +"\n")
#     prediction = model.predict(hist)[0]
#     # cv2.putText(image, prediction, (10, 30), cv2.FONT_HERSHEY_SIMPLEX,1.0, (0, 0, 255), 3)
#     # cv2.imshow("Image", image)
#     # cv2.waitKey(0)
#     print(allPathListTesting[i], ' ' , prediction)

