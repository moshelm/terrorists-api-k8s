from fastapi import FastAPI, UploadFile,HTTPException, Depends,File
import pandas as pd
from pandas import DataFrame
from io import BytesIO
import os
import uvicorn
from models import BasicInfoTerrorist, TopThreatsResponse
from db import MongoManager


MONGO_HOST = os.getenv("MONGO_HOST","127.0.0.1")
MONGO_PORT = os.getenv("MONGO_PORT","27017")
MONGO_USERNAME = os.getenv("MONGO_USERNAME","admin")  
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD","secretpass")
MONGO_DB = os.getenv("MONGO_DB","threat_db")
MONGO_AUTH_SOURCE = os.getenv("MONGO_AUTH_SOURCE","admin")


app = FastAPI()

db = MongoManager()

def get_db():
    return db

@app.post('/top-threats',response_model=TopThreatsResponse)
async def getting_and_processing_data(file: UploadFile = File(...), database = Depends(get_db) ):
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400,detail="Invalid type file")
    # 1. read from file
    contatns = await file.read()
    df = pd.read_csv(BytesIO(contatns))
    # 2. Data processing
    data = sort_by_danger_rate(df)
    number_of_recoreds, spec_info = get_specific_info(data)
    # 3. insert to db
    db.insert_all(spec_info)

    return {
        "count":number_of_recoreds,
        "top":spec_info
        }

def sort_by_danger_rate(data:DataFrame):
    """
    sorting by column danger_rate 
    return in dict form
    
    :param data: Description
    :type data: DataFrame
    return: data sorted in dict form
    """
    raw_records = data.sort_values(by='danger_rate',ascending=False).head(5)
    return raw_records.to_dict(orient='records')


def get_specific_info(data: list[dict]) -> tuple[int,list[dict]]:    
    recoreds = [BasicInfoTerrorist(**record).model_dump(by_alias=True) for record in data]
    return len(recoreds), recoreds
    

if __name__=="__main__":
    uvicorn.run(app,host='0.0.0.0',port=8000)
    