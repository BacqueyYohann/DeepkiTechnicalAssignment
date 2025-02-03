import os

from download import download_csv
from transform import transform_data
from search_closest import search_closest
from download_from_url import download_csv_from_url


# WKT Polygon that contains Cristo Redentor and a large part of Rio de Janeiro
your_own_wkt_polygon = ('POLYGON((-43.4172362480006 -22.719810214030947,-42.987396160109974 -22.719810214030947,-42.987396160109974 -23.038652469890703,-43.4172362480006 -23.038652469890703,-43.4172362480006 -22.719810214030947))')

# Cristo Redentor coordinates
cristo_lat = -22.95167
cristo_long = -43.21083

# URL to download the CSV from open-buildings containing Rio de Janeiro
url = 'https://storage.googleapis.com/open-buildings-data/v3/polygons_s2_level_4_gzip/009_buildings.csv.gz'


# CHOSE ONE DOWNLOAD ONLY, use URL or your own wkt polygon
download_csv(your_own_wkt_polygon)
""" download_csv_from_url(url) """

# cleaning the data 
transform_data()

# find closest building from cristo for every entry files (if necessary)
closest_to_cristo =[]
for filename in os.listdir('data/clean'):
    if filename == '.gitkeep':  # Skip .gitkeep file
        continue
    closest_to_cristo.append(search_closest(filename, cristo_lat, cristo_long))
