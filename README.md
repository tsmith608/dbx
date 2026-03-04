# DbX Synapse (Gandr Analyzer)

**DbX Synapse** is an AI-powered analyzer for IBM i (AS/400) systems. It combines modern FastAPI backends, Watsonx AI agents, and Next.js frontends to help developers search, analyze, and understand complex Db2 catalogs and RPG/COBOL source code.

---

## 🚀 Current Status: Foundation Complete
We have successfully built the **Backend Foundation**, including the database abstraction layer and the initial REST API.

- [x] **FastAPI Core:** Application engine initialized with Swagger documentation.
- [x] **Hybrid Database Layer:** 
    - Supports production **IBM i Access ODBC** connections.
    - Includes a **Mock Database (SQLite)** translation layer for local development without VPN access.
- [x] **Object Search API:** Functional endpoint to search for Db2 tables, views, and schemas.
- [x] **Mock Environment:** Pre-populated with sample Db2 metadata at `data/mock/db2_mock.db`.

---

## 🛠️ Tech Stack
- **Backend:** Python 3.13 + FastAPI
- **Database:** IBM Db2 for i (via `pyodbc`) / SQLite (Mock)
- **AI Agent:** IBM Watsonx (Granite models)
- **Frontend:** Next.js (Tailwind CSS + TypeScript) - *Pending*

---

## 📂 Project Structure
```text
gandr-analyzer/
├── app/
│   ├── api/v1/         # REST API Endpoints (e.g., search)
│   ├── core/           # Configuration & Settings
│   ├── db/             # Connection logic & SQL Queries
│   ├── services/       # Business logic (DB & Source handling)
│   └── main.py         # App entry point
├── data/mock/          # Local SQLite mock database
├── scripts/            # Initialization & Utility scripts
├── .env                # Environment variables (Credentials)
└── README.md           # You are here
```

---

## 🚦 Getting Started

### 1. Prerequisites
- Python 3.13+
- IBM i Access ODBC Driver (for live connections)

### 2. Setup
1. Clone the repository.
2. Initialize the mock database (if not using live IBM i):
   ```bash
   python scripts/init_mock_db.py
   ```
3. Check your `.env` file for credentials.

### 3. Run the Backend
```bash
python -m uvicorn app.main:app --reload
```
View the interactive API docs at: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🗺️ Roadmap
1. **Source Code Handling:** Pre-processing RPG/COBOL files (stripping sequence numbers).
2. **AI Integration:** Integrating Watsonx to explain database schemas.
3. **Frontend Implementation:** Building the Next.js Dashboard.
4. **Dockerization:** Containerizing the entire stack for easy deployment.
