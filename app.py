from cgitb import html
from email.mime import image
import imp
from click import edit
import cv2
import os

from numpy import imag

from edit import blur, brightness, contrast, sharp
from flask import Flask, redirect,flash, render_template, url_for, request, Response
from wtforms import Form
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = 'static/uploads/'

app = Flask(__name__, static_url_path='/static')
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


@app.route('/')
def home():
    return render_template('index.html')


edit_img = ''
edited=''
brightness_data='0'
contrast_data='1'
blur_data='0'

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        global brightness_data
        global contrast_data
        global blur_data
        global sharpness_data
        global edit_img
        global edited
        if request.form['upload'] == 'Upload' and request.form['path'] != '' and request.files['local_file'].filename == '':
            path = request.form['path']
            a = path.split('/')
            previous = os.getcwd()
            edit_img = previous+'/static/images/trash/'+a[len(a)-1]
            if os.path.isfile(previous+'/static/images/trash/'+a[len(a)-1]):
                return render_template('edit.html', image_filename='../static/images/trash/'+a[len(a)-1],brightness_data=brightness_data,contrast_data=contrast_data,blur_data=blur_data)
            folder = previous + '/static/images/trash/'
            os.chdir(folder)
            image_filename = wget.download(path)
            os.chdir(previous)
            return render_template('index.html', image_filename='../static/images/trash/'+image_filename,brightness_data=brightness_data,contrast_data=contrast_data,blur_data=blur_data)
        elif request.form['upload'] == 'Upload' and request.form['path'] == '' and request.files['local_file'].filename != '':
            f = request.files['local_file']
            previous = os.getcwd()
            edit_img = previous+'/static/images/trash/'+f.filename
            folder = previous + '/static/images/trash/'
            os.chdir(folder)
            f.save(secure_filename(f.filename))
            os.chdir(previous)
            return render_template('index.html', image_filename='../static/images/trash/'+f.filename,brightness_data=brightness_data,contrast_data=contrast_data,blur_data=blur_data)
        elif request.form['upload'] == 'submit' and edit_img!='':
            brightness_data = request.form['brightness']
            contrast_data = request.form['contrast']
            blur_data = request.form['blur']
            sharpness_data = request.form['sharpness']
            previous = os.getcwd()
            folder = previous + '/static/images/trash/'
            if edit_img.count('jpeg')>0 or edit_img.count("jpg")>0:
              edited=folder+'edited.jpg'
            elif edit_img.count('png')>0:
                edited=folder+'edited.png'
            os.chdir(folder)

            if brightness_data:
              brightness(edit_img,int(brightness_data))
            if contrast_data:
                contrast(edited, float(contrast_data))
            if blur_data:
                blur(edited,int(blur_data))
            if sharpness_data:
                sharp(edited,sharpness_data)
            os.chdir(previous)

            if edit_img.count('jpeg')>0 or edit_img.count("jpg")>0:
                return render_template('index.html',image_filename='../static/images/trash/edited.jpg',brightness_data=brightness_data,contrast_data=contrast_data,blur_data=blur_data)
            elif edit_img.count('png')>0:
                return render_template('index.html',image_filename='../static/images/trash/edited.jpg',brightness_data=brightness_data,contrast_data=contrast_data,blur_data=blur_data)
            else:
               flash("Oops Something went wrong !")
               return render_template('index.html',brightness_data=brightness_data,contrast_data=contrast_data,blur_data=blur_data)
        else:
            edit_img=''
            edited=''
            brightness_data='0'
            contrast_data='1' 
            flash("Oops Something went wrong !")     
            return render_template('index.html',brightness_data=brightness_data,contrast_data=contrast_data,blur_data=blur_data)
    return render_template('index.html', image_filename='../static/images/edited.jpg',brightness_data=brightness_data,contrast_data=contrast_data,blur_data=blur_data)


if __name__ == "__main__":
    app.run(debug=True)
