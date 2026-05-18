from fastapi import FastAPI
import os

app = FastAPI()

VERSION = os.getenv("APP_VERSION", "1.0.0")

@app.get("/")
def read_root():
    return {"message": "Hello from FluxCD!", "version": VERSION}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/new-endpoint")
def new_endpoint():
    return {"message": "This is new!"}
