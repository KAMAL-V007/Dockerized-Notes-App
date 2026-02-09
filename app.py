# flask app
from flask import Flask, render_template, request, redirect
import redis
import os
import json
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

# Externalized configuration for 12-factor app compliance
REDIS_HOST = os.getenv("REDIS_HOST", "redis_db")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

# Connect to Redis
# We use 'decode_responses=True' so we get Strings back, not Bytes
r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0, decode_responses=True)


@app.route("/")
def index():
    # Get all keys from Redis
    keys = r.keys()
    notes = []
    for key in keys:
        # Get value for each key
        val = r.get(key)
        notes.append({"id": key, "content": val})
    return render_template("index.html", notes=notes)


@app.route("/add", methods=["POST"])
def add_note():
    content = request.form.get("content")
    if content:
        # Create a simple unique ID using the length of existing keys + random
        note_id = f"note:{r.dbsize() + 1}"
        r.set(note_id, content)
    return redirect("/")


@app.route("/delete/<note_id>", methods=["POST"])
def delete_note(note_id):
    r.delete(note_id)
    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
