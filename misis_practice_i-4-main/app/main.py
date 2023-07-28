from fastapi import FastAPI, UploadFile, Request
from fastapi.templating import Jinja2Templates
from data_preparation import data_preparation
from model import prediction
import json
import statistics

app = FastAPI()
templates = Jinja2Templates(directory="../app/templates")


@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload")
async def upload_file(file: UploadFile):
    contents = await file.read()
    print("файл загружен")
    data = json.loads(contents)
    new_row = data_preparation(data)
    pred = prediction(df = new_row)

    return {"prediction": pred, "real": data['data_result']['cargo_space']['calculation_info']['density_percent']}