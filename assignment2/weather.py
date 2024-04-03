# import openmeteo_requests
# import requests_cache
# import pandas as pd
# from retry_requests import retry

# cache_session = requests_cache.CachedSession('weather_cache', expire_after=-1)
# retry_session = retry(cache_session, retries=3, backoff_factor=0.5)
# openmeteo = openmeteo_requests.OpenMeteo(session=retry_session)