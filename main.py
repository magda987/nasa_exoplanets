from fastapi import FastAPI
import requests

api = FastAPI()

@api.get("/planets")
def planets(limit: int = 10):
    url = f"https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+top+{limit}+pl_name,hostname,sy_snum,sy_pnum,st_mass+from+ps&format=json"
    response = requests.get(url)
    return response.json()

@api.get("/")
def home():
    return "Exoplanets API"