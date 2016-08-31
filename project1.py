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
numberOfFiles = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])

def open_files(dir = ""):
    for value in range(1, numberOfFiles):
        key = "image{0}".format(value)
        dictionary[key] = Image.open(DIR + str(value) + ".png")
    return dictionary

def getMedianRGB(x,y):
    #Returns median for images at pixel x & y
    array = []
    mediun_position = 0
    for key, value in dictionary.items():
        rgb_im = dictionary[key].convert('RGB')
        red, green, blue = rgb_im.getpixel((x,y))
        array.append([red, green, blue])
        mediun_dictionary[key] = red + green + blue
    print (mediun_dictionary)
    d = OrderedDict(sorted(mediun_dictionary.items(), key=itemgetter(1)))
    #print(d)
    if numberOfFiles % 2 == 0:
        mediun_position = numberOfFiles / 2
    else:
        mediun_position = numberOfFiles - 1 / 2
    print(array)
    return array[int(mediun_position)]

open_files(DIR)
rgb = (getMedianRGB(dictionary["image1"].size[0] - 3, dictionary["image1"].size[1] - 1))
img = Image.new( 'RGB', (dictionary["image1"].size[0] - 1, dictionary["image1"].size[1] - 1), "White")
pixels = img.load()
#print (rgb[0], rgb[1], rgb[2])
pixels[0,1] = (rgb[0],rgb[1],rgb[2])
# for x in range(0, dictionary["image1"].size[0] - 1):
#     for y in range(0, dictionary["image1"].size[1] - 1):
#         rgb = getMedianRGB(x,y)
#         pixels[x,y] = (rgb[0], rgb[1], rgb[2])
#         print(str(x) + " " + str(y))
img.show()
#for key, value in dictionary.items():
#print (value.size[1])
#count = count + 1

    #alpha = value.split()[-1]
    #for xPixel in range(0, dictionary.image.size[0]):
    #    for yPixel in range(0,value.size[1]):
            #r,g,b = rgb_im.getpixel((xPixel, yPixel))
            #print (r,g,b)
#print(im.size[0])
