import os
import json
from flask import Flask

app = Flask(__name__)

# Path for the shared volume
db_path = os.getenv("DB_PATH", "/data/hits.json")

# Ensure the directory exists
os.makedirs(os.path.dirname(db_path), exist_ok=True)

# Ensure the hits.json file exists
if not os.path.exists(db_path):
    with open(db_path, "w") as f:
        json.dump({"hits": 0}, f)

@app.route("/")
def hello_world():
    try:
        # Read and update the hit counter
        with open(db_path, "r+") as f:
            data = json.load(f)
            data["hits"] += 1
            f.seek(0)
            json.dump(data, f)
            f.truncate()
        return f"<h1>Hello, World!</h1><p>Page hits: {data['hits']}</p>"
    except Exception as e:
        return f"<h1>Internal Server Error</h1><p>{e}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

