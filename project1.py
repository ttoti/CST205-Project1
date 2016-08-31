#!/usr/bin/env python3
import os, os.path
from collections import OrderedDict
from operator import itemgetter
from PIL import Image, ImageFilter
import sys

DIR = "/Users/tomas/Desktop/Code/Python/Project 1/images/"
dictionary = {}
mediun_dictionary = {}
d = {}
rgb  = [0,0,0]
numberOfFiles = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])

def open_files(dir = ""):
    for value in range(1, numberOfFiles):
        key = "image{0}".format(value)
        dictionary[key] = Image.open(DIR + str(value) + ".png")
    return dictionary

def getMedianRGB(x,y):
    #Returns median for images at pixel x & y
    array = []
    returnArray = []
    for key, value in dictionary.items():
        rgb_im = dictionary[key].convert('RGB')
        red, green, blue = rgb_im.getpixel((x,y))
        array.append([red, green, blue])
        mediun_dictionary[key] = red + green + blue

    for key, value in mediun_dictionary.items():
        for number in array:
            if value == (number[0] + number[1] + number[2]):
                returnArray = number
                print(number)
    return returnArray

open_files(DIR)
rgb = (getMedianRGB(dictionary["image1"].size[0] - 3, dictionary["image1"].size[1] - 1))
print (rgb)
img = Image.new( 'RGB', (dictionary["image1"].size[0] - 1, dictionary["image1"].size[1] - 1), "White")
pixels = img.load()
xSize = int((dictionary["image1"].size[0] - 1))
ySize = int((dictionary["image1"].size[1] - 1))
#for x in range(int(xSize/1.1), xSize):
    # for y in range(int(ySize/1.1), ySize):
    #    rgb = (getMedianRGB(x,y))
    #    pixels[x,y] = (rgb[0], rgb[1], rgb[2])
    #    print(str(x) + " " + str(y))
img.show()
