from PIL import Image
from ImageChops import *
import glob, os
import sys

def main():
    size = 240,290
    black=(0,0,0)
    red=(255,0,0)
    
    image1=Image.open("F:\\current.bmp")
    #image1.thumbnail(size, Image.ANTIALIAS)
    ok=0
    c=1
    minim=255*3*240*290
    for infile in glob.glob("F:\\*.bmp"):
        file, ext = os.path.splitext(infile)
        if file!="F:\\current":
            im = Image.open(infile)
            #im.thumbnail(size, Image.ANTIALIAS)
            image2=difference(image1,im)
            pix=image2.load()
            sum=0
            for i in range(0,239):
                for j in range(0,289):
                    sum=sum+pix[i,j][0]+pix[i,j][1]+pix[i,j][2]
            if sum< 240*290*60:
                if sum<minim:
                    minim=sum
                    care=c
                    ok=1
                    pa=file[3:]
                #print file[3:], sum
                
        c=c+1   
    if ok==0:
        print ("You were not found in the DB")
        return 0
    else:
        print ("Hello "+pa+"! You are now loged in.")
        return care
        
        
    
    
'''
image2=Image.open("F:\\test2.bmp")

image5=difference(image1,image2)

w=image5.size[0]
h=image5.size[1]
pix=image5.load()


for i in range(0,w):
    for j in range(0,h):
        if pix[i,j]!=black:
            pix[i,j]=red

image5.save("F:\\test4.bmp")
'''
if __name__ == "__main__":
    sys.exit(main())