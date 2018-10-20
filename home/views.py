from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"app.html")

def manipulate():
    img=Image.open("demoimg.jpg")
    size = img.size
    for y in range(1,5):
        img2=Image.open("filters/filter ({}).jpg".format(y))
        img2=img2.resize(size, Image.ANTIALIAS)
        img3=ImageChops.blend(img,img2,alpha=(4/10))
        img3=ImageChops.darker()
        img3.save("outputs/img_blend_{}.jpg".format(y))