from PIL import Image
import os


class Tools:
    def __init__(self):
        self.imageWidth=480
        self.imageHeight=360


    def resizeImage(self,image, wid, hei):
        img = Image.open(image)
        imgResized = img.resize((wid, hei), Image.ANTIALIAS)
        imgResized.save(image)

    def getAllImagesResized(self,strSourcePath):
        for root, dirs, files in os.walk(os.path.abspath(strSourcePath)):
            for f in files:
                fullpath = os.path.join(root, f)
                if os.path.splitext(fullpath)[1] == '.jpg':
                    self.resizeImage(fullpath, self.imageWidth, self.imageHeight)

    def getImagePaths(self, strSourcePath):
        listPaths=[]
        for root, dirs, files in os.walk(os.path.abspath(strSourcePath)):
            for f in files:
                fullpath = os.path.join(root, f)
                if os.path.splitext(fullpath)[1].lower() == '.jpg':
                    listPaths.append(fullpath)
        return listPaths

    def getClassNames(self,strSourcePath):
        listClasses= (os.listdir(strSourcePath))
        return listClasses