import sys
import subprocess
import os
import time

# kValueList = [ 10,20,50,75,100,150,200 ]
kValueList = [ 10,20]
classCount = [ 2,3,4,5,10,20]
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
print(training_names)

for item in classCount:

    i = 0
    while i+item <= len(training_names):
        testClasses = []
        testClasses+= [training_names[k] for k in range(i,i+item)]
        i=i+item
        # print(' '.join(testClasses))

        for kVal in kValueList:
            for x in range(2):
                processTrain=subprocess.check_output(r'python preFinalTraining.py '+ str(kVal) + ' '+ str(dataSetEqualSize)  + ' ' + ' '.join(testClasses) + '>> output.txt',shell=True)
                processTest=subprocess.check_output(r'python preFinalTesting.py '+ ' '.join(testClasses) + '>> output.txt',shell=True)
                dataSetEqualSize = (not dataSetEqualSize)




