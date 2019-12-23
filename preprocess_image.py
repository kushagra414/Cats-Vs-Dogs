import warnings
warnings.filterwarnings('ignore')

import numpy as np
from tkinter import messagebox
import skimage as ski
#from matplotlib.pyplot import imread
#from tensorflow.keras.preprocessing.image import save_img

class preprocessing:
    def __init__(self,path):
        self.path = path
    

    def process_image(self):
        '''Will covert all the images to 300x400 pixels using random cropping and padding'''
        try:
            image = ski.io.imread(self.path)
        except:
            messagebox.showerror('Error!','Please select a image file')
            return None
        # Padding the image to 300x400 if image has less than 300 dims
        # Cropping image if image has greater than 300 dims
        # Final Size of the image will be 300x400 after preprocessing.
        # Better to perform resizing for avoiding random cropping and padding of targeted areas of image
        image = resize(image)
        x,y = image.shape[0],image.shape[1]
        if x<=300 and y<=400:
            image = padding400(image)
        elif x>=300 and y>=400:
            image = cropping400(image)
        elif x<=300 and y>=400:
            image = padding400(image)
            image = cropping400(image)
        elif x>=300 and y<=400:
            image = padding400(image)
            image = cropping400(image)
        ski.io.imsave(self.path+'1.jpg',image)
        return self.path+'1.jpg'







def padding400(image):
    x,y = image.shape[0],image.shape[1]
    if x<= 300 and y<= 400:
        pad_image = np.zeros((300,400,3),dtype=np.float64)
    elif x<=300 and y>=400:
        pad_image = np.zeros((300,y,3),dtype=np.float64)
    elif x>=300 and y<=400:
        pad_image = np.zeros((x,400,3),dtype=np.float64)
    pad_image[0:x,0:y,:] = image
    return pad_image



def cropping400(image):
    x,y = image.shape[0],image.shape[1]
    if x>300 and y>400:
        x_random = np.random.randint(0,x-300,dtype=np.int32)
        y_random = np.random.randint(0,y-400,dtype=np.int32)
    elif x==300 and y>400:
        x_random =0
        y_random = np.random.randint(0,y-400,dtype=np.int32)
    elif x>300 and y==400:
        x_random = np.random.randint(0,x-300,dtype=np.int32)
        y_random =0
    crop_img = np.zeros((300,400,3),dtype=np.float64)
    crop_img[:,:,:] = image[x_random:x_random+300,y_random:y_random+400]
    return crop_img


def resize(image):
    x = image.shape[0]
    y = image.shape[1]
    fac_h=x
    fac_w=y
    if x>=600:
        fac_h = x//2.7
    elif x<=150:
        fac_h = x*2
    else:
        fac_h = x
    if y>=800:
        fac_w = y//2.7
    elif y<=200:
        fac_w = y*2
    else:
        fac_w = y
    if(fac_h !=x or fac_w !=y):
        return ski.transform.resize(image,(fac_h,fac_w),anti_aliasing=False)
    else:
        return image