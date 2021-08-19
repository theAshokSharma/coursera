#!/usr/bin/env python3

import os
import datetime
import reports
import emails

current_date = datetime.datetime.now().strftime('%b %d, %Y')

desc_location = 'supplier-data/descriptions/'
pdf_file = '/tmp/processed.pdf'

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
    for desc in os.listdir(desc_location):
        data_list = extract_data_list(os.path.join(desc_location, desc))
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


if __name__ == '__main__':
    extract_data_and_report()

    sender = 'automation@example.com'
    receiver = 'student-00-7e6ad623c74c@example.com'
    subject = 'Upload Completed - Online Fruit Store'
    body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'
    
    message = emails.generate_email(sender,receiver, subject, body, pdf_file)
    emails.send_email(message)