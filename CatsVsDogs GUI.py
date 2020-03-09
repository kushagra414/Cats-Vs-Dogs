#!/usr/bin/env python
# coding: utf-8

# In[1]:


import warnings
warnings.filterwarnings('ignore')
from tkinter import filedialog
from tkinter import *
import os


# In[2]:


win = Tk()
win.title("Is is a cat or a dog?")
win.geometry("400x200")


# ## Labels

# In[3]:


path_label = Label(win)
path_label.pack()


# ## Entry box

# In[4]:


entry_path_var = StringVar()
enter_path = Entry(win,width=30,textvariable=entry_path_var)
enter_path.pack()
enter_path.focus()


# ## Buttons

# ### Predict Button

# In[5]:


def submit():
    import preprocess_image as pi
    import numpy as np
    
    paths = entry_path_var.get()
    paths = paths.split(',')
    new_path = []
    for path in paths:
        # Preprocessing Image
        process_img = pi.preprocessing(path)
        process_img = process_img.process_image()
        if process_img == None:
            enter_path.delete(0,END)
            return None
        else:
            new_path.append(process_img)
        ## End
    
    from matplotlib.pyplot import imread
    from tensorflow.keras import models
    from tkinter import messagebox
    import os
    
    model = models.load_model('CatsVsDogs_model_saved/CatVsDogs.h5')
    
    no_of_images = len(new_path)
    x = np.zeros((no_of_images,300,400,3))
    
    for count, path in enumerate(new_path):
        image = imread(path)
        x[count,:,:,:] = image
    predict = model.predict(x/255.0)
    for count, path in enumerate(new_path):
        app = Window(win)
        app.image(path)
        predicted_cat = predict[count][0]*100
        predicted_dog = predict[count][1]*100
        Label(win,text='Probability of being a cat = '+str(predicted_cat)+
                  '\nProbability of being a dog ='+str(predicted_dog)).pack()
        win.geometry("1000x500")
        os.remove(path)
    enter_path.delete(0,END)


# In[6]:


button_path = Button(win,text='Predict',bg = '#3cba54',fg='black',command=submit)
button_path.pack()


# ### Browse Button

# In[7]:


def browse_files():
    tk_filenames = filedialog.askopenfilenames(title='Please select one or more files')
    paths = ''
    for count, filename in enumerate(tk_filenames):
        if count ==0:
            paths += filename
        else:
            paths += ',' + filename
    entry_path_var.set(paths)


# In[8]:


button_browse = Button(win,text='Browse files',bg = '#3cba54',fg='black',command=browse_files)
button_browse.pack()


# ## Predict Accuracy Button

# In[9]:


def predict_acc():
    from tkinter import messagebox
    
    dir_path = entry_path_var.get()
    if dir_path =='':
        messagebox.showerror('Error','Please select a path for directory')
        enter_path.delete(0,END)
        return None
    
    import preprocess_image as pi
    import numpy as np
    from tensorflow.keras.preprocessing.image import ImageDataGenerator as IDG
    from tensorflow.keras import models
    
    model = models.load_model('CatsVsDogs_model_saved/CatVsDogs.h5')
    
    generator = IDG(rescale=1/255.0)
    acc_generator = generator.flow_from_directory(dir_path,(300,400),class_mode='binary')
    try:
        accuracy = model.evaluate_generator(acc_generator)
    except:
        messagebox.showerror("Error",'Directory does not contains any sub-directories of classes')
        enter_path.delete(0,END)
        return None
    messagebox.showinfo('Accuracy','Accuracy on the data set is : '+str(accuracy[1]*100))
    enter_path.delete(0,END)


# In[10]:


pred_acc_button = Button(win,text='Predict Accuracy',bg = '#f4c20d',fg='black',command=predict_acc)
pred_acc_button.pack()


# ## Predict Accuracy Browse Button

# In[11]:


def browse_dir():
    tk_dir_path = filedialog.askdirectory(title='Please open directory which contains sub-directories for cats and dogs labels')
    entry_path_var.set(tk_dir_path)


# In[12]:


button_browse = Button(win,text='Browse directory',bg = '#f4c20d',fg='black',command=browse_dir)
button_browse.pack()


# ## Load and Label Images

# In[13]:


## Copied from https://pythonbasics.org/tkinter-image/
from PIL import Image, ImageTk
from tkinter import Frame
from tkinter import BOTH

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        
    def image(self,path):
        load = Image.open(path)
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)


# ## Window

# In[14]:


win.mainloop()

