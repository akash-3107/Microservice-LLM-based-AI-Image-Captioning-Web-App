from fastapi import FastAPI, File, UploadFile
from model.captioning import generate_caption
from model.story import generate_story_from_caption
import shutil

app = FastAPI()

@app.post("/caption")
async def caption_image(file: UploadFile = File(...)):
    temp_path = f"/tmp/{file.filename}"
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    caption = generate_caption(temp_path)
    #story = generate_story_from_caption(caption)
    #print(story)
    return {"caption" : caption}
    #return {"caption": caption, "story": story}
