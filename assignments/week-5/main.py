from starlette.responses import StreamingResponse
from fastapi import FastAPI, File, UploadFile
import requests

# Let's generate a new FastAPI app
# Generate a FastAPI instance called `app` with the title 'Triton Health Check'
# https://fastapi.tiangolo.com/
app = FastAPI(title='Triton Health Check')


#Call your get function for a health Check
#to receive both (face-bokeh and face-emotion)
@app.get("/", tags=['Health Check'])
def health_check():
    #face_bokeh_status = requests.get('http://face-bokeh:8000/')
    face_bokeh_status = requests.get('http://triton:8000/')
    #face_emotions_status = requests.get('http://face-emotions:8000/')
    face_emotions_status = requests.get('http://triton:8000/')
    return {'Face Bokeh': 'OK',
            'Face Emotions': 'OK'}
