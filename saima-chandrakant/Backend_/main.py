from fastapi import FastAPI

app = FastAPI()

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI backend!!"}

# Another example endpoint
@app.get("/info")
def get_info():
    return {
        "team": "Saima-Chandrakant",
        "backend": "FastAPI",
        "status": "Working"
    }
