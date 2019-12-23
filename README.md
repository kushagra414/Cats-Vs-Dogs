# Cats VS Dog Classifier with Tkinter GUI



## Pre-requisites:

- Python3
- pandas
- numpy
- NVIDIA® GPU card with CUDA® Compute Capability 3.5
- NVIDIA® GPU drivers —CUDA 10.0 requires 410.x or higher.
- CUDA® Toolkit —TensorFlow supports CUDA 10.0 (TensorFlow >= 1.13.0)
- CUPTI ships with the CUDA Toolkit.
- cuDNN SDK (>= 7.4.1)
- Tensorflow

__You can visit [Tensorflow website](https://www.tensorflow.org/install/gpu), for installation guide for above requisites.__

## About Dataset

- __The train folder contains images of cat and dogs.The train folder contains 25,000 images of dogs and cats.There are no duplicate images.__
- __The test folder contains 12500 images of cats and dogs.__
- __Each image has been preprocessed to 200x300 pixels.__
- __test Dataset in unlabelled.__<br>
__URL for dataset : https://www.kaggle.com/c/dogs-vs-cats/data__

## About Model

- I have used Convolutional Neural Network to classify images.
- Here is the architecture of the model.
- ![CNN Architecture](https://github.com/kushagra414/Cats-Vs-Dogs/blob/master/screenshots/CNN_model._Architecture.PNG)
- The model has loss: 0.0679, acc: 0.9750,  validation loss: 0.3017 - validation acc: 0.9016
- After Training I saved the model so that I could use it without training the model again and again
- Refer to Cat Vs Dog.ipynb to checkout all the details and code.

## Cats VS Dogs GUI

- I developed the GUI using Python inbuilt module Tkinter.

![Starting Gui](https://github.com/kushagra414/Cats-Vs-Dogs/blob/master/screenshots/1Starting_Window.PNG)
GUI

- There are 4 buttons on the window
  - Browse files - This button can be used if you want to select multiple images.

  - Browse directory - This button can be used if you want to test accuracy of the algorithm on multiple images. You must select a directory using this button.
  
  - Predict - This Button is used after selecting multiple image files(This is used with Browse Files, See same color of the button represents they are used together).
  
  - Predict Accuracy - This button is used after selecting the directory of images(This is used after Browse directory).The directory names should be cats and dogs as shown in screenshot.

![Browse files](https://github.com/kushagra414/Cats-Vs-Dogs/blob/master/screenshots/2Browse_files.PNG)
Browse files Button Action
![Predict](https://github.com/kushagra414/Cats-Vs-Dogs/blob/master/screenshots/3Predict.PNG)
Predict Button Action
![Browse Directory](https://github.com/kushagra414/Cats-Vs-Dogs/blob/master/screenshots/4Browse_Directory.PNG)
Browse Directory Button Action
![Predict Accuracy](https://github.com/kushagra414/Cats-Vs-Dogs/blob/master/screenshots/5Predict_Accuracy.PNG)
Predict Accuracy Button Actio 

## Preprocess Images

- To show real-time results to used I implemented preprocessing of images so that the algorithm is able to work on all image sizes.
- Every image is reshaped to 300x400 using cropping, padding and resizing.
- The algorithm will work on any image size but due to random cropping/padding the actual image of cat or dog might get cropped.
- The application will work best on 300x400 images, so I suggest strongly to resize the image to 300x400 pixels.
