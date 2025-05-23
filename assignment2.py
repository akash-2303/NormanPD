import argparse
import pandas as pd
from pypdf import PdfReader
import os
import sqlite3
import io
import re
import sys
import pickle
import urllib.request
from geocode_weather import GeocodeWeather



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


def get_pdf_reader(url):


    headers = {
        'User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    }

    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as response:
        data = response.read()

    pdf_data = io.BytesIO(data)
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
    df['day_of_week'] = (df['incident_time'].dt.dayofweek + 1) % 7 + 1

    # df['day_of_week'] = df['incident_time'].dt.dayofweek + 1 #1 = sunday, 7 = saturday
    df['time_of_day'] = df['incident_time'].dt.hour

    # df = df.iloc[:100]
    geo_weather_obj = GeocodeWeather()
    #incident_location to latitude and longitude
    df['latitude'], df['longitude'] = zip(*df['incident_location'].apply(geo_weather_obj.get_lat_lon))

    #side of town 
    df['side_of_town'] = df.apply(lambda row: get_side_of_town(row['latitude'], row['longitude']), axis=1)

    #weather information
    df['weather_code'] = df.apply(lambda row: geo_weather_obj.get_weather(row['latitude'], row['longitude'], row['incident_time']), axis=1)
    geo_weather_obj.save_cache()

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
    # df['EMSSTAT'] = df.apply(lambda row: check_emsstat(df, row.name), axis=1)
    check_emsstat(df)

    return df



#Saving csv and sql
def save_csv(df, csv_file):
    df.to_csv(csv_file, index=False)

def save_sql(df, conn):
    df.to_sql('incidents', conn, if_exists='replace', index=False)



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

#EMSSTAT
def check_emsstat(df, ori_colunm = 'incident_ori', time_column = 'incident_time', location_column = 'incident_location'):

    emsstat_dict = {}
    for index, row in df.iterrows():
        key = (row['incident_time'], row['incident_location'])
        if key not in emsstat_dict:
            emsstat_dict[key] = []
        emsstat_dict[key].append((index, row['incident_ori'] == 'EMSSTAT'))

    df['EMSSTAT'] = False
    for key, incidents in emsstat_dict.items():
        if any(ori for idx, ori in incidents if ori):
            for idx, _ in incidents:
                df.at[idx, 'EMSSTAT'] = True


def load_final_df_cache(cache_file):
    cache_file_path = os.path.join("resources", cache_file)
    if os.path.exists(cache_file_path):
        with open(cache_file_path, 'rb') as f:
            return pickle.load(f)
    return None

def save_final_df_cache(df, cache_file):
    cache_file_path = os.path.join("resources", cache_file)
    os.makedirs(os.path.dirname(cache_file_path), exist_ok=True)  # Create the directory if it doesn't exist
    with open(cache_file_path, 'wb') as f:
        pickle.dump(df, f)



def main():
    parser = argparse.ArgumentParser(description='Process PDF for incident data.')
    parser.add_argument('--urls', type=str, help='')

    args = parser.parse_args()
    file_path = args.urls

    urls = pd.read_csv(file_path, header=None)
    lst_urls = urls[0].tolist()

    lst_df = []
    for url in lst_urls:
        
        pdf_file_data = get_pdf_reader(url)
        list_lines = lines_from_pages(pdf_file_data)
        df = dataframe_from_lines(list_lines)
        lst_df.append(df)
    
    final_df = pd.concat(lst_df, axis = 0)

    final_df.to_csv('output.csv', index=False)
    # Ensure all required columns are included
    output_columns = ['day_of_week', 'time_of_day', 'weather_code', 'location_rank', 'side_of_town', 'incident_rank', 'nature', 'EMSSTAT']
    final_df = final_df[output_columns]
    
    for row in final_df.itertuples(index=False):
        sys.stdout.write("\t".join(map(str, row)) + "\n")
    
if __name__ == '__main__':

    main()
