import uvicorn
from PIL import Image
from ultralytics import YOLO
import cv2
import os
import io

from fastapi import FastAPI
from fastapi import FastAPI, File, UploadFile, Response, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from PIL import Image

model = YOLO('models/yolov8s_facemask.pt')
app = FastAPI(debug=True)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return "Hi there! Welcome to the Face Mask Detection project. If you want to use the API, please add 'docs' at the end of the link for the documentation."

@app.post("/predict", tags=["Predict papsmear"])
async def predict_image(file: UploadFile = File(...)):
  content_type = file.content_type
  file_name = file.filename
  if content_type is None or file_name is None:
    raise HTTPException(status_code=400, detail="File is Empty")
  if "image" not in content_type:
    raise HTTPException(status_code=400, detail="File is not an image")
  contents = await file.read()
  image = Image.open(io.BytesIO(contents))
  # Convert image to a format compatible with YOLOv8 (e.g., RGB)
  image = image.convert("RGB") if image.mode != "RGB" else image

  # Perform object detection with your custom model to get predictions
  results = model(image)  # Replace with your model's inference call
  for result in results:
        result.save(filename='result.jpg')
    
  # Read the saved result image
  with open("result.jpg", "rb") as file:
        image_bytes = file.read()

  headers = {
    'Content-Type': 'image/jpeg',
    # Consider including confidence scores and abnormal/normal predictions if applicable
  }

  return Response(content=image_bytes, media_type="image/jpeg", headers=headers)

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)