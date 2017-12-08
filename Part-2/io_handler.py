import pandas as pd
import os
import csv
import platform
import numpy as np


def create_csv_with_header(output_path):

    title_row = ("what", "when", "Howmuch", "where", "longitude", "latitude")
    with open(output_path, 'w', newline=define_newline(), encoding='utf-8') as f:
        output_writer = csv.writer(f)
        output_writer.writerow(title_row)


def initiate_dataframe_csv():

    if not os.path.exists("geodata"):
        os.makedirs("geodata")
    
    if not os.path.exists("geodata/geolocated_data.csv"):
        create_csv_with_header('geodata/geolocated_data.csv')


def write_csv(string, output_path):

    with open(output_path, 'a', newline=define_newline(), encoding='utf-8') as f:
        output_writer = csv.writer(f)
        output_writer.writerow(string)

def write_dataframe_csv(dataframe,output_path):
    
    dataframe.to_csv(output_path,sep=',', encoding='utf-8')

def define_newline():
    # Checks the operating system in order to determine newline rules.
    if platform.system() == 'Windows':
        return ''
    else:
        return None