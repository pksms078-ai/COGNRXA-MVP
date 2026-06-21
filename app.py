Purpose:
Main application.
Responsibilities:
Plain text
Start server.

Connect database.

Load AI engine.

Handle API requests.
ROUTES
Plain text

Python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "project":"COGNRXA AI",
        "status":"running",
        "version":"0.1.0"
    }

if __name__ == "__main__":
    app.run(debug=True)
backend/config.py
Python
class Config:

    APP_NAME = "COGNRXA AI"

    VERSION = "0.1.0"

    DATABASE = "database/cognrxa.db"

    DEBUG = True

    SECRET_KEY = "COGNRXA_SECRET_KEY"
routes/upload_routes.py
Python
from flask import Blueprint

upload_bp = Blueprint(
    "upload",
    __name__
)

@upload_bp.route("/upload")
def upload():

    return {
        "message":"Upload endpoint"
    }
