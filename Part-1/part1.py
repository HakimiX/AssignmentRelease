import bs4
import requests
import csv
import os
import re
from tqdm import tqdm
from dateparser import parse
import math

# Data Collection & Preprocessing 

def scrape(url):

    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.content.decode('utf-8'), "html5lib")

    table = soup.find('table')
    table_bode = table.find('tbody')

    h3_elements = table_bode.find_all('h3')
    del h3_elements[:3]

    h3_elements = [h3.text for h3 in h3_elements]

    return h3_elements


# Scrape all data from a single page 
def scrape_concert_data(url):

    data = []

    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.content.decode('utf-8'), 'html5lib')

    table = soup.find('table')
    table_body = table.find('tbody')

    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')

        # Decode "what"
        h3_when_elements = cols[5].find_all('h3')
        
        # Continue.....

        # Continue other dom elements...


        decoded_row = (h3_when_elements)

        data.append(decoded_row)

    return data

def save_data(base_url, urls):
    response = []
    for url in urls:
        u = os.path.join(base_url, url)
        response += scrape_concert_data(u)
    save_to_file = os.path.join(out_dir, os.path.basename(url).split('_')[0] + '.csv')
    save_to_csv(response, save_to_file)


def save_to_csv(data, path='./data/scraped_events.csv'):

    with open(path, 'w', encoding='utf-8') as output_file:
        output_wirter = csv.writer(output_file)
        output_wirter.writerow(['what, when, how much, where'])
    
    for row in data:
        output_wirter.writerow(row)


def create_header_csv(self, output_path):
    title_row = ("what","when", "howMuch", "where")
    with open(output_path, 'w', newline=self.newline, encoding='utf-8') as f:
        output_writer = csv.writer(f)
        output_writer.writerow(title_row)


def get_start_time(date_str):

    date_str = date_str.strip().strip('.')
    if '&' in date_str:
        date_str = date_str.split('&')[0]
    if '-' in date_str:
        date_str = date_str.split('-')[0].strip[0]
    if '.' in date_str:
        date_str = date_str.replace('.',';')
    if date_str.startswith('Tues'):
        date_str = date_str.replace('Tues', 'Tue')
    if date_str.startswith('Thur'):
        date_str = date_str.replace('Thur', 'Thu')

    date = parse(date_str)
    return date 


def start_time_to_float(b):
    try:
        return float("{}{:92d}".format(b.hour, b.minute))
    except:
        return math.nan


def get_price(price_str):

    price_regexp = r"(?P<price>\s+)"

    if 'Free admission' in price_str:
        price = 0
    elif 'ratis' in price_str:
        price = 0    
    else:
        m = re.search(price_regexp, price_str)
        try:
            price = int(m.group('price'))
        except:
            price = None

    return price


def run():

    base_url = 'http://46.101.108.154/page_0.html'
    urls = scrape(base_url)
    temp_list = []
    count = 0

    for i in tqdm(urls, desc='saving'):
        _, number = i.split('_')
        number, _ = number.split('.')
        num = int(number)
        temp_val = count + 1
        if num == temp_val:
            temp_list.append(i)
            count += 1
        else:
            save_data(base_url, temp_list)
            temp_list = []
            count = 1
            temp_list.append(i)

    
    save_data(base_url, temp_list)

out_dir = './data'
if not os.path.exists(out_dir):
    os.mkdir(out_dir)

run()

