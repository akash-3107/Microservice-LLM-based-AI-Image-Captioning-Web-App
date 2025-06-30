from flask import Flask, render_template, request
import requests
from models import db, CaptionLog
import os
from werkzeug.utils import secure_filename


app = Flask(__name__)

# update database details
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///captions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = os.path.join("flask_app", "static", "uploads")
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
db.init_app(app)


FASTAPI_URL = "http://localhost:8000/caption"


@app.before_request
def create_tables():
    db.create_all()



@app.route('/', methods = ['GET','POST'])
def index():
    caption = None
    if request.method == "POST":
        image = request.files["image"]
        filename = secure_filename(image.filename)
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        print(image_path)
        image.save(image_path)

        # send to FastAPI
        with open(image_path, "rb") as f:
            files = {"file": (filename, f, image.content_type)}
            response = requests.post(FASTAPI_URL, files=files)
            caption = response.json().get("caption")
            #story = response.json().get("story")

        # log to the database
        log = CaptionLog(image_name=image.filename, image_path=image_path, caption=caption)
        db.session.add(log)
        db.session.commit()

    return render_template("index.html", caption=caption)


@app.route("/history")
def history():
    logs = CaptionLog.query.order_by(CaptionLog.timestamp.desc()).all()
    return render_template("history.html", logs=logs)


if __name__ == "__main__":
    app.run(debug=True)