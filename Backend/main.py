from fastapi import FastAPI
from pydantic import BaseModel


app=FastAPI()

class Test(BaseModel):
    id:int
    name:str
    origin:str



@app.get("/")
def read_root():
    return {"message":"Hi"}