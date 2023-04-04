from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date

app = FastAPI()

class User(BaseModel):
    name: str
    email: str
    password: str
    dob: date

users = {
    1: {
        "name": "Kamal",
        "email": "kamal@demo.com",
        "password": "sample@123",
        "dob": "2004/06/30"
    },
    2: {
        "name": "Raja",
        "email": "raja@demo.com",
        "password": "sample@123",
        "dob": "2005/08/10"
    },
    3: {
        "name": "Naveen",
        "email": "naveen@dt3.com",
        "password": "sample@12345",
        "dob": "2005/08/10"
    }
}

@app.get("/api/users/get_details") #127.0.0.1:8000/docs
def get_details():
    return users

@app.post("/api/users/create")
def create_user(new_user: User):
    user_id = max(users.keys())+1
    users[user_id] = new_user.dict()
    return users

@app.put("/api/user/{user_id}")
def update_user(user_id:int, updated_user: User):
    user = users[user_id]
    user["name"] = updated_user.name
    user["email"] = updated_user.email
    user["password"] = updated_user.password
    user["dob"] = updated_user.dob
    
    return users

@app.delete("/api/user/{user_id}")
def delete_user(user_id: int):
    del users[user_id]
    return users

@app.delete("/api/user")
def delete_users(user_ids: list): 
    for user_id in user_ids:
        del users[user_id] 
        return users  

