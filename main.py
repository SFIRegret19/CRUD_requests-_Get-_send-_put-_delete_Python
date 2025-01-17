from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Фёдор, возраст: 20'}

@app.get('/')
async def welcome() -> str:
    return f'Hello!'

@app.get('/users')
async def get_all_users() -> dict:
    return users

@app.post('/user/{username}/{age}')
async def create_user(
        username: Annotated[str, Path(min_length=2,
                                    max_length=20,
                                    regex="^[a-zA-Z0-9_-]+$")],
        age: Annotated[int, Path(gt=0, lt=100)]
    ) -> str:
    current_index = str(int(max(users,key=int)) + 1)
    users[current_index] = f'Имя: {username}, возраст: {age}'
    return f'User {current_index} is registered'

@app.put('/user/{user_id}/{username}/{age}')
async def update_user_info(
        user_id: Annotated[int, Path(gt=0)], 
        username: Annotated[str, Path(min_length=2,
                                    max_length=20,
                                    regex="^[a-zA-Z0-9_-]+$")],
        age: Annotated[int, Path(gt=0, lt=100)]
    ) -> str:
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'The user {user_id} is updated'

@app.delete('/user/{user_id}')
async def delete_message(user_id: Annotated[int, Path(gt=0)],) -> str:
    users.pop(user_id)
    return f'User {user_id} has been deleted'