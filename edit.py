import numpy as np
import cv2
import os

directory1 = r'C:\Users\rites\OneDrive\Desktop\Image-Editor\static\images'
directory=r'C:\Users\rites\OneDrive\Desktop\Image-Editor'


def apply(path,edit_img,name="edited"):
   if path.count("jpg")>0 or path.count("jpeg")>0:
      os.chdir(directory1)
      cv2.imwrite(name+'.jpg',edit_img)
   elif path.count("png")>0:
      os.chdir(directory1)
      cv2.imwrite(name+'.png',edit_img)
   os.chdir(directory)

def brightness(path,value):
    image=cv2.imread(path)
    zero=np.zeros(image.shape,image.dtype)
    bright_img = cv2.addWeighted(image,1,zero,0,value)
    apply(path,bright_img)
   