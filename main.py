from typing import List
from fastapi import FastAPI, HTTPException

from uuid import uuid4, UUID
from models import User, Gender, Role, UserUpdateRequest
app = FastAPI()

db: List[User] = [
    User(
            id=uuid4(),
            first_name="Nicolas",
            last_name="Schneider",
            gender = Gender.male,
            roles=[Role.admin, Role.user]
        )
]

@app.get("/")
async def root():
    return { "hello": "World" }

@app.get("/api/v1/users")
async def fetch_users():
    return db

@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exist"
    )

@app.put("/api/v1/users/{user_id}")
async def update_user(user_data: UserUpdateRequest, user_id: UUID):
    for user in db:
        if user.id == user_id:
            newUser = User(
                id=user_id,
                first_name=user_data.first_name or user.first_name,
                last_name=user_data.last_name or user.last_name,
                gender=user_data.gender or user.gender,
                roles=user_data.roles or user.roles,
            )
            db[db.index(user)] = newUser
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exist"
    )
