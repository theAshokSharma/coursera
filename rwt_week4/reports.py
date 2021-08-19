#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(filename, title, description):

    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(filename)
    report_title = Paragraph(title, styles["h1"])
    report_body = Paragraph(description,styles["BodyText"])
    blank_line = Spacer(1,20)
    
    report.build([report_title, blank_line, report_body, blank_line])
