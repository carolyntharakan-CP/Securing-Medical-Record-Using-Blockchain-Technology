from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import hashlib
import os
from config import w3, contract

app = Flask(__name__, template_folder="../frontend")
CORS(app)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def hash_file(file_bytes):
    return hashlib.sha256(file_bytes).hexdigest()

# =========================
# ROUTES - PAGES
# =========================

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/patient_dashboard")
def patient_dashboard():
    return render_template("patient_dashboard.html")

@app.route("/doctor_dashboard")
def doctor_dashboard():
    return render_template("doctor_dashboard.html")

# =========================
# FILE UPLOAD
# =========================

@app.route("/upload", methods=["POST"])
def upload():
    try:
        file = request.files["file"]
        file_bytes = file.read()
        file_hash = hash_file(file_bytes)

        path = os.path.join(UPLOAD_FOLDER, file.filename)
        with open(path, "wb") as f:
            f.write(file_bytes)

        return jsonify({
            "status": "success",
            "file_hash": file_hash,
            "message": "Upload successful. Confirm in MetaMask."
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# =========================
# FETCH RECORDS
# =========================

@app.route("/get_records", methods=["POST"])
def get_records():
    try:
        data = request.json
        user_address = data["address"]

        records = contract.functions.getMyRecords().call({
            "from": user_address
        })

        return jsonify({
            "status": "success",
            "records": records
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# =========================
# RUN SERVER
# =========================

if __name__ == "__main__":
    app.run(debug=True, port=5000)
