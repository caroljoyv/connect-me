from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()


@app.get("/")           # path operation
def root():
    return {"message": "Welcome to my api peeps!"}

@app.get("/posts")
def get_post():
    return {"data":"This is your post"}

@app.post("/createposts")
def create_post(payload: dict = Body(...)):
    print(payload)
    return {"newpost":f"title: {payload['title']} content:{payload['content']}"}