#!/usr/bin/env python3

import os
import requests
import locale
import re

desc_location = 'supplier-data/descriptions/'
data_col = ['name', 'weight', 'description']
url = 'http://localhost/fruits/'

def extract_description_from_file(filename):
    with open(filename) as file:
        rec = file.readlines()
        data_dict = {}
        for k, data in zip(data_col, rec):
            data = data.strip('\n')
            data_dict.update({k:data})

        item_weight = data_dict["weight"]
        item_weight = locale.atoi(re.sub(r"lbs$","", item_weight))
        data_dict["weight"] = item_weight
        data_dict["image_name"] = os.path.splitext(os.path.basename(filename))[0] + ".jpeg"
    return data_dict

def extract_description_and_post():
    for desc in os.listdir(desc_location):
        data = extract_description_from_file(os.path.join(desc_location, desc))
        print (data)
        response = requests.post(url, json=data)
        response.raise_for_status()

def main():
    print("Extracting description...")
    extract_description_and_post()
    print("Done.....")

if __name__ == '__main__':
    main()