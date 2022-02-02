import cv2
import os

from edit import brightness
from flask import Flask, render_template, url_for, request
from wtforms import Form


UPLOAD_FOLDER = 'static/uploads/'

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


@app.route('/',methods = ["GET","POST"])
def index():
  if request.method == "POST":
    global brightness_data
    global contrast_data
    global blur_data
    global sharpness_data
    if request.form['submit']=='submit':
      brightness_data = request.form['brightness']
      contrast_data = request.form['contrast']
      blur_data = request.form['blur']
      sharpness_data = request.form['sharpness']
      if brightness_data:
        brightness('viking.jpg',int(brightness_data))

   
  return render_template('index.html')
  
if __name__ == "__main__":
  app.run(debug=True)



