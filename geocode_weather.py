import os
import pickle
import requests
class GeocodeWeather:

    def __init__(self):
        if os.path.exists(os.path.join('resources', 'geocode_cache.pkl')):
            with open(os.path.join('resources', 'geocode_cache.pkl'), 'rb') as file:
                self.geocode_cache = pickle.load(file)
        else:
            self.geocode_cache = {}

        if os.path.exists(os.path.join('resources', 'weather_cache.pkl')):
            with open(os.path.join('resources', 'weather_cache.pkl'), 'rb') as file:
                self.weather_cache = pickle.load(file)
        else:
            self.weather_cache = {}

    def save_cache(self):
        with open(os.path.join('resources', 'geocode_cache.pkl'), 'wb') as file:
            pickle.dump(self.geocode_cache, file)

        with open(os.path.join('resources', 'weather_cache.pkl'), 'wb') as file:
            pickle.dump(self.weather_cache, file)

    def get_weather(self, latitude, longitude, datetime):
        
        #print("weather_hit")
        if latitude is None or longitude is None:
            return None
        key = "_".join(map(str,(latitude, longitude, datetime.strftime('%Y-%m-%d'))))
        # if key in weather_cache:
        #     return weather_cache[key]

        date_str = datetime.strftime('%Y-%m-%d')
        time_str = datetime.strftime('%H')
        # cache = get_weather_cache(latitude, longitude, date_str)
        if key in self.weather_cache:
            #print("weather_cache_hit")
            return self.weather_cache[key]
        else:
            params = {
                'latitude': latitude,
                'longitude': longitude,
                'start_date': date_str,
                'end_date': date_str,
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
            self.weather_cache[key] = weather_code
            # pickle.dump(weather_cache, open(os.path.join("resources", 'weather_cache.pkl'), 'wb'))
            # weather_cache[key] = weather_code
            return weather_code
        
    def get_lat_lon(self, incident_location):
        
        #print("geocode_hit")
        if incident_location in self.geocode_cache:
            #print("geocode_cache_hit")
            return self.geocode_cache[incident_location]
        url = "https://geocode-api.arcgis.com/arcgis/rest/services/World/GeocodeServer/findAddressCandidates"
        params = {
            "f":"pjson",
            "singleLine": incident_location,
            "token": "AAPKe5546b6452e0425d8d54da8ffb8806990kyymB9V5RZoiQTmYAeDo5uv8M2X4lsea2BaqBQkzae6cjoidi4MQV5jxrYWTwYk"
            }
        try:
            response = requests.get(url, params=params)
            if response.status_code == 200:
                data = response.json()
                if len(data['candidates']) == 0:
                    self.geocode_cache[incident_location] = (None, None)
                    return (None, None)
                latitude = round(data['candidates'][0]['location']['y'],4)
                longitude = round(data['candidates'][0]['location']['x'],4)
                self.geocode_cache[incident_location] = (latitude, longitude)
                # pickle.dump(cache, open(os.path.join("resources", 'geocode_cache.pkl'), 'wb'))
                return (latitude, longitude)
            else:
                self.geocode_cache[incident_location] = (None, None)
                return (None, None)
        except requests.exceptions.RequestException as e:
            self.geocode_cache[incident_location] = (None, None)
            return (None, None)