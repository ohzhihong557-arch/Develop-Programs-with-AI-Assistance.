# CareBridge — Module 2: Web Redesign & AI Refactoring

This rebuilds the original CLI tool (`register_patient`, `book_appointment`,
`calculate_bill`, `process_patient_triage`) as a small **Flask** web app with
a JSON API and a single-page frontend. Same validation rules and business
logic as the CLI script — just exposed over HTTP instead of `input()`/`print()`.

## Run it

```bash
pip install -r requirements.txt
python app.py
```

Open **http://127.0.0.1:5000/**

## Architecture

```
carebridge/
├── app.py              # Flask backend — routes + business logic
├── requirements.txt
├── templates/
│   └── index.html       # single-page frontend (4 tabs, one per module)
└── static/
    ├── style.css         # "hospital wayfinding board" design system
    └── app.js            # tab switching + fetch() calls to the API
```

**Backend (`app.py`)** — one Flask route per CLI menu option, each returning
JSON instead of printing to a terminal:

| CLI function              | Web route                          |
|----------------------------|-------------------------------------|
| `register_patient()`       | `POST /api/patients`               |
| `book_appointment()`       | `POST /api/appointments`           |
| `calculate_bill()`         | `POST /api/bill`                   |
| `process_patient_triage()` | `POST /api/triage`                 |

Validation carried over 1:1 from the original CLI (blank-name checks,
positive-age checks, date-within-7-days checks, severity 1–10, etc.), plus
one addition: duplicate `patient_id` is now rejected, since a web form can't
rely on a human re-typing on error the way a `while True:` input loop did.

Data is kept in an in-memory Python list for this demo — good enough to
show the working app end-to-end. Swap in SQLite/Postgres if the project
needs data to survive a restart.

**Frontend (`templates/index.html`, `static/`)** — a single page styled like
a hospital directory board: the header lists the four "wings" (Registration,
Appointments, Billing, Triage) the way a corridor sign would, and each wing
shows a clipboard-style form on the left and a printed chart/slip on the
right that fills in with the API's response.

## Tested

All four endpoints were exercised directly (valid input, invalid input,
edge cases like duplicate patient IDs and out-of-range dates/severities) —
see the project chat log for the request/response pairs. Behaviour matches
the original CLI script's rules exactly.

## Next steps (Modules 3–5)

- **Module 3 (Docker):** wrap this Flask app in a `Dockerfile` on
  `python:3.12-alpine`.
- **Module 4 (ngrok):** run `ngrok http 5000` to get a public URL once the
  container is running locally.
- **Module 5 (AI Assistance):** document how AI was used to port the CLI
  logic into Flask routes + a frontend, and what you had to fix/verify
  yourselves (e.g. the validation-parity checks above).
