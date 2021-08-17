#!/usr/bin/env python3
import os
import datetime
import reports

current_date = datetime.datetime.now().strftime('%b %d, %Y')

description_dir = os.getcwd() + '/week4/supplier-data/descriptions/'
pdf_file = '/Users/ashar11/Downloads/processed.pdf'


def extract_data_list(filename):
    data_list = []
    with open(filename) as file:
        rec = file.readlines()
        name = rec[0].strip()
        weight = rec[1].strip()
        data_list.append(name)
        data_list.append(weight)
    return data_list

def extract_data_and_report():
    fruit_list = []
    for desc in os.listdir(description_dir):
        data_list = extract_data_list(os.path.join(description_dir, desc))
        fruit_list.append(data_list)

    # Sort the list       
    fruit_list.sort(key=lambda a: a[0], reverse=False)    

    # build data for generating PDF doc
    description = ""
    for list in fruit_list:
        name = "name: " + list[0]
        weight = "weight: " + list[1]
        description += name + "<br/>" + weight + "<br/><br/>"
    title = "Processed Update on " + current_date 
    
    reports.generate_report(pdf_file,title, description)    


def main():
    print("Extracting description from")
    extract_data_and_report()
    print("Done.....")

if __name__ == '__main__':
    main()