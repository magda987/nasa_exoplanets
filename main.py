from fastapi import FastAPI
# from fastapi package install FastAPI class,  the class will be using an object connecting with server through uvicorn --- fastapi is imported for @api decorator

api = FastAPI()
# creating new object of FastAPI class, kept in api

@api.get("/planets")
def x():
    return "xxxx"


#"get" method is defined in class FastAPI (api)
# if endpoint "/planets" is identified the following function is being executed
