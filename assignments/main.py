from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/health")
def health():
    return {"message": "Service is online"}
