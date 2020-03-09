import warnings
warnings.filterwarnings('ignore')

import numpy as np
from tkinter import messagebox
from skimage.transform import rescale, resize, downscale_local_mean
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.image import save_img

class preprocessing:
    def __init__(self,path):
        self.path = path
    

    def process_image(self):
        '''Will covert all the images to 300x400 pixels using random cropping and padding'''
        try:
            image = plt.imread(self.path)
        except:
            messagebox.showerror('Error!','Please select a image file')
            return None
        image = resize(image,(300,400,3))
        plt.imsave(self.path+'1.jpg',image)
        return self.path+'1.jpg'