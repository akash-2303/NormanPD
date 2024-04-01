import io
import urllib.request
from pypdf import PdfReader  # Make sure you have an actual library that supports PdfReader
import re
import pandas as pd
import os
import sqlite3  # Ensure you use this for database operations
import argparse
import sys  

from geopy.geocoders import Nominatim

# Assuming normanpd.py sets up a database connection, we'll create and manage it within main.py for clarity
def get_db_connection(db_path='normanpd.db'):

    curr_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
    
    #print("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHh",curr_dir)
    if os.path.exists(os.path.join(curr_dir, 'resources', db_path)):
        os.remove(os.path.join(curr_dir, 'resources', db_path))

    if not os.path.exists(os.path.join(curr_dir, 'resources')):
        os.mkdir(os.path.join(curr_dir, 'resources'))

    conn = sqlite3.connect(os.path.join(curr_dir, 'resources', db_path))
    return conn

def lines_from_pages(pdf_reader):
    list_lines = []


    for page in pdf_reader.pages:
        splitted_line = page.extract_text(extraction_mode="layout", layout_mode_space_vertically=False).split('\n')
        # Assuming your PdfReader supports .pages and .extract_text()
        # text = page.extract_text()
        # if text:  # Check if text extraction was successful
        #     lines = text.split('\n')
        for line in splitted_line:
            field_split = re.split(r'\s{2,}', line)
            list_lines.append(field_split)

    list_lines = list_lines[3:-1]
    return list_lines

# def get_pdf_reader(url):
#     # Initialize and return a PdfReader object
#     headers = {
#         'User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
#     }

#     req = urllib.request.Request(url, headers=headers)
#     with urllib.request.urlopen(req) as response:
#         data = response.read()

#     pdf_data = io.BytesIO(data)
#     pdf_reader = PdfReader(pdf_data) 

#     return pdf_reader

file_path = "C:\\Users\\Akash Balaji\\Downloads\\DATA ENGINEERING\\cis6930sp24-assignment2\\2024-02-01_daily_incident_summary.pdf"
def get_pdf_reader(file_path):
    with open(file_path, 'rb') as file:
        pdf_data = io.BytesIO(file.read())
    pdf_reader = PdfReader(pdf_data)
    return pdf_reader
                   

def dataframe(list_lines):
    # Adjust the slicing as needed, assuming the first few lines are not part of the table
    df = pd.DataFrame(list_lines)
    expected_columns = ['incident_time', 'incident_number', 'incident_location', 'nature', 'incident_ori']
    while len(df.columns) < len(expected_columns):
        df[len(df.columns)] = None  # Adding empty columns as needed to match expected length

    df = df.iloc[:, :len(expected_columns)]  # Slice to expected length
    df.columns = expected_columns  # Rename columns
    df = df[df['incident_time'].notna()]
    df = df[df['incident_time'] != '']  # Remove rows with empty incident_time
    

    return df

def save_csv(df, filename='incident_summary.csv'):
    df.to_csv(filename, index=False)

def save_sql(df, conn):
    df.to_sql('incidents', conn,index=False)

def print_counts(conn):
    query = 'SELECT nature, COUNT(*) as count FROM incidents GROUP BY nature ORDER BY count DESC, nature'
    df = pd.read_sql_query(query, conn)
    a = ""
    for index, row in df.iterrows():
        if(row['nature'] is None):
            a += f"|{row['count']}" 
        else:
            print(f"{row['nature']}|{row['count']}")
    print(a)

#Augmenting functions for weather, side of town, and geolocation

def get_side_of_town(incident_location):
    geolocator = Nominatim(user_agent="specify_your_app_name_here")
    location = geolocator.geocode(incident_location + ', Norman, OK')
    
    if location:
        norman_center = (35.220833, -97.443611)
        incident_coords = (location.latitude, location.longitude)
        lat_diff = incident_coords[0] - norman_center[0]
        lon_diff = incident_coords[1] - norman_center[1]

        if lat_diff > 0 and lon_diff > 0:
            side = 'NE'
        elif lat_diff > 0 and lon_diff < 0:
            side = 'NW'
        elif lat_diff < 0 and lon_diff > 0:
            side = 'SE'
        elif lat_diff < 0 and lon_diff < 0:
            side = 'SW'
        elif lat_diff > 0:
            side = 'N'
        elif lat_diff < 0:
            side = 'S'
        elif lon_diff > 0:
            side = 'E'
        else:
            side = 'W'
        return (side, location.latitude, location.longitude)
    else:
        return ('Unknown', None, None)

import openmeteo_requests
import requests_cache
from retry_requests import retry

# Initialize the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after=-1)
retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
openmeteo = openmeteo_requests.Client(session=retry_session)

def get_weather(location):
    def get_weather(latitude, longitude, start_date, end_date):
    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "start_date": start_date,
        "end_date": end_date,
        "hourly": ["temperature_2m", "precipitation", "weather_code"]
    }
    responses = openmeteo.weather_api(url, params=params)
    # Process the response as needed...
    return processed_data



def main(url):
 # Ensure PdfReader supports BytesIO objects

    pdf_reader = get_pdf_reader(url)
    list_lines = lines_from_pages(pdf_reader)
    df = dataframe(list_lines)
    if not df.empty:
        # Establish a database connection
        conn = get_db_connection()
        save_csv(df)
        df.columns = ['incident_time', 'incident_number', 'incident_location', 'nature', 'incident_ori']
        #print(df.columns)
        save_sql(df, conn)
        print_counts(conn)
        conn.close()  # Close the database connection
        #print(str(url)[-54:])

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--incidents", type=str, required=True, 
                         help="Incident summary url.")
     
    args = parser.parse_args()
    if args.incidents:
        main(args.incidents)
    


    # url = "https://www.normanok.gov/sites/default/files/documents/2024-01/2024-01-17_daily_incident_summary.pdf"
    # main(url)
    #pipenv run python assignment0/main.py --incidents https://www.normanok.gov/sites/default/files/documents/2024-01/2024-01-17_daily_incident_summary.pdf


