#!/usr/bin/env python3
import os, sys
import requests

url = "http://localhost/upload/"


def Uplodad_Image(imgfile_with_path):
    with open(imgfile_with_path, 'rb') as img_file:
        response = requests.post(url, files={'file': img_file})
        response.raise_for_status()
        print(imgfile_with_path)

def Uplodad_Image_all():
    img_file_dir = os.getcwd() + '/week4/supplier-data/images/'
    for files in os.listdir(img_file_dir):
        if files.endswith(".jpeg"):
            imgfile_with_path = os.path.join(img_file_dir, files)
            Uplodad_Image(imgfile_with_path)

def main():
    Uplodad_Image_all()

if __name__ == '__main__':
    main()