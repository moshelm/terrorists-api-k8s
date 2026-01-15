from fastapi import FastAPI, UploadFile
import pandas as pd
import uvicorn
from pandas import DataFrame

app = FastAPI()


@app.post('/top-threats')
def get_data(file_csv: UploadFile):
    df = pd.read_csv(file_csv.file)
    res = sort_danger(df)
    print(res)
    return {"massege":res.to_dict(orient='records')}

def sort_danger(data):
    sort = data.sort_values(by='danger_rate',ascending=False)
    return sort.head(5)


if __name__=="__main__":
    uvicorn.run(app,host='0.0.0.0',port=8000)
    