# from os import getenv

from fastapi import FastAPI

from models import db, User


app = FastAPI()


@app.get('/')
async def index():
  return {'hello': 'world'}


@app.get('/users')
async def list_users():
    users = []
    for user in db.users.find():
        users.append(User(**user))
    return {'users': users}


@app.post('/users')
async def create_user(user: User):
    if hasattr(user, 'id'):
        delattr(user, 'id')
    instance = db.users.insert_one(user.dict(by_alias=True))
    user.id = instance.inserted_id
    return {'user': user}
