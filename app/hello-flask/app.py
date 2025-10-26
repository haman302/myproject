from flask import Flask
import os

app = Flask(__name__)

@app.get("/")
def index():
    msg = os.environ.get("APP_MESSAGE", "Hello ISP Modernize")
    env = os.environ.get("APP_ENV", "dev")
    return f"{msg} (env={env})"

@app.get("/healthz")
def healthz():
    token = os.environ.get("SECRET_TOKEN", "")
    return ("ok", 200) if token != "" else ("no token", 503)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

