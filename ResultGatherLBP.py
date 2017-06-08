import sys
import subprocess
import os
import time

now = time.time()

# kValueList = [ 10,20,50,75,100,150,200 ]
classCount = [ 2,3,4,5,10 ]
numOfPointsRadiusList = [[8,3],[16,3],[16,4],[32,4],[32,5],[64,5],[64,6]]
dataSetEqualSize = True


train_path = "Resources/MajorProjectResources/LearningSet"
testingSetPath = "Resources/MajorProjectResources/TestingSet"

training_names = os.listdir(train_path)
# print(training_names)
# for training_name in training_names:
#     dir = os.path.join(train_path, training_name)
#     class_path = list(paths.list_images(dir))
#     image_paths += [class_path[i] for i in range(0,90)]
#     image_classes += [training_name] * 90
#     class_id += 1
# print(training_names)

for item in classCount:
    i = 0
    while i+item <= len(training_names):
        testClasses = []
        testClasses+= [training_names[k] for k in range(i,i+item)]
        i+=item

        # print(' '.join(testClasses))

        for numOfPoints,radius in numOfPointsRadiusList:
            for x in range(2):
                # print(r'python preFinalLBPRecognizer.py '+ str(numOfPoints) + ' '+ str(radius) + ' ' + str(dataSetEqualSize)  + ' ' + ' '.join(testClasses) + '>> outputLBP.txt')

                processTrain=subprocess.check_output(r'python preFinalLBPRecognizer.py '+ str(numOfPoints) + ' '+ str(radius) + ' ' + str(dataSetEqualSize)  + ' ' + ' '.join(testClasses) + '>> outputLBP.txt',shell=True)
                dataSetEqualSize = (not dataSetEqualSize)

        if(i==item*2):
            break

