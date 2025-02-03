import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
from geopy.distance import geodesic
from tqdm import tqdm

CLEAN_DIR = 'data/clean'

def load_data(filename):

    filepath = f"{CLEAN_DIR}/{filename}"
    df = pd.read_csv(filepath)
    return df

# find the closest point to the given reference lat and long
def find_closest_point(df, ref_lat, ref_lon):

    gdf = gpd.GeoDataFrame(df, geometry=gpd.GeoSeries.from_xy(df['longitude'], df['latitude']))

    ref_point = Point(ref_lon, ref_lat)

    # computing distance from every entry to the ref_point, monitored by tqdm
    distances = []
    for point in tqdm(gdf.geometry, desc="Calculating distances", unit="points"):
        distance = geodesic((ref_lat, ref_lon), (point.y, point.x)).meters
        distances.append(distance)
    
    # adding the new column distance
    gdf['distance'] = distances

    # finding the closest point with min distance
    closest_index = gdf['distance'].idxmin()
    closest_point = gdf.iloc[closest_index]

    return closest_point

def search_closest(filename, ref_lat, ref_lon):

    print(f"Loading data from {filename}...")
    df = load_data(filename)

    print(f"Searching for the closest point to ({ref_lat}, {ref_lon})...")
    closest_point = find_closest_point(df, ref_lat, ref_lon)

    print(f"Closest point found:\n{closest_point}")
    return closest_point
