from PIL import Image

import random
import sys

image = Image.open("/content/Snapchat-1856147453.jpg")
color_image = image.convert('CMYK')
bw_image = image.convert('1')

outfile1 = Image.new("CMYK", [dimension for dimension in image.size])

outfile2 = Image.new("CMYK", [dimension for dimension in image.size])

outfile3 = Image.new("CMYK", [dimension for dimension in image.size])

for x in range(0, image.size[0], 2):
    for y in range(0, image.size[1], 2):
        sourcepixel = image.getpixel((x, y))

        outfile1.putpixel((x, y),(sourcepixel[0],0,0,0))

        outfile2.putpixel((x, y),(0,sourcepixel[1],0,0))

        outfile3.putpixel((x, y),(0,0,sourcepixel[2],0))

"""decomposing images into 3 CMY images"""

outfile1.save('outfile1.jpg')
outfile2.save('outfile2.jpg')
outfile3.save('outfile3.jpg')

image1 = Image.open("outfile1.jpg")
image2 = Image.open("outfile2.jpg")
image3 = Image.open("outfile3.jpg")

image1 = image1.convert('1')
image2 = image2.convert('1')
image3 = image3.convert('1')

ht1 = Image.new("CMYK", [dimension for dimension in image1.size])
ht2 = Image.new("CMYK", [dimension for dimension in image1.size])
ht3 = Image.new("CMYK", [dimension for dimension in image1.size])

for x in range(0, image1.size[0]):
    for y in range(0, image1.size[1]):
        pixcol1 = image1.getpixel((x, y))
        pixcol2 = image2.getpixel((x, y))
        pixcol3 = image3.getpixel((x, y))
        if pixcol1 == 255:
            ht1.putpixel((x, y),(255,0,0,0))
        else:
            ht1.putpixel((x, y),(0,0,0,0))

        if pixcol2 == 255:
            ht2.putpixel((x, y),(0,255,0,0))
        else:
            ht2.putpixel((x, y),(0,0,0,0))

        if pixcol3 == 255:
            ht3.putpixel((x, y),(0,0,255,0))
        else:
            ht3.putpixel((x, y),(0,0,0,0))

"""Conversion of CMY images into respective halftones"""

ht1.save('ht1.jpg')
ht2.save('ht2.jpg')
ht3.save('ht3.jpg')

image1 = Image.open("ht1.jpg")
image1 = image1.convert('CMYK')

image2 = Image.open("ht2.jpg")
image2 = image2.convert('CMYK')

image3 = Image.open("ht3.jpg")
image3 = image3.convert('CMYK')

new1 = Image.new("CMYK", [dimension * 2 for dimension in image1.size])

new2 = Image.new("CMYK", [dimension * 2 for dimension in image2.size])

new3 = Image.new("CMYK", [dimension * 2 for dimension in image3.size])
for x in range(0, image1.size[0]):
    for y in range(0, image1.size[1]):
        pixcol= image1.getpixel((x, y))

        if pixcol[0]+pixcol[1]+pixcol[2] == 0:
            new1.putpixel((x * 2, y * 2), (255,0,0,0))
            new1.putpixel((x * 2 + 1, y * 2), (0,0,0,0))
            new1.putpixel((x * 2, y * 2 + 1), (0,0,0,0))
            new1.putpixel((x * 2 + 1, y * 2 + 1), (255,0,0,0))

        else:
            new1.putpixel((x * 2, y * 2), (0,0,0,0))
            new1.putpixel((x * 2 + 1, y * 2), (255,0,0,0))
            new1.putpixel((x * 2, y * 2 + 1), (255,0,0,0))
            new1.putpixel((x * 2 + 1, y * 2 + 1), (0,0,0,0))

        pixcol = image2.getpixel((x, y))

        if pixcol[0]+pixcol[1]+pixcol[2] == 0:
            new2.putpixel((x * 2, y * 2), (0,255,0,0))
            new2.putpixel((x * 2 + 1, y * 2), (0,0,0,0))
            new2.putpixel((x * 2, y * 2 + 1), (0,0,0,0))
            new2.putpixel((x * 2 + 1, y * 2 + 1), (0,255,0,0))

        else:
            new2.putpixel((x * 2, y * 2), (0,0,0,0))
            new2.putpixel((x * 2 + 1, y * 2), (0,255,0,0))
            new2.putpixel((x * 2, y * 2 + 1), (0,255,0,0))
            new2.putpixel((x * 2 + 1, y * 2 + 1), (0,0,0,0))

        pixcol = image3.getpixel((x, y))

        if pixcol[0]+pixcol[1]+pixcol[2] == 0:
            new3.putpixel((x * 2, y * 2), (0,0,255,0))
            new3.putpixel((x * 2 + 1, y * 2), (0,0,0,0))
            new3.putpixel((x * 2, y * 2 + 1), (0,0,0,0))
            new3.putpixel((x * 2 + 1, y * 2 + 1), (0,0,255,0))

        else:
            new3.putpixel((x * 2, y * 2), (0,0,0,0))
            new3.putpixel((x * 2 + 1, y * 2), (0,0,255,0))
            new3.putpixel((x * 2, y * 2 + 1), (0,0,255,0))
            new3.putpixel((x * 2 + 1, y * 2 + 1), (0,0,0,0))

""" Converting the halftones images into respective shares so that after overlapping it should form the actual image"""

new1.save('new1.jpg')
new2.save('new2.jpg')
new3.save('new3.jpg')

infile1 = Image.open("new1.jpg")
infile2 = Image.open("new2.jpg")
infile3 = Image.open("new3.jpg")

outfile = Image.new('CMYK', infile1.size)

for x in range(0,infile1.size[0],2):
    for y in range(0,infile1.size[1],2):

        C = infile1.getpixel((x+1, y))[0]
        M = infile2.getpixel((x+1, y))[1]
        Y = infile3.getpixel((x+1, y))[2]


        outfile.putpixel((x, y), (C,M,Y,0))
        outfile.putpixel((x+1, y), (C,M,Y,0))
        outfile.putpixel((x, y+1), (C,M,Y,0))
        outfile.putpixel((x+1, y+1), (C,M,Y,0))

"""Shows the final images after merging the  3 new images"""

outfile.save("final_img.jpg")