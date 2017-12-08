import pandas as pd
import numpy as np
import io_handler as io
import os
from osmread import parse_file, Node
from pandas import Series
from tqdm import tqdm


def add_geolocation(dataframe):

    coded_dataframe = dataframe
    
    coded_dataframe['lat'] = np.nan
    coded_dataframe['lon'] = np.nan

    io.initiate_dataframe_csv()

    dataframe.set_index("api_addresses", inplace=True)

    pbar = tqdm()
    for file in os.listdir("./data"):
        if not file.endswith('xml'): continue
        for idx, decoded_node in enumerate(decoded_node_to_csv(file)):
            try:
                full_address = decoded_node.tags['addr:street'] + " " + decoded_node.tags['addr:housenumber'] + " " + decoded_node.tags['addr:postcode'] + " " + decoded_node.tags['addr:city']
                addr_with_geo = (full_address, decoded_node.lon, decoded_node.lat)

                io.write_csv(addr_with_geo, "geodata/addr_with_geo.csv")

                pbar.update()

                geolocate_dataframe(dataframe, addr_with_geo)

            except (KeyError, ValueError):
                pass
        
        print('Finished with file: ' + file)

    io.write_dataframe_csv(dataframe, "geodata/geolocated_data.csv")



def geolocate_dataframe(dataframe, addr_with_geo):

    if dataframe.loc[addr_with_geo[0]] is not None:
        dataframe.set_value(addr_with_geo[0],'lon',addr_with_geo[1])
        dataframe.set_value(addr_with_geo[0],'lat',addr_with_geo[2])


def decoded_node_to_csv(filename):

    for entry in parse_file('./data/' + filename):

        if (isinstance(entry, Node) and
            'addr:street' in entry.tags and
            'addr:postcode' in entry.tags and
            'addr:housenumber' in entry.tags and
            'addr:city' in entry.tags):
        
            yield entry
    



