#!/usr/bin/env python3

from PIL import Image
import os

src_location = '/week4/supplier-data/images/'   # '/media/images/'
dest_location = '/week4/supplier-data/images/'  # '/media/images/'

def ChangeImage(srcfile, dest):

    base = os.path.basename(srcfile)
    imgfile = os.path.splitext(base)[0]
    destfile = dest + imgfile + '.jpeg'
    print("{}\n{}". format(srcfile, destfile))

    try:
        with Image.open(srcfile) as img:
            img = img.resize((600,400))
            img = img.convert('RGB')
            img.save(destfile, "jpeg")
            img.close()
    except IOError as e:
            print(e)

def ChangeImgage_all():
    print (os.getcwd())
    srcfile = os.getcwd() + src_location
    dest = os.getcwd() + dest_location

    for files in os.listdir(srcfile):
        imgfile_with_path = os.path.join(srcfile, files)
        if imgfile_with_path.endswith(".tiff"):
            ChangeImage(imgfile_with_path, dest)

if __name__ == '__main__':
    ChangeImgage_all()