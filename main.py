from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Post(BaseModel):
    title : str
    content : str
    published : bool = True
    rating : Optional[int] = None

#dictionary to store the data
my_post = [{"title": "title of post 1","content":"content of post 1","id":1},{"title":"favourite food","content":"I love shawarma","id":2}]



@app.get("/")           # path operation
def root():
    return {"message": "Welcome to my api peeps!"}

@app.get("/posts")
def get_post():
    return {"data":my_post}

@app.post("/posts")
def create_post(post: Post):
    print(post.rating)
    return {"data":"post recieved"}