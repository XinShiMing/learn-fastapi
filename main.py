from fastapi import FastAPI

app = FastAPI()


@app.get("/home/{name}")
def home(name: int):
    return {"this is home page"}


@app.get("/home/{age}")
def user_age(age: int):
    return age


@app.get("/test/{page}")
def next_page(page: int):
    return page
