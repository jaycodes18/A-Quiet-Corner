from flask import Flask, render_template, request, jsonify
import json
import os
from datetime import datetime, timedelta

app = Flask(__name__)
DATA_FILE = "diary_entries.json"
DATA_KEY = "diary_entries"

# Vercel KV in production, local JSON file when developing
redis = None
if os.environ.get("KV_REST_API_URL"):
    try:
        import importlib
        Redis = importlib.import_module("upstash_redis").Redis
        redis = Redis.from_env()
    except (ImportError, AttributeError):
        redis = None

def load_entries():
    if redis:
        data = redis.get(DATA_KEY)
        return json.loads(data) if data else {}
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}

def save_entries(entries):
    if redis:
        redis.set(DATA_KEY, json.dumps(entries))
        return
    with open(DATA_FILE, "w") as f:
        json.dump(entries, f, indent=4)

@app.route('/')
def home():
    return render_template('journal.html', initial_date="")

@app.route('/get_pages')
def get_pages():
    target_date_str = request.args.get('date')
    if not target_date_str:
        return jsonify({"error": "date is required"}), 400
    try:
        date_obj = datetime.strptime(target_date_str, "%Y-%m-%d")
    except ValueError:
        return jsonify({"error": "invalid date format"}), 400

    entries = load_entries()
    next_date_obj = date_obj + timedelta(days=1)
    next_date_str = next_date_obj.strftime("%Y-%m-%d")

    return jsonify({
        "left_date": target_date_str,
        "left_header": date_obj.strftime("%A, %B %d, %Y"),
        "left_content": entries.get(target_date_str, ""),
        "right_date": next_date_str,
        "right_header": next_date_obj.strftime("%A, %B %d, %Y"),
        "right_content": entries.get(next_date_str, "")
    })

@app.route('/write', methods=['POST'])
def write():
    entries = load_entries()

    for side in ('left', 'right'):
        date_str = request.form.get(f'{side}_date', '').strip()
        content = request.form.get(f'{side}_content', '').strip()
        if not date_str:
            continue
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            continue
        if content:
            entries[date_str] = content
        else:
            entries.pop(date_str, None)

    entries.pop("", None)
    save_entries(entries)
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)