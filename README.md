# cis6930sp24-assignment2

This assignment is a continuation of assignment 0. In assignment 0 we worked with police website, Norman PD. They have a daily incident_summarypdf describing incidents happening everyday. In assignment 0, we extracted the fields from a given url which links to a incident_summary pdf. In this assignment, we add on to it. We perform data augmentation by taking records from several instances of pdf files and augment the data. We also created a Datasheet for the dataset. 

# API used:
(The geocoding API the one suggested was very slow I used this open-source free one instead)
For geocoding, I used the ArcGIS Developers
Link: https://developers.arcgis.com/

For weather code, I used the openmeteo historical weather API that was suggested in the assignment. 
Link: https://open-meteo.com/en/docs/historical-weather-api

Now I will dive in to the functionalities of the code:

# assignment2.py

The module assignment2.py provides a set of functions for processing PDF files containing incident data. The main functionality includes extracting lines of text from PDF files, converting them into a pandas DataFrame, and augmenting the data with additional information such as the side of town and EMSSTAT status. The module also supports caching the final DataFrame to reduce processing time for subsequent runs.

Key functions include:

lines_from_pages: Extracts lines of text from each page of a PDF.
get_pdf_reader: Retrieves a PDF file from a URL and returns a PdfReader object for further processing.
dataframe_from_lines: Converts the extracted lines into a DataFrame and performs additional data transformations.
get_side_of_town: Determines the side of town based on latitude and longitude coordinates.
check_emsstat: Updates the EMSSTAT status for each incident in the DataFrame.
load_final_df_cache and save_final_df_cache: Functions for loading and saving the final DataFrame from/to a cache file to improve efficiency.
The main function orchestrates the processing of PDF files specified in a CSV file and generates an output CSV file with the processed data. It also prints the data to the console for quick viewing. This module is designed to be used as a command-line tool, with the --urls argument specifying the path to the CSV file containing the URLs to the PDF files.

def lines_from_pages(pdf_reader):
    """
    Extracts lines of text from each page of a PDF using the provided pdf_reader object.

    Args:
        pdf_reader (PDFReader): The PDF reader object used to read the PDF.

    Returns:
        list: A list of lines extracted from the PDF pages.
    """

def get_pdf_reader(url):
    """
    Retrieves a PDF file from the given URL and returns a PdfReader object.

    Args:
        url (str): The URL of the PDF file.

    Returns:
        PdfReader: A PdfReader object representing the PDF file.

    Raises:
        urllib.error.URLError: If there is an error while retrieving the PDF file.

    """

def dataframe_from_lines(list_lines):
    """
    Convert a list of lines into a pandas DataFrame with additional data transformations.

    Args:
        list_lines (list): A list of lines representing the data.

    Returns:
        pandas.DataFrame: The transformed DataFrame.

    """

def get_side_of_town(latitude, longitude):
    """
    Determines the side of town based on the given latitude and longitude.

    Args:
        latitude (float): The latitude coordinate.
        longitude (float): The longitude coordinate.

    Returns:
        str: The side of town based on the given coordinates. Possible values are:
            - 'NE' for Northeast
            - 'NW' for Northwest
            - 'SE' for Southeast
            - 'SW' for Southwest
            - 'N' for North
            - 'S' for South
            - 'E' for East
            - 'W' for West
            - 'Unknown' if either latitude or longitude is None.
    """

def check_emsstat(df, ori_colunm='incident_ori', time_column='incident_time', location_column='incident_location'):
    """
    Checks the EMSSTAT status for each incident in the given DataFrame and updates the 'EMSSTAT' column accordingly.

    Args:
        df (pandas.DataFrame): The DataFrame containing the incident data.
        ori_colunm (str, optional): The name of the column containing the incident origin information. Defaults to 'incident_ori'.
        time_column (str, optional): The name of the column containing the incident time information. Defaults to 'incident_time'.
        location_column (str, optional): The name of the column containing the incident location information. Defaults to 'incident_location'.

    Returns:
        None
    """

def load_final_df_cache(cache_file):
    """
    Load the final DataFrame from a cache file.

    Parameters:
    cache_file (str): The name of the cache file.

    Returns:
    object: The loaded DataFrame object if the cache file exists, otherwise None.
    """

def save_final_df_cache(df, cache_file):
    """
    Save the given DataFrame to a cache file.

    Args:
        df (pandas.DataFrame): The DataFrame to be saved.
        cache_file (str): The name of the cache file.

    Returns:
        None
    """

def main():
    """
    Process PDF for incident data.

    This function reads a CSV file containing URLs to PDF files, downloads and processes each PDF file,
    and generates an output CSV file with specific columns. It also prints the processed data to the console.

    Args:
        --urls (str): Path to the CSV file containing URLs to PDF files.

    Returns:
        None
    """

# geocode_weather.py


The GeocodeWeather class provides a centralized way to handle geocoding and weather data retrieval for incident locations. It leverages caching mechanisms to optimize performance by reducing redundant API calls.

Key components of the GeocodeWeather class include:

geocode_cache: A dictionary that stores previously retrieved geocoding information to avoid repeated requests for the same location.
weather_cache: A similar dictionary for caching weather information based on location and date.
The class offers the following methods:

save_cache(): Persists the current state of the geocode and weather caches to disk, allowing for reuse in future runs of the application.
get_weather(latitude, longitude, datetime): Fetches weather information for a specified location and time. It first checks the cache for existing data before making an API call.
get_lat_lon(incident_location): Retrieves the geographical coordinates for a given incident location, using the cache to minimize API requests.
By encapsulating geocoding and weather data retrieval in the GeocodeWeather class, the code becomes more modular, maintainable, and efficient, especially when dealing with large datasets.

class GeocodeWeather:
    """
    A class that provides methods to retrieve geocode and weather information.

    Attributes:
        geocode_cache (dict): A dictionary to cache geocode information.
        weather_cache (dict): A dictionary to cache weather information.

    Methods:
        save_cache(): Saves the geocode and weather cache to disk.
        get_weather(latitude, longitude, datetime): Retrieves the weather information for a given latitude, longitude, and datetime.
        get_lat_lon(incident_location): Retrieves the latitude and longitude for a given incident location.
    """

    def save_cache(self):
        """
        Saves the geocode and weather cache to disk.
        """

    def get_weather(self, latitude, longitude, datetime):
        """
        Retrieves the weather information for a given latitude, longitude, and datetime.

        Args:
            latitude (float): The latitude of the location.
            longitude (float): The longitude of the location.
            datetime (datetime): The datetime for which weather information is requested.

        Returns:
            int or None: The weather code corresponding to the given location and datetime, or None if the information is not available.
        """

    def get_lat_lon(self, incident_location):
        """
        Retrieves the latitude and longitude for a given incident location.

        Args:
            incident_location (str): The incident location for which latitude and longitude are requested.

        Returns:
            tuple or None: A tuple containing the latitude and longitude of the incident location, or None if the information is not available.
        """


# test_newmain.py

The test_newmain.py file contains unit tests for the functions in the newmain.py module. These tests ensure the correctness and reliability of the functions.

test_get_pdf_reader(): This test verifies that the get_pdf_reader function is able to fetch a PDF file from a URL and return a PdfReader object.
test_lines_from_pages(): This test checks if the lines_from_pages function correctly extracts lines of text from a PDF file and returns them as a list.
test_dataframe_from_lines(): This test ensures that the dataframe_from_lines function successfully converts a list of lines into a pandas DataFrame with the expected columns.
test_save_csv(tmpdir): This test checks if the save_csv function correctly saves a DataFrame as a CSV file in a specified directory.

def test_get_pdf_reader():
    """
    Test case for the get_pdf_reader function.

    This test verifies that the get_pdf_reader function returns a non-null value.

    """

def test_lines_from_pages():
    """
    Test the lines_from_pages function.

    This function tests the lines_from_pages function by checking if the returned value is a list and if the list has a length greater than 0.

    Returns:
        None
    """

def test_dataframe_from_lines():
    """
    Test case for the `dataframe_from_lines` function.

    This test case verifies that the `dataframe_from_lines` function returns a pandas DataFrame
    with the expected columns and non-zero length.

    It performs the following assertions:
    - The returned object is an instance of pd.DataFrame.
    - The length of the DataFrame is greater than 0.
    - The columns of the DataFrame match the expected columns.

    """

def test_save_csv(tmpdir):
    """
    Test function to check if the save_csv function correctly saves a DataFrame as a CSV file.

    Parameters:
    - tmpdir: A temporary directory provided by the pytest framework.

    Returns:
    - None

    Raises:
    - AssertionError: If the CSV file is not created.

    """

# Running the code:

To execute the program use the following command:

`pipenv run python .\assignment2.py --url file.csv`

where file.csv consists of the urls

To perform the test file use:
`pytest`

Note: In the video the code execution is pretty fast as I have the cache details. For new urls expect it to take two to five minutes. 


https://github.com/akash-2303/cis6930sp24-assignment2/assets/67377539/4d3502e3-deb2-41ca-a9b9-043ab13c5678



# Bugs and Assumptions
I have dropped the empty cells. 
For the first run, program might take two to five minutes to execute. 
Couldnt implement async functions as it was messing up with my API calls. 
Only checked for the exact coordinates. Did not cache nearby locations and weather code. I feel like implementing that would have improved performance. 

