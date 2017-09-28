#ISC Code Challenge #1
#Written for meeting: Thursday, September 28th, 2017
#Written by Eric Fedrowisch, All rights reserved

##### Read if you want but leave this code alone ##########
from PIL import Image #Import PILLOW Image Library
from string import ascii_lowercase #Get lowercase letters

image = Image.open('Message_Image.png') #Create Image Object
width, height =  image.size #Get image size
coded_pixel = (0, 0, 1, 0) #This is the RGB value of a pixel marking a letter

letters = {} #Create a dictionary for looking up letters for a given x
xvals = {}   #Create a dictionary for looking up x vals based on a given letter
for x in range(0,25): #Populate the dictionaries
    letters[x] = ascii_lowercase[x]
    xvals[ascii_lowercase[x]] = x
letters[26] = ' '
xvals[' ']  = 26

#Given list of (x,y) integer pairs, return a string message
def decode(list_xy):
    message = ''
    for xy in list_xy:
        message = message + letters[xy[0]]
    return message

##### Your Code Goes Here =) ##########

#Hints:
#The text of the message will be stored in the pixels of the message image.
#Each line of pixels (or each y value) will store one character of the
#alphabet. Which leter it is will depend on the x value of the pixel.
#So a value of x=0 as the letter 'A', x=1 as 'B', etc (with x=26 as a space).
#You will have to loop through the y values and search the first 27 x positions
#of each line looking for pixels equal to the variable coded_pixel above.
#You can use image.getpixel(xy) to get the pixel at xy = (x,y). This will
#return the (Red,Green,Blue,Transparency) value of each pixel. The color of
#a pixel is determined by the mix of these color values.
#Once you have found a coded pixel you should store the (x,y) of it in a list.
#Once you have your list you can use the decode function provided to get back
#the message.
#Good luck and happy programming!
