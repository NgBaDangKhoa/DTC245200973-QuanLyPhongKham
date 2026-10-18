import os
from flask import Flask, jsonify

app = Flask(__name__)

DB_HOST = os.getenv('DB_HOST', 'postgres-db')
DB_NAME = os.getenv('DB_NAME', 'clinic_db')
DB_USER = os.getenv('DB_USER', 'clinic_admin')

@app.route('/')
def home():
    return jsonify({
        "system": "He thong Quan ly Phong kham / Benh vien",
        "student_name": "Nguyen Ba Dang Khoa",
        "student_id": "DTC245200973",
        "status": "Running successfully"
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)