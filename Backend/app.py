"""
CareBridge Hospital Management System — Web Backend (Module 2)

Rebuilds the original CLI tool (register / book appointment / calculate bill /
triage) as a Flask web application with a JSON API and a single-page frontend.

Run:
    pip install -r requirements.txt
    python app.py
Then open http://127.0.0.1:5000/
"""

from datetime import datetime, timedelta, date
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# ---------------------------------------------------------------------------
# Constants (carried over from the original CLI script)
# ---------------------------------------------------------------------------
BASE_CONSULTATION_FEE = 100
LAB_TEST_RATE = 10

# ---------------------------------------------------------------------------
# In-memory "database" — good enough for a demo / local deployment.
# Swap for a real DB (SQLite/Postgres) if the project needs persistence.
# ---------------------------------------------------------------------------
patients = []
appointments = []


def error(message, status=400):
    return jsonify({"ok": False, "error": message}), status


# ---------------------------------------------------------------------------
# Page
# ---------------------------------------------------------------------------
@app.route("/")
def index():
    return render_template("index.html")


# ---------------------------------------------------------------------------
# 1. Register Patient
# ---------------------------------------------------------------------------
@app.route("/api/patients", methods=["GET", "POST"])
def api_patients():
    if request.method == "GET":
        return jsonify({"ok": True, "patients": patients})

    data = request.get_json(silent=True) or {}
    name = str(data.get("name", "")).strip()
    age_raw = data.get("age", "")
    patient_id = str(data.get("patient_id", "")).strip()

    if not name:
        return error("Name cannot be blank.")

    try:
        age = float(age_raw)
    except (TypeError, ValueError):
        return error("Age must be a valid positive number.")

    if age <= 0:
        return error("Age must be a positive number.")

    if age.is_integer():
        age = int(age)

    if not patient_id:
        return error("Patient ID cannot be blank.")

    if any(p["patient_id"] == patient_id for p in patients):
        return error(f"Patient ID '{patient_id}' is already registered.")

    record = {"name": name, "age": age, "patient_id": patient_id}
    patients.append(record)
    return jsonify({"ok": True, "patient": record}), 201


# ---------------------------------------------------------------------------
# 2. Book Appointment
# ---------------------------------------------------------------------------
@app.route("/api/appointments", methods=["GET", "POST"])
def api_appointments():
    if request.method == "GET":
        return jsonify({"ok": True, "appointments": appointments})

    data = request.get_json(silent=True) or {}
    dept_raw = str(data.get("department", "")).strip().lower()
    date_raw = str(data.get("date", "")).strip()

    if dept_raw not in ("gp", "specialist"):
        return error("Department must be 'GP' or 'Specialist'.")
    department = "GP" if dept_raw == "gp" else "Specialist"

    try:
        parsed_date = datetime.strptime(date_raw, "%Y-%m-%d").date()
    except ValueError:
        return error("Invalid date format. Use YYYY-MM-DD.")

    today = date.today()
    max_date = today + timedelta(days=7)
    if not (today <= parsed_date <= max_date):
        return error(f"Appointment date must be within 7 days of today ({today}).")

    record = {
        "department": department,
        "date": parsed_date.isoformat(),
        "date_display": parsed_date.strftime("%A, %B %d, %Y"),
    }
    appointments.append(record)
    return jsonify({"ok": True, "appointment": record}), 201


# ---------------------------------------------------------------------------
# 3. Calculate Bill
# ---------------------------------------------------------------------------
@app.route("/api/bill", methods=["POST"])
def api_bill():
    data = request.get_json(silent=True) or {}
    patient_type = str(data.get("patient_type", "")).strip()
    num_raw = data.get("num_labtests", "")

    if patient_type not in ("Subsidised", "Private"):
        return error("Patient type must be 'Subsidised' or 'Private'.")

    if not str(num_raw).strip().isdigit():
        return error("Number of lab tests must be a whole number.")
    num_labtests = int(num_raw)

    subtotal = BASE_CONSULTATION_FEE + (num_labtests * LAB_TEST_RATE)
    total = subtotal * 0.7 if patient_type == "Subsidised" else subtotal

    return jsonify({
        "ok": True,
        "bill": {
            "patient_type": patient_type,
            "num_labtests": num_labtests,
            "subtotal": round(subtotal, 2),
            "total": round(total, 2),
        }
    })


# ---------------------------------------------------------------------------
# 4. Assign Triage Room
# ---------------------------------------------------------------------------
@app.route("/api/triage", methods=["POST"])
def api_triage():
    data = request.get_json(silent=True) or {}
    raw = str(data.get("severity", "")).strip()

    if not raw.isdigit() or not (1 <= int(raw) <= 10):
        return error("Severity must be a whole number from 1 to 10.")

    severity = int(raw)
    if severity <= 4:
        room = "Waiting Room"
    elif severity <= 7:
        room = "Room 1"
    else:
        room = "Room 2"

    return jsonify({"ok": True, "triage": {"severity": severity, "room": room}})


if __name__ == "__main__":
    app.run(debug=True)
