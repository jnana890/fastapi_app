from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from EC2 + Docker!"}


@app.get("/home")
def read_root():
    return {"message": "welcome to home"}
