from fastapi import FastAPI

app = FastAPI()


@app.get("/home/{name}")
def home(name: int):
    return {"this is home page"}
