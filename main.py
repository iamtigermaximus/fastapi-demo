from typing import List
from fastapi import FastAPI, HTTPException
from uuid import UUID
from models import Gender, User, Role, UserUpdateRequest

app= FastAPI()

db:List[User]=[
    # User(
    #     id=UUID("d74ea12f-0f5f-4882-855e-dcf406251241"), 
    #     first_name="Siegfred", 
    #     last_name="Gamboa", 
    #     middle_name="Molina",
    #     gender=Gender.male, 
    #     role=[Role.admin]
    #     ),
    # User(
    #     id=UUID("c4abb58c-4dd7-462f-8038-9369e6cd7311"), 
    #     first_name="Alonzo", 
    #     last_name="Gamboa", 
    #     middle_name="Villanueva",
    #     gender=Gender.male, 
    #     role=[Role.user]
    #     ),
    #  User(
    #     id=UUID("9f6ae96f-1e59-4365-b294-112b6036986e"), 
    #     first_name="Saige", 
    #     last_name="Gamboa", 
    #     middle_name="Villanueva",
    #     gender=Gender.female, 
    #     role=[Role.student]
    #     )
]

@app.get("/")
async def root():
    return {"HELLO": "WORLD"}

@app.get("/api/v1/users")
async def fetch_users():
    return db;

@app.post("/api/v1/users")
async def register_user(user:User):
    db.append(user)
    return {"id":user.id}

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id:UUID):
    for user in db:
        if user.id==user_id:
           db.remove(user)
           return
    raise HTTPException(
        status_code=404,
        detail=f"user with id : {user_id} does not exist"
    )

@app.put("/api/v1/users/{user_id}")
async def update_user(user_update:UserUpdateRequest,user_id:UUID):
    for user in db:
        if user.id==user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.middle_name is not None:
                user.middle_name = user_update.middle_name
            if user_update.roles is not None:
                user.roles = user_update.role
            return
        raise HTTPException(
            status_code=404,
            detail=f"user with id : {user_id} does not exist"
    )

@app.get("/api/v1/users/{user_id}")
async def fetch_user_by_id(user_id:UUID):
    for user in db:
        if user.id==user_id:
           return user
    raise HTTPException(
        status_code=404,
        detail=f"user with id : {user_id} does not exist"
    )
    
