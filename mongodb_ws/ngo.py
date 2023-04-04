from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi import Form,File
from pydantic import BaseModel
from pymongo import MongoClient
from typing import List
from fastapi.encoders import jsonable_encoder

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/registerPage", response_class=HTMLResponse)#http://127.0.0.1:8000/registerPage/
def show_service_page(request: Request):
    return templates.TemplateResponse("index.html", context={"request": request})

uri ="mongodb+srv://Demo:Demo_123@cluster0.9sjlmqh.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)
db = client.NGO

class Donors(BaseModel):
    name: str = Form()
    email: str = Form()
    contact: int = Form()
    reg_date: str = Form()
    m_id: int = Form()


@app.get("/api/donor/findAll", response_model=List[Donors])#http://127.0.0.1:8000/api/donor/findAll
def list_Donors():
    Donors = list(db["Donors"].find(limit=100))
    return Donors

@app.post("/api/donor/create", response_model=List[Donors])  #http://127.0.0.1:8000/api/donor/create 
def create_donor(donor: Donors):
    donor = jsonable_encoder(donor)
    object_id = db["Donors"].insert(donor)
    Donors = list(db["Donors"].find(limit=100))
    return Donors

@app.get("/api/donor/findOne", response_model=Donors) #http://127.0.0.1:8000/api/donor/findOne
def find_one(m_id: int):
    donor = db["Donors"].find_one({"m_id": m_id})
    return donor


@app.put("/api/donor/update") #http://127.0.0.1:8000/api/donor/update
def update_donor(m_id: int, donor: Donors):
    donor = jsonable_encoder(donor)
    update_donor = db["Donors"].update_one(
        {"m_id": m_id}, {"$set": donor})
    return f"{m_id} updated successfully"


@app.delete("/api/donor/delete") #http://127.0.0.1:8000/api/donor/delete
def delete_donor(m_id: int):
    delete_donor = db["Donors"].delete_one({"m_id": m_id})
    return f"{m_id} deleted successfully"      



        


