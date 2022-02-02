import numpy as np
import cv2

def apply(path,edit_img,name="edited"):
   if path.count("jpg")>0 or path.count("jpeg")>0:
      cv2.imwrite(name+'.jpg',edit_img)
   elif path.count("png")>0:
      cv2.imwrite(name+'.png',edit_img)


def brightness(path,value):
    image=cv2.imread(path)
    zero=np.zeros(image.shape,image.dtype)
    bright_img = cv2.addWeighted(image,1,zero,0,value)
    apply(path,bright_img)
    cv2.imshow("img1",image)
    cv2.imshow("img2",bright_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
   