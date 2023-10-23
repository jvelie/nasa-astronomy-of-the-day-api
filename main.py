import requests
from dotenv import load_dotenv
import os

load_dotenv()

nasa_api = os.getenv("NASA_API")
apod_url = f"https://api.nasa.gov/planetary/apod?api_key={nasa_api}"

results = requests.json(apod_url)
results_object = results.json()
picture_url = results_object["url"]
split_url = picture_url.split("/")
filename = split_url[-1]

with open (filename, "wb") as f:
    f.write(picture_url.content)