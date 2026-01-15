from fastapi import FastAPI, UploadFile
import pandas as pd
import uvicorn
from models import InfoModel
from pandas import DataFrame

app = FastAPI()


@app.post('/top-threats')
def get_data(file_csv: UploadFile):
    df = pd.read_csv(file_csv.file)
    res = sort_by_danger_rate(df)
    number_of_terrorest, spec_info = get_info(res)
    print(spec_info)
    return {
        "count":number_of_terrorest,
        "top":spec_info
        }

def sort_by_danger_rate(data:DataFrame):
    sort = data.sort_values(by='danger_rate',ascending=False)
    return sort.head(5).to_dict(orient='records')


def get_info(data:list[dict]):    
    return len(data), [InfoModel(**record) for record in data]


if __name__=="__main__":
    uvicorn.run(app,host='0.0.0.0',port=8000)
    