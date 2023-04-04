from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient
from typing import List
from fastapi.encoders import jsonable_encoder

app = FastAPI()

uri ="mongodb+srv://Demo:Demo_123@cluster0.9sjlmqh.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)
db = client. college 

class students(BaseModel):
    name: str
    rollno: int
    email: str
    course: str
    credit: float


@app.get("/api/student/findAll", response_model=List[students])
def list_students():
    students = list(db["students"].find(limit=100))
    return students

@app.post("/api/student/create", response_model=List[students])
def create_student(student: students):
    student = jsonable_encoder(student)
    object_id = db["students"].insert_one(student)
    students = list(db["students"].find(limit=100))
    return students    

@app.get("/api/student/findOne", response_model=students)
def find_one(rollno: int):
    student = db["students"].find_one({"rollno": rollno})
    return student


@app.put("/api/student/update")
def update_student(rollno: int, student: students):
    student = jsonable_encoder(student)
    update_student = db["students"].update_one(
        {"rollno": rollno}, {"$set": student})
    return f"{rollno} updated successfully"


@app.delete("/api/student/delete")
def delete_student(rollno: int):
    delete_student = db["students"].delete_one({"rollno": rollno})
    return f"{rollno} deleted successfully"              




    