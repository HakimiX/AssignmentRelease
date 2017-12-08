from mpl_toolkits.basemap import Basemap
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pylab as P
import numpy as np
import folium
import math
from tqdm import tqdm 
import collections
import pandas as pd


# Visualisation 

# Plot locations on a map


def generate_basemap(dataframe):

    fig = plt.figure(figsize=(8, 8))
    m = Basemap(projection='lcc', resolution=None,
            width=5000000, height=5000000, 
            lat_0=55, lon_0=10,)
    
    # Continue.....


def haversine_to_location(multi, dataframe):

    if multi is 1:
        return dataframe.apply(lambda row: multi_haversine(row), axis=1)
    else:
        return dataframe.apply(lambda row: calc_haversine(row), axis=1)


def plot_haversine_from_venue(dataframe):

    return dataframe.assign(km_to_venue=haversine_to_location(1, dataframe))


def multi_haversine(row):
    nørreport_venue = [(55.68352, 12.57206)]
    results = []

    for venue in nørreport_venue:
        results.append(calc_haversine(row,venue))
    return min(results)

def calc_haversine(row, venue=''):

    if venue is not '':
        lat_orig, lon_orig = venue
    else:
        lat_orig, lon_orig = (55.68352, 12.57206)
    lat_dest = row['lat']
    lon_dest = row['lon']

    radius = 6371

    dlat = math.radians(lat_dest-lat_orig)
    dlon = math.radians(lon_dest-lon_orig)
    a = (math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(math.radians(lat_orig)) 
        * math.cos(math.radians(lat_dest)) * math.sin(dlon / 2) * math.sin(dlon / 2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = radius * c

    return d


def read_csv_to_dataframe(csv_path, dtype=''):
    
    dateparse = lambda x: pd.datetime.strptime(x, '%d-%m-%Y')
    
    if (dtype is ''):
        df = pd.read_csv(csv_path)
    else:
        df = pd.read_csv(csv_path, dtype=dtype, date_parser=dateparse)

    return df


def scatter_plot_from_dataframe(dataframe):
    plot = dataframe.plot(kind='scatter', x='lon', y='lat')
    plot.get_figure().savefig('scatterplot1.png')


def generate_scatter_plot(datetime_dataframe):
    scatter_plot_from_dataframe(datetime_dataframe)    


def run():

    print ('Scraped Dataframe')
    scraped_dataframe = pd.read_csv('./data/scraped_events.csv')
    generate_scatter_plot(scraped_dataframe)


run()