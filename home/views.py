from django.shortcuts import render
from PIL import Image,ImageEnhance,ImageChops
import requests
import random as rn
from io import BytesIO
import os
from Spaceapps.settings import TEMPLATE_DIR as dry
# Create your views here.
def index(request):
        global d
        d = "https://gibs.earthdata.nasa.gov/wmts/epsg4326/best/MODIS_Terra_CorrectedReflectance_TrueColor/default/2012-07-09/250m/6/"+str(rn.randint(1,39))+"/"+str(rn.randint(1,79))+".jpg"
        manipulate()
        #enhance()
        print(dry+"/filters/")
        return render(request,"app.html", {'img':d})

def manipulate():
    response = requests.get(d)
    img = Image.open(BytesIO(response.content))
    size = img.size
    for y in range(1,5):
        img2=Image.open(os.path.join(dry,"filters","filter({}).jpg".format(y)))
        img2=img2.resize(size, Image.ANTIALIAS)
        img3=ImageChops.blend(img,img2,alpha=(4/10))
        img3=ImageChops.darker(img,img2)
        img3.save(os.path.join(dry,"outputs","Artified_img-{}.jpg".format(y)))

 
def enhance():    
    response = requests.get(d)
    img = Image.open(BytesIO(response.content))
    enhancer = ImageEnhance.Color(img)
    factor=1.5
    img=enhancer.enhance(factor)
    enhancer = ImageEnhance.Contrast(img)
    factor=1.5
    img=enhancer.enhance(factor)
    enhancer = ImageEnhance.Sharpness(img)
    factor=2
    img=enhancer.enhance(factor)
    img.save("/outputs/Enhanced_Image.jpg")