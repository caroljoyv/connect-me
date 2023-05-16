from fastapi import FastAPI

app = FastAPI()


@app.get("/")           # path operation
def root():
    return {"message": "Welcome to my api peeps!"}

@app.get("/posts")
def get_post():
    return {"data":"This is your post"}

@app.post("/createposts")
def create_post():
    return {"message":"successfully created post"}