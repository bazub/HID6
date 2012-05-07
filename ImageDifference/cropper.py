'''
Created on Apr 20, 2012

@author: Bogdan
'''
#from PIL import Image
from ImageChops import *
import glob, os
import ImageDraw
image1=Image.open("F:\\a.bmp")
image2=image1.crop((220,50,460,340))

image2.save("F:\\current.bmp")