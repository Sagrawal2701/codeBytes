
import numpy as np
import cv2
import os

# directory1 = r'C:\Users\rites\OneDrive\Desktop\Image-Editor\static\images\trash'
# directory=r'C:\Users\rites\OneDrive\Desktop\Image-Editor'


def apply(path,edit_img,name="edited"):
   if path.count("jpg")>0 or path.count("jpeg")>0:
      #os.chdir(directory1)
      cv2.imwrite(name+'.jpg',edit_img)
   elif path.count("png")>0:
     # os.chdir(directory1)
      cv2.imwrite(name+'.png',edit_img)
   #os.chdir(directory)

def brightness(path,value):
    image=cv2.imread(path)
    zero=np.zeros(image.shape,image.dtype)
    bright_img = cv2.addWeighted(image,1,zero,0,value)
    # cv2.imshow("test",bright_img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    apply(path,bright_img)
   
def contrast(path,value):
    image=cv2.imread(path)
    zero=np.zeros(image.shape,image.dtype)
    con = cv2.addWeighted(image,value,zero,0,0)
    # cv2.imshow("test",con)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows() 
    apply(path,con)


def sharp(path,value):
    image=cv2.imread(path)
    kernel = np.array([[0,-1,0], 
                       [-1,5,-1],                     #min
                       [0,-1,0]])
    kernel1 =np.array([[-1,-1,-1], 
                [-1, 9,-1],                           #max
                [-1,-1,-1]])
    if value=='max':
        sharpened = cv2.filter2D(image, -1, kernel1)
    else:
        sharpened = cv2.filter2D(image, -1, kernel)
    apply(path,sharpened)
    

def blur(path,value):
    image = cv2.imread(path) 
    blur = cv2.blur(image,(value,value)) 
    apply(path,blur)