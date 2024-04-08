# from assignment2.newmain import get_pdf_reader, lines_from_pages, dataframe_from_lines, save_csv
# import pandas as pd
# import os

# # Sample data for testing
# file_path = "C:/Users/Akash Balaji/Downloads/DATA ENGINEERING/cis6930sp24-assignment2/2024-02-01_daily_incident_summary.pdf"

# sample_pdf_path = file_path
# sample_lines = [['02/01/2024 00:10', '2024-00012345', '123 MAIN ST', 'Traffic Stop', 'PD123'],
#                 ['02/01/2024 00:15', '2024-00012346', '456 ELM ST', 'Suspicious Activity', 'PD456']]

# def test_get_pdf_reader():
#     pdf_reader = get_pdf_reader("https://www.normanok.gov/sites/default/files/documents/2024-01/2024-01-17_daily_incident_summary.pdf")
#     lines = lines_from_pages(pdf_reader)
#     assert isinstance(lines, list)

# def test_save_csv():

#     # Replacing with a sample DataFrame
#     sample_df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
#     save_csv(sample_df)
#     assert os.path.isfile('incident_summary.csv')
   

# def test_lines_from_pages():
#     pdf_reader = get_pdf_reader(sample_pdf_path)
#     lines = lines_from_pages(pdf_reader)
#     assert len(lines) > 0

# def test_dataframe_from_lines():
#     df = dataframe_from_lines(sample_lines)
#     assert len(df) == 2  # Check that two rows were created
#     assert list(df.columns) == ['incident_time', 'incident_number', 'incident_location', 'nature', 'incident_ori']
#     assert df.iloc[0]['incident_number'] == '123456789'  


# import pytest
# from assignment2.newmain import get_pdf_reader, lines_from_pages, dataframe_from_lines, save_csv
# import pandas as pd
# import os

# # Define a sample PDF path for testing
# sample_pdf_path = "https://www.normanok.gov/sites/default/files/documents/2024-03/2024-03-01_daily_incident_summary.pdf"

# def test_get_pdf_reader():
#     pdf_reader = get_pdf_reader(sample_pdf_path)
#     assert pdf_reader is not None

# def test_lines_from_pages():
#     pdf_reader = get_pdf_reader(sample_pdf_path)
#     lines = lines_from_pages(pdf_reader)
#     assert isinstance(lines, list)
#     assert len(lines) > 0

# def test_dataframe_from_lines():
#     pdf_reader = get_pdf_reader(sample_pdf_path)
#     lines = lines_from_pages(pdf_reader)
#     df = dataframe_from_lines(lines)
#     assert isinstance(df, pd.DataFrame)
#     assert len(df) > 0
#     assert list(df.columns) == ['incident_time', 'incident_number', 'incident_location', 'nature', 'incident_ori']

# def test_save_csv(tmpdir):
#     sample_df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
#     csv_file = tmpdir.join("output.csv")
#     save_csv(sample_df, str(csv_file))
#     assert os.path.isfile(str(csv_file))

import pytest
import pandas as pd
from assignment2 import newmain
import os
import pickle

# Define a sample PDF path for testing
sample_pdf_path = "https://www.normanok.gov/sites/default/files/documents/2024-03/2024-03-01_daily_incident_summary.pdf"

# Load caches into the newmain module
newmain.geocode_cache = pickle.load(open(os.path.join(newmain.os.path.dirname(newmain.os.path.dirname(newmain.os.path.abspath(__file__))), 'resources', 'geocode_cache.pkl'), 'rb'))
newmain.weather_cache = pickle.load(open(os.path.join(newmain.os.path.dirname(newmain.os.path.dirname(newmain.os.path.abspath(__file__))), 'resources', 'weather_cache.pkl'), 'rb'))

def test_get_pdf_reader():
    pdf_reader = newmain.get_pdf_reader(sample_pdf_path)
    assert pdf_reader is not None

def test_lines_from_pages():
    pdf_reader = newmain.get_pdf_reader(sample_pdf_path)
    lines = newmain.lines_from_pages(pdf_reader)
    assert isinstance(lines, list)
    assert len(lines) > 0

def test_dataframe_from_lines():
    pdf_reader = newmain.get_pdf_reader(sample_pdf_path)
    lines = newmain.lines_from_pages(pdf_reader)
    df = newmain.dataframe_from_lines(lines)
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0
    expected_columns = ['incident_time', 'incident_number', 'incident_location', 'nature', 'incident_ori', 'day_of_week', 'time_of_day', 'latitude', 'longitude', 'side_of_town', 'weather_code', 'nature_count', 'incident_rank', 'location_count', 'location_rank', 'EMSSTAT']
    assert list(df.columns) == expected_columns


def test_save_csv(tmpdir):
    sample_df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    csv_file = tmpdir.join("output.csv")
    newmain.save_csv(sample_df, str(csv_file))
    assert os.path.isfile(str(csv_file))

