# Identification of Properties of Architectures using machine learning techniques

The goal of this project is to classify the architectures by their styles.  

The architecture styles that are used on testing for this project is as follows:
 * American Craftsman  
 * Ancient Egyptian
 * Art Deco
 * Art Nouveau
 * Baroque
 * Beaux Art
 * Byzantine
 * Chicago School
 * Colonial
 * Deconstructivism
 * Georgian
 * Gothic
 * Greek Revival
 * International
 * Novelty
 * Palladian
 * Postmodern
 * Queen Anne
 * Russian Revival
 * Tudor Revival 

## Getting Started

These instructions will guide you to run this project on your local machine for development and testing purposes. 


### Prerequisites

What libraries you need to run the project on your machine 

```
Python 3.5
numpy
Scikit-image
Scikit-learn
opencv-python
opencv-contrib-python


```

### Installing

After copyying all repo to your local machine, and adding related libraries as I mentioned above, you could directly run the project on your machine.


## Descriptions for Directories

### Resources

Under Resources directory, MajorProjectResources contain both learning set with each class containing more than 90 images and testing set with equal to 20 images.

### Source Codes

In this part, only the files that are used in test are mentioned. The rest of the files shared in this project are implemented during studying process.

#### preFinalTraining.py

It's major code that is used for training SVM with feature extracted using SIFT algorithm. It takes 3 parameters
 * k ==> K-value used in clustering 
 * dataSet ==> Data is taken from each class equally or not
 * Architecture styles 
 An example is to execute it;
 
```
python preFinalTraining.py 10 True Deconstructivism AmericanCraftsman
```


#### preFinalTesting.py

It's major code that is used for testing the results with feature extracted using SIFT algorithm. It takes only 1 parameters
 * Architecture styles 
 
 An example is to execute it;

```
python preFinalTesting.py Deconstructivism AmericanCraftsman
```

### preFinalLBPRecognize.py

It's major code that is used for training SVM and testing the results with feature extracted using LBP algorithm. It takes 4 parameters
 * n ==> number of points
 * r ==> radius
 * dataSet ==> Data is taken from each class equally or not
 * Architecture styles 
 
  An example is to execute it;

```
python preFinalLBPRecognizer.py 8 3 True Deconstructivism AmericanCraftsman
```


## Authors

* Mehmet Doğan  

* Sinem Dalkılıç



## Acknowledgments

* Xu Z., Tao D., Zhang Y., Wu J., Tsoi A.C. (2014) Architectural Style Classification Using Multinomial Latent Logistic Regression. In: Fleet D., Pajdla T., Schiele B., Tuytelaars T. (eds) Computer Vision – ECCV 2014. ECCV 2014. Lecture Notes in Computer Science, vol 8689. Springer, Cham

