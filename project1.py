#
# * Title: project1.java
# * Abstract: This takes in images from local directory, removes the subject in the pictures by using a median filter
# * Author: Tomas Hernandez
# Date:9/9/2016
#!/usr/bin/env python3
import os, os.path
import operator
from PIL import Image, ImageFilter
import sys

DIR = "/Users/tomas/Desktop/Code/Python/Project 1/images/"
#Get the number of files within the directory
numberOfFiles = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
dictionary = {}
mediun_dictionary = {}
rgb  = [0,0,0]

#Initializes images and stores them in a dictionary
def open_files(dir):
    for value in range(1, numberOfFiles):
        key = "image{0}".format(value)
        dictionary[key] = Image.open(DIR + str(value) + ".png")
    return dictionary

#Returns array of the median pixel values for images at pixel x & y
def getMedianRGB(x,y):
    array = []
    returnArray = []
    #Converts images to RGB to get pixel data then add to array for later use
    for key, value in dictionary.items():
        rgb_im = dictionary[key].convert('RGB')
        red, green, blue = rgb_im.getpixel((x,y))
        array.append([red, green, blue])
        mediun_dictionary[key] = red + green + blue

    sorted_dict = sorted(mediun_dictionary.items(), key=operator.itemgetter(1))
    for x in range(0, numberOfFiles - 1):
        if(sorted_dict[int(numberOfFiles / 2) - 1][1] == (array[x][0] + array[x][1] + array[x][2])):
           returnArray = (array[x])
    return returnArray

#Main
open_files(DIR)
img = Image.new( 'RGB', (dictionary["image1"].size[0] - 1, dictionary["image1"].size[1] - 1), "Black")
pixels = img.load()
xSize = int((dictionary["image1"].size[0] - 1))
ySize = int((dictionary["image1"].size[1] - 1))
#Loops through all pixels by using X and Y
for x in range(0, xSize):
    for y in range(0, ySize):
       rgb = (getMedianRGB(x,y))
       pixels[x,y] = (rgb[0], rgb[1], rgb[2])
       print(str(x) + " " + str(y))
img.save("result.jpg", 'jpeg')
img.show()
