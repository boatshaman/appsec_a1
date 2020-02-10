#!/usr/bin/env python3
"""
Joseph Hensersky
Program for cropping image into a square
"""
import sys
from PIL import Image

findCenter = lambda x, y: int((x-y)/2) # for finding location to paste image in created square

def crop_image(img):
    fill_color = (0, 0, 0, 0) # black background
    width, height = img.width, img.height
    size = max(width, height)
    squareImg = Image.new('RGBA', (size, size), fill_color)
    squareImg.paste(img, (findCenter(size, width), findCenter(size, height))) # pastes image in center of square
    return squareImg

def main(image):
    i = Image.open(image)
    newImage = crop_image(i)
    newImage.save("square_%s" % i.filename , i.format)

if __name__ == "__main__":
    try:
        image_name = sys.argv[1]
    except:
        print("Usage: ./image_resize.py image_name")
        sys.exit(1)

    main(image_name)
