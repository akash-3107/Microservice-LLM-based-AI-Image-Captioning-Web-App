from fastapi import FastAPI, File, UploadFile
from model.captioning import generate_caption
import shutil

app = FastAPI()

@app.post("/caption")
async def caption_image(file: UploadFile = File(...)):
    temp_path = f"/tmp/{file.filename}"
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    caption = generate_caption(temp_path)
    return {"caption": caption}
