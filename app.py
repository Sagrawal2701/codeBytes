from cgitb import html
from email.mime import image
import imp
from click import edit
import cv2
import os
import wget

from numpy import imag

from edit import brightness
from flask import Flask, redirect, render_template, url_for, request,Response
from wtforms import Form
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = 'static/uploads/'

app = Flask(__name__,static_url_path='/static')
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

@app.route('/')
def home():
  return render_template('index.html')

edit_img=''
@app.route('/',methods = ["GET","POST"])
def index():
  if request.method == "POST":
    global brightness_data
    global contrast_data
    global blur_data
    global sharpness_data
    global edit_img
    if request.form['upload']=='Upload' and request.form['path']!='' and  request.files['local_file'].filename=='':
           path = request.form['path']
           a = path.split('/')
           previous = os.getcwd()
           edit_img=previous+'/static/images/trash/'+a[len(a)-1]
           if os.path.isfile(previous+'/static/images/trash/'+a[len(a)-1]):
              return render_template('edit.html',image_filename='../static/images/trash/'+a[len(a)-1])
           folder = previous +'/static/images/trash/'
           os.chdir(folder)
           image_filename = wget.download(path)
           os.chdir(previous)
           return render_template('index.html',image_filename='../static/images/trash/'+image_filename)  
    elif request.form['upload']=='Upload' and request.form['path']=='' and  request.files['local_file'].filename!='':
            f = request.files['local_file']
            previous = os.getcwd()
            edit_img=previous+'/static/images/trash/'+f.filename
            folder = previous +'/static/images/trash/'
            os.chdir(folder)
            f.save(secure_filename(f.filename))
            os.chdir(previous)
            return render_template('index.html',image_filename='../static/images/trash/'+f.filename)       
    elif request.form['upload']=='submit':
      brightness_data = request.form['brightness']
      contrast_data = request.form['contrast']
      blur_data = request.form['blur']
      sharpness_data = request.form['sharpness']
      if brightness_data:
        brightness(edit_img,int(brightness_data))
        


  return render_template('index.html',image_filename='../static/images/edited.jpg')
  
if __name__ == "__main__":
  app.run(debug=True)



