from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title : str
    content : str
    published : bool = True
    rating : Optional[int] = None

#dictionary to store the data
my_post = [{"title": "title of post 1","content":"content of post 1","id":1},{"title":"favourite food","content":"I love shawarma","id":2}]


def find_post(id):      #function to find a post with a certain id
    for p in my_post:
        if p['id'] == id:
            return p


@app.get("/")           # path operation
def root():
    return {"message": "Welcome to my api peeps!"}

@app.get("/posts")     #get method
def get_post():
    return {"data":my_post}

@app.post("/posts")    #post method
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0,10000)
    my_post.append(post_dict)
    return {"data":post_dict }
    
#retrieving a post by id
@app.get("/posts/{id}")
def get_posts(id):
    post = find_post(int(id))
    return {"Post details ": post}



