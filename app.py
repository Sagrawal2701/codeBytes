from flask import Flask, render_template ,request,flash,Response, send_file
from werkzeug.utils import secure_filename
import cv2
import os
import calendar
import time
import getpass
import platform
from effects import color_pop, cool, alchemy,wacko,unstable,ore,contour,snicko,indus,spectra,molecule,lynn
from edit import brightness,contrast,blur,resize,denoise,rotate,sharp
from filter import hind,flora,handlebar,bella,tilak,thug,lido,polychrome,visor,rcb,mi,nags
from nightMode import night

app = Flask(__name__)
app.config['SECRET_KEY']='codeBytes'
port = int(os.environ.get("PORT",5000))


@app.after_request
def add_header(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

###################################################################################################home page
@app.route('/')
def home():
	return render_template('edit.html')


#################################################################################about page

@app.route('/about')
def about():
	return render_template('about.html')



############################################################################################edit page
file_type=''
edit_img=''
edited=''
brightness_value='0'
contrast_value='1'
sharp_value=''
resize_value=''
rotate_value=''
denoise_value=''
blur_value='1'
effected=''
filter_val='None'

@app.route('/edit',methods=['GET','POST'])
def edit():
    if request.method=='POST':
       global edit_img
       global effected
       global edited
       global brightness_value
       global contrast_value
       global sharp_value
       global resize_value
       global rotate_value
       global denoise_value
       global blur_value
       global filter_val
       global file_type
   
       if request.form['button']=='Upload'  and  request.files['local_file'].filename!='':
            f = request.files['local_file']
            previous = os.getcwd()
            eff_img=previous+'/static/images/trash/'+f.filename
            edit_img=previous+'/static/images/trash/'+f.filename
            com_img=previous+'/static/images/trash/'+f.filename
            folder = previous +'/static/images/trash/'
            os.chdir(folder)
            f.save(secure_filename(f.filename))
            os.chdir(previous)
            return render_template('edit.html',image_filename='../static/images/trash/'+f.filename,brightness_value=brightness_value,contrast_value=contrast_value,blur_value=blur_value,sharp_value=sharp_value,denoise_value=denoise_value,rotate_value=rotate_value,resize_value=resize_value,filter_val=filter_val)
     
       elif request.form['button']=='Apply' and edit_img!='':
            brightness_value = request.form['brightness']
            contrast_value = request.form['Contrast']
            sharp_value = request.form['type']
            resize_value = request.form['type2']
            rotate_value = request.form['type1']
            denoise_value = request.form['type3']
            blur_value = request.form['Blur']
            filter_val=request.form['filters']
            previous = os.getcwd()
            folder = previous +'/static/images/trash/'
            if edit_img.count('jpeg')>0 or edit_img.count("jpg")>0:
                file_type='jpg'
                edited=folder+'edited.jpg'
            elif edit_img.count('png')>0:
                 file_type='png'
                 edited=folder+'edited.png'
            os.chdir(folder)
            if brightness_value:
               brightness(edit_img,int(brightness_value))
            if contrast_value:
               contrast(edited,float(contrast_value))
            if sharp_value!='none':
               sharp(edited,sharp_value)
            if resize_value!='none':
               resize(edited,resize_value)
            if rotate_value!='none': 
               rotate(edited,rotate_value)
            if denoise_value!='none':
               denoise(edited,denoise_value)
            if blur_value:
               blur(edited,int(blur_value))
            if filter_val!='':
               if filter_val=='Oreo':
                   color_pop(edited)
               elif filter_val=='Alchemy':
                   alchemy(edited)          
               elif filter_val=='Contour':
                   contour(edited)
               elif filter_val=='Indus':
                   indus(edited)
               elif filter_val=='Molecule':
                   molecule(edited)
               elif filter_val=='Mercury':
                   cool(edited)
               elif filter_val=='Wacko':
                   wacko(edited)
               elif filter_val=='Ore':
                   ore(edited)
               elif filter_val=='Snicko':
                   snicko(edited)                               
            os.chdir(previous)           
 
            if edit_img.count('jpeg')>0 or edit_img.count("jpg")>0:
                return render_template('edit.html',image_filename='../static/images/trash/edited.jpg',brightness_value=brightness_value,contrast_value=contrast_value,blur_value=blur_value,sharp_value=sharp_value,denoise_value=denoise_value,rotate_value=rotate_value,resize_value=resize_value,filter_val=filter_val)
            elif edit_img.count('png')>0:
                return render_template('edit.html',image_filename='../static/images/trash/edited.png',brightness_value=brightness_value,contrast_value=contrast_value,blur_value=blur_value,sharp_value=sharp_value,denoise_value=denoise_value,rotate_value=rotate_value,resize_value=resize_value,filter_val=filter_val)
            else:
               flash("Oops Something went wrong !")
               return render_template('edit.html',brightness_value=brightness_value,contrast_value=contrast_value,blur_value=blur_value,sharp_value=sharp_value,denoise_value=denoise_value,rotate_value=rotate_value,resize_value=resize_value,filter_val=filter_val)
    
       else:
            effected=''
            edit_img=''
            edited=''
            brightness_value='0'
            contrast_value='1'
            sharp_value=''
            resize_value=''
            rotate_value=''
            denoise_value=''
            blur_value='1'
            file_type=''
            flash("Oops Something went wrong !")
            return render_template('edit.html',brightness_value=brightness_value,contrast_value=contrast_value,blur_value=blur_value,sharp_value=sharp_value,denoise_value=denoise_value,rotate_value=rotate_value,resize_value=resize_value,filter_val=filter_val)

    return render_template('edit.html',brightness_value=brightness_value,contrast_value=contrast_value,blur_value=blur_value,sharp_value=sharp_value,denoise_value=denoise_value,rotate_value=rotate_value,resize_value=resize_value,filter_val=filter_val)

############################################################################################filters page
cap =''
value=0
filter_img=''
flag=False
def stream():
    global cap
    cap=cv2.VideoCapture(0)
    while True:
        _,frame = cap.read()
        imgencode=cv2.imencode('.jpg',frame)[1]
        strinData = imgencode.tostring()
        yield (b'--frame\r\n'b'Content-Type: text/plain\r\n\r\n'+strinData+b'\r\n')

def stop():
    global cap
    if cap.isOpened():
        cap.release()

   

@app.route('/filters/video')
def video():
     if value==0:     
         return Response(stream(),mimetype='multipart/x-mixed-replace;boundary=frame')
     elif value==1:
         print("Entered Hind video")
         return Response(hind(cap),mimetype='multipart/x-mixed-replace;boundary=frame')
     elif value==2:
         return Response(handlebar(cap),mimetype='multipart/x-mixed-replace;boundary=frame')
     elif value==3:
         return Response(flora(cap),mimetype='multipart/x-mixed-replace;boundary=frame')
     elif value==4:
         return Response(bella(cap),mimetype='multipart/x-mixed-replace;boundary=frame')
     elif value==5:
         return Response(tilak(cap),mimetype='multipart/x-mixed-replace;boundary=frame')
     elif value==6:
         return Response(thug(cap),mimetype='multipart/x-mixed-replace;boundary=frame')
     elif value==7:
         return Response(lido(cap),mimetype='multipart/x-mixed-replace;boundary=frame')
     elif value==8:
         return Response(polychrome(cap),mimetype='multipart/x-mixed-replace;boundary=frame')
     elif value==9:
         return Response(visor(cap),mimetype='multipart/x-mixed-replace;boundary=frame')
     elif value==10:
         return Response(mi(cap),mimetype='multipart/x-mixed-replace;boundary=frame')
     elif value==11:
         return Response(rcb(cap),mimetype='multipart/x-mixed-replace;boundary=frame')
     elif value==12:
         return Response(nags(cap),mimetype='multipart/x-mixed-replace;boundary=frame')
     elif value==13:
         return Response(stop(),mimetype='multipart/x-mixed-replace;boundary=frame')

@app.route('/filters',methods=['GET','POST'])
def filters():
     global value
     global filter_img
     global flag
     if request.method=='POST':
        print("Entered")
        if request.form['button']=='Hind':
               print("Entered Hind")
               value=1       
        elif request.form['button']=='Handlebar':
               value=2
        elif request.form['button']=='Flora':
               value=3
        elif request.form['button']=='Bella':
               value=4
        elif request.form['button']=='Tilak':
               value=5
        elif request.form['button']=='Thug':
               value=6
        elif request.form['button']=='Lido':
               value=7
        elif request.form['button']=='Polychrome':
               value=8
        elif request.form['button']=='Visor':
               value=9
        elif request.form['button']=='MI':
               value=10
        elif request.form['button']=='RCB':
               value=11
        elif request.form['button']=='Nags':
               value=12
        elif request.form['button']=='Clear':
               value=0
        elif request.form['button']=='Capture':
               value=13
               flag=True
               filter_img='../static/images/trash/filter.jpg'
               return render_template('filters.html',img_filename='../static/images/trash/filter.jpg')
        else:
              value=0
     return render_template('filters.html',img_filename=None)

@app.route('/download')
def download_file():
    if(file_type=='png'):
     path='static/images/trash/edited.png'
    else:
     path='static/images/trash/edited.jpg'    
    return send_file(path,as_attachment=True)
@app.route('/download1')
def download_file1():
    path='static/images/trash/filter.jpg'
    return send_file(path,as_attachment=True)


night_img=''
file_type=''
@app.route('/nightmode',methods=['GET','POST'])
def nightmode():
    if request.method == 'POST':
        global night_img
        global file_type
        if request.form['button']=='Upload' and request.files['local_file'].filename!='':
            f = request.files['local_file']
            previous = os.getcwd()
            night_img=previous+'/static/images/trash/'+f.filename
            folder = previous +'/static/images/trash/'
            os.chdir(folder)
            f.save(secure_filename(f.filename))
            os.chdir(previous)
            return render_template('nightmode.html',image_filename='../static/images/trash/'+f.filename) 
             
        elif request.form['button']=='night' and night_img!='':
            previous=os.getcwd()
            folder=previous+'/static/images/trash/'
            os.chdir(folder)
            night(night_img)
            os.chdir(previous)
            if night_img.count('jpeg')>0 or night_img.count("jpg")>0:
                file_type='jpg'
                night_img=folder+'nightmode.jpg'
                return render_template('nightmode.html',image_filename='../static/images/trash/nightimage.jpg') 
            elif night_img.count('png')>0:
                file_type='png'
                night_img=folder+'nightmode.png'
                return render_template('nightmode.html',image_filename='../static/images/trash/nightimage.png')  
            else:
                return render_template('nightmode.html')            
    return render_template('nightmode.html')

@app.route('/download2')
def download_file2():
    if(file_type=='png'):
     path='static/images/trash/nightimage.png'
    else:
     path='static/images/trash/nightimage.jpg'    
    return send_file(path,as_attachment=True)

###############################################################################################main function
if __name__ == '__main__':
	app.run(host='0.0.0.0',port=port)
