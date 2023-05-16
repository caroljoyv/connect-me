from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title : str
    content : str
    published : bool = True


@app.get("/")           # path operation
def root():
    return {"message": "Welcome to my api peeps!"}

@app.get("/posts")
def get_post():
    return {"data":"This is your post"}

@app.post("/createposts")
def create_post(new_post: Post):
    print(new_post)
    print(new_post.title)
    print(new_post.published)
    return {"data":"new_post recieved"}