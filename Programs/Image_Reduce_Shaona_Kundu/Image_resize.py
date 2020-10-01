import PIL

from PIL import Image

mywidth = 3024
myheight = 4032

img = Image.open('Programs/Image_Reduce_Shaona_Kundu/aesthetic.jpg') 
img = img.resize((mywidth, myheight), PIL.Image.ANTIALIAS)
img.save('resize.jpg')