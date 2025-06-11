from flask import Flask, render_template, request
import requests

app = Flask(__name__)

FASTAPI_URL = "http://localhost:8000/caption"

@app.route('/', methods = ['GET','POST'])
def index():
    caption = None
    if request.method == "POST":
        image = request.files["image"]
        files = {"file": (image.filename, image.stream, image.content_type)}
        response = requests.post(FASTAPI_URL, files=files)
        caption = response.json().get("caption")
    return render_template("index.html", caption=caption)

if __name__ == "__main__":
    app.run(debug=True)