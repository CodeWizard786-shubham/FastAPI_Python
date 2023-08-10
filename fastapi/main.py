from pydantic import BaseModel
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import APIKeyHeader
from dotenv import load_dotenv
import os
load_dotenv()
app = FastAPI()

API_KEY = os.getenv('ACCESS_TOKEN')

api_key_header = APIKeyHeader(name="access-token")

async def authenticate_api_key(api_key: str = Depends(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")


# @app.get("/secure")
# async def secure_endpoint(api_key: str = Depends(authenticate_api_key)):
#     return {"message": "This is a secure endpoint"}

app = FastAPI()
db={}

class Item(BaseModel):
    first_name:str
    last_name:str

@app.post("/")
def create_data(item:Item,first:str,last:str,api_key: str = Depends(authenticate_api_key)):
    item.first_name=first
    item.last_name=last
    db[item.first_name]=item.last_name
    return{"Items":item}

@app.get("/")
def get_data(api_key: str = Depends(authenticate_api_key)):
    return db

@app.put("/")
def update_data(item:Item,first:str,last:str):
    item.first_name=first
    item.last_name=last
    db[item.first_name]=item.last_name
    return db

@app.delete("/")
def delete_data(name:str):
    del db[name]
    return db