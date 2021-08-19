#!/usr/bin/env python3

import shutil
import psutil
import socket
import emails
import os

def alert_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free < 20

def alert_cpu_usage():
	usage = psutil.cpu_percent(1)
	return usage > 80

def alert_memory_available():
    mem = psutil.virtual_memory()
    threshold = 500 * 1024 * 1024
    return mem.available < threshold

def alert_localhost():
    localhost = socket.gethostbyname('localhost')
    return localhost != '127.0.0.1'

def send_email_alert(error):
    print (error)
    sender = 'automation@example.com'
    receiver = 'student-00-7e6ad623c74c@example.com'
    subject = error
    body = "Please check your system and resolve the issue as soon as possible."
    message = emails.generate_email(sender, receiver, subject, body, "")
    emails.send_email(message)

if alert_cpu_usage():
    subject = "Error - CPU usage is over 80%"
    send_email_alert(subject)

if  alert_disk_usage('/'):
    subject = "Error - Available disk space is less than 20%"
    send_email_alert(subject)

if  alert_memory_available():
    subject = "Error - Available memory is less than 500MB"
    send_email_alert(subject)

if  alert_localhost():
    subject = "Error - localhost cannot be resolved to 127.0.0.1"
    send_email_alert(subject)