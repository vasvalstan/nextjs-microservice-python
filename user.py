from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

# in-memory database
users_db: Dict[int, Dict] = {}


class User(BaseModel):
    id: int
    name: str
    email: str


# create user
@app.post("/users")
def create_user(user: User):
    if user.id in users_db:
        raise HTTPException(status_code=400, detail="User already exists")
    users_db[user.id] = user.model_dump()
    return {"message": f"User {user.name} created successfully"}


# get a user
@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = users_db.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# update a user
@app.put("/users/{user_id}")
def update_user(user_id: int, updated_user: User):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    users_db[user_id] = updated_user.model_dump()
    return users_db[user_id]


# delete a user
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    del users_db[user_id]
    return {"message": "User deleted successfully"}


# get all users
@app.get("/users")
def get_all_users():
    return list(users_db.values())
