from fastapi import FastAPI
import requests
# from fastapi package install FastAPI class,  the class will be using an object connecting with server through uvicorn --- fastapi is imported for @api decorator

api = FastAPI()
# creating new object of FastAPI class, kept in api

@api.get("/planets")
def planets(limit: int = 10):
    url = f"https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+top+{limit}+pl_name,hostname,sy_snum,sy_pnum,st_mass+from+ps&format=json"
    response = requests.get(url)
    return response.json()

#response returns many metadata, using json method helps to get only .json converted to directory 
#json is function of class Response (method) --- applicable only to Response class objects
#get is normal function

#"get" method is defined in class FastAPI (api)
# if (url) endpoint "/planets" is identified the following function is being executed

@api.get("/")
def home():
    return "Exoplanets API"