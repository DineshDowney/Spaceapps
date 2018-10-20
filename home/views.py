from django.shortcuts import render
from PIL import Image,ImageEnhance,ImageChops
import requests
from io import BytesIO
# Create your views here.
def index(request):
    return render(request,"app.html")

def manipulate(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    size = img.size
    for y in range(1,5):
        img2=Image.open("filters/filter ({}).jpg".format(y))
        img2=img2.resize(size, Image.ANTIALIAS)
        img3=ImageChops.blend(img,img2,alpha=(4/10))
        img3=ImageChops.darker()
        img3.save("outputs/Artified_img-{}.jpg".format(y))
 
def enhance():    
    response = requests.get(url)
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
    img.save("outputs/Enhanced_Image.jpg")