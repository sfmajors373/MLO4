from starlette.responses import StreamingResponse
from fastapi import FastAPI, File, UploadFile
import requests

#We generate a new FastAPI app in the Prod environment
#https://fastapi.tiangolo.com/

app = FastAPI(title='FastAPI main', root_path="/Prod/")

#Call your get function for a health Check
#to receive both (face-bokeh and face-emotion)
@app.get("/", tags=["Health Check"])
async def root():
    # may need to change it to 8000 instead of 8001/8002
    response_face_bokeh = response.get("http://face_bokeh_service:8000")
    response_face_emotion = resonse.get("http://face_emotion_service:8000")
    return {"Face bokeh": "OK",
            "Face emotion": "OK"}
