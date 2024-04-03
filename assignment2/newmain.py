import argparse
import pandas as pd
from pypdf import PdfReader
import os
import sqlite3
import io
import re
import sys
import pickle

import requests
from geopy.geocoders import Nominatim

#Getting db connection
def get_db_connection(db_path='normanpd.db'):
    curr_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
    if os.path.exists(os.path.join(curr_dir, 'resources', db_path)):
        os.remove(os.path.join(curr_dir, 'resources', db_path))
    if not os.path.exists(os.path.join(curr_dir, 'resources')):
        os.mkdir(os.path.join(curr_dir, 'resources'))
    conn = sqlite3.connect(os.path.join(curr_dir, 'resources', db_path))
    return conn

#Extracting lines from pdf
def lines_from_pages(pdf_reader):
    list_lines = []
    for page in pdf_reader.pages:
        splitted_line = page.extract_text(extraction_mode="layout", layout_mode_space_vertically=False).split('\n')
        for line in splitted_line:
            field_split = re.split(r'\s{2,}', line)
            list_lines.append(field_split)
    list_lines = list_lines[3:-1]
    return list_lines

#Read PDF from file path (Temporarily working with single file)
file_path = "C:/Users/Akash Balaji/Downloads/DATA ENGINEERING/cis6930sp24-assignment2/2024-02-01_daily_incident_summary.pdf"
def get_pdf_reader(file_path):
    pdf_data = open(file_path, "rb")
    pdf_reader = PdfReader(pdf_data)
    return pdf_reader

#Dataframe from extracted lines
def dataframe_from_lines(list_lines):
    df = pd.DataFrame(list_lines)
    expected_columns = ['incident_time', 'incident_number', 'incident_location', 'nature', 'incident_ori']
    while len(df.columns) < len(expected_columns):
        df[len(df.columns)] = None

    df = df.iloc[:, :len(expected_columns)]
    df.columns = expected_columns
    df = df[df['incident_time'].notna()]
    df = df[df['incident_time'] != '']

    #incident_time to datetime to extract day of the week and time of day
    df['incident_time'] = pd.to_datetime(df['incident_time'])
    df['day_of_week'] = df['incident_time'].dt.dayofweek + 1 #1 = sunday, 7 = saturday
    df['time_of_day'] = df['incident_time'].dt.hour

    #incident_location to latitude and longitude
    df['latitude'], df['longitude'] = zip(*df['incident_location'].apply(get_lat_lon))

    #side of town 
    df['side_of_town'] = df.apply(lambda row: get_side_of_town(row['latitude'], row['longitude']), axis=1)

    #weather information
    df['weather_code'] = df.apply(lambda row: get_weather(row['latitude'], row['longitude'], row['incident_time']), axis=1)

    # Counting frequency of each nature for incident_rank
    nature_counts = df['nature'].value_counts().reset_index()
    nature_counts.columns = ['nature', 'nature_count']
    df = df.merge(nature_counts, on='nature', how='left')

    # Fill NaN values in nature_count with 0 (or another appropriate value) before ranking
    df['nature_count'] = df['nature_count'].fillna(0)

    df['incident_rank'] = df['nature_count'].rank(method='min', ascending=False).astype(int)

    #Counting frequency of location rank
    location_counts = df['incident_location'].value_counts().reset_index()
    location_counts.columns = ['incident_location', 'location_count']
    df = df.merge(location_counts, on='incident_location', how='left')
    df['location_rank'] = df['location_count'].rank(method = 'min', ascending=False).astype(int)

    #Checking for EMSSTAT
    df['EMSSTAT'] = df.apply(lambda row: check_emsstat(df, row.name), axis=1)

    return df



#Saving csv and sql
def save_csv(df, csv_file):
    df.to_csv(csv_file, index=False)

def save_sql(df, conn):
    df.to_sql('incidents', conn, if_exists='replace', index=False)

#Caching weather data
def load_cache(cache_file):
    if os.path.exists(cache_file):
        with open(cache_file, 'rb') as f:
            return pickle.load(f)
    return {}

def save_cache(cache, cache_file):
    with open(cache_file, 'wb') as f:
        pickle.dump(cache, f)

geocode_cache = load_cache('geocode_cache.pkl')
weather_cache = load_cache('weather_cache.pkl')


#Location latitude and longitudes and side of town

def get_lat_lon(incident_location):
    if incident_location in geocode_cache:
        return geocode_cache[incident_location]
    
    geolocator = Nominatim(user_agent="assignment2", timeout=10)
    location = geolocator.geocode(incident_location + ', Norman, OK')
    if location:
        result = (location.latitude, location.longitude)
    else:
        result = (None, None)
    geocode_cache[incident_location] = result
    return result    


def get_side_of_town(latitude, longitude):
    if latitude is not None and longitude is not None:
        norman_center = (35.220833, -97.443611)
        lat_diff = latitude - norman_center[0]
        lon_diff = longitude - norman_center[1]

        if lat_diff > 0 and lon_diff > 0:
            return 'NE'
        elif lat_diff > 0 and lon_diff < 0:
            return 'NW'
        elif lat_diff < 0 and lon_diff > 0:
            return 'SE'
        elif lat_diff < 0 and lon_diff < 0:
            return 'SW'
        elif lat_diff > 0:
            return 'N'
        elif lat_diff < 0:
            return 'S'
        elif lon_diff > 0:
            return 'E'
        else:
            return 'W'
    else:
        return 'Unknown'


#weather data
def get_weather(latitude, longitude, datetime):
    if latitude is None or longitude is None:
        return None
    key = (latitude, longitude, datetime.strftime('%Y-%m-%d'))
    if key in weather_cache:
        return weather_cache[key]

    date_str = datetime.strftime('%Y-%m-%d')
    time_str = datetime.strftime('%H')

    params = {
        'latitude': latitude,
        'longitude': longitude,
        'start': date_str,
        'end': date_str,
        'hourly': 'weather_code'
    }
    try:
        response = requests.get('https://archive-api.open-meteo.com/v1/archive', params=params)
        if response.status_code == 200:
            data = response.json()
            weather_code = data['hourly']['weather_code'][int(time_str)]
            # return weather_code
        else:
            # return None
            weather_code = None
    except requests.exceptions.RequestException as e:
        weather_code = None

    weather_cache[key] = weather_code
    return weather_code
   
save_cache(geocode_cache, 'geocode_cache.pkl')
save_cache(weather_cache, 'weather_cache.pkl')
    
    #     print("Data received:", data)  # Debugging line
    #     try:
    #         weather_code = data['hourly']['weather_code'][int(time_str)]
    #         return weather_code
    #     except KeyError as e:
    #         print("KeyError:", e)
    #         print("Data structure might be different than expected.")
    #         return None
    # else:
    #     return None
    
#EMSSTAT
def check_emsstat(df, index, ori_colunm = 'incident_ori', time_column = 'incident_time', location_column = 'incident_location'):
    # current_time = df.loc[index, time_column]
    # current_location = df.loc[index, location_column]

    # check_indices = list(range(max(index - 2, 0), min(index + 3, len(df))))

    # for i in check_indices:
    #     if i != index:
    #         if df.loc[i, time_column] == current_time and df.loc[i, location_column] == current_location:
    #             if df.loc[i, ori_colunm] == 'EMSSTAT':
    #                 return True
                
    # return False
    emsstat_dict = {}
    for index, row in df.iterrows():
        key = (row['incident_time'], row['incident_location'])
        if key not in emsstat_dict:
            emsstat_dict[key] = row['incident_ori'] == 'EMSSTAT'
        elif not emsstat_dict[key]:
            emsstat_dict[key] = row['incident_ori'] == 'EMSSTAT'

    df['EMSSTAT'] = df.apply(lambda row: emsstat_dict[(row['incident_time'], row['incident_location'])], axis=1)


def main():
    parser = argparse.ArgumentParser(description='Process PDF for incident data.')
    parser.add_argument('--csv', type=str, help='Path to save the CSV file')
    parser.add_argument('--db', type=str, help='Path to the SQLite database file')
    args = parser.parse_args()

    # Hardcoded PDF path
    file_path = "C:/Users/Akash Balaji/Downloads/DATA ENGINEERING/cis6930sp24-assignment2/2024-02-01_daily_incident_summary.pdf"
    pdf_reader = get_pdf_reader(file_path)
    list_lines = lines_from_pages(pdf_reader)
    df = dataframe_from_lines(list_lines)

    if args.csv:
        save_csv(df, args.csv)

    if args.db:
        conn = get_db_connection(args.db)
        save_sql(df, conn)
        conn.close()

    # Ensure all required columns are included
    output_columns = ['day_of_week', 'time_of_day', 'weather_code', 'location_rank', 'side_of_town', 'incident_rank', 'nature', 'EMSSTAT']
    final_df = df[output_columns]
    
    # Output the DataFrame to stdout with the header
    final_df.to_csv(sys.stdout, index=False, header=True, sep='\t')


if __name__ == '__main__':
    main()
