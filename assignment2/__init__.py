import os
import pickle
def get_geocode_cache():
    return geocode_cache

def save_geocode_cache(cache):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources', 'geocode_cache.pkl'), 'wb') as file:
        pickle.dump(cache, file)

def get_weather_cache():
    return weather_cache

def save_weather_cache(cache):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources', 'weather_cache.pkl'), 'wb') as file:
        pickle.dump(cache, file)

if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources', 'geocode_cache.pkl')):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources', 'geocode_cache.pkl'), 'rb') as file:
        geocode_cache = pickle.load(file)
else:
    geocode_cache = {}

if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources', 'weather_cache.pkl')):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources', 'weather_cache.pkl'), 'rb') as file:
        geocode_cache = pickle.load(file)
else:
    weather_cache = {}
