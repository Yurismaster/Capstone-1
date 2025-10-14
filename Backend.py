# ==============================
# AI-Driven Malware Detection Backend (Dummy)
# ==============================
# Framework: FastAPI
# Description: Simulated backend API for the frontend prototype
# ================================================

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Dict
from datetime import datetime, timedelta
import random

app = FastAPI(title="AI Malware Detection Backend (Dummy)")

# ==============================
# Mock Data Structures
# ==============================

class ScanRequest(BaseModel):
    device_id: str
    logs: List[str]

class ScanResult(BaseModel):
    scan_id: str
    device_id: str
    timestamp: str
    risk_level: str
    reasons: List[str]

class AuthToken(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expiry: str

# In-memory cache
scan_results: Dict[str, ScanResult] = {}
users = {"user01": "password123"}  # dummy user storage

# ==============================
# Authentication Endpoints
# ==============================

@app.post("/auth/login", response_model=AuthToken)
def login(username: str, password: str):
    if username not in users or users[username] != password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    expiry = (datetime.now() + timedelta(hours=1)).isoformat()
    token = f"jwt-{username}-{random.randint(1000,9999)}"
    return AuthToken(access_token=token, expiry=expiry)

# ==============================
# Scan Endpoints
# ==============================

@app.post("/scan", response_model=ScanResult)
def post_scan(request: ScanRequest):
    """
    Simulates receiving encrypted logs and returning a dummy scan result.
    """
    scan_id = f"scan-{random.randint(10000,99999)}"
    risk_level = random.choice(["Low", "Medium", "High"])
    reasons = [
        "Suspicious network activity",
        "Unusual file access",
        "Sensitive permission used"
    ]
    result = ScanResult(
        scan_id=scan_id,
        device_id=request.device_id,
        timestamp=datetime.now().isoformat(),
        risk_level=risk_level,
        reasons=random.sample(reasons, 3)
    )
    scan_results[scan_id] = result
    return result

@app.get("/results/{device_id}", response_model=List[ScanResult])
def get_results(device_id: str):
    """
    Fetch dummy scan results for a given device.
    """
    device_scans = [r for r in scan_results.values() if r.device_id == device_id]
    if not device_scans:
        raise HTTPException(status_code=404, detail="No results found")
    return device_scans

# ==============================
# Alert & History Endpoints
# ==============================

@app.get("/alerts/{device_id}")
def get_alerts(device_id: str):
    """
    Simulates alert retrieval.
    """
    alerts = [
        {"alert_id": "A1", "type": "Data Leak", "status": "Active"},
        {"alert_id": "A2", "type": "Malicious Network Activity", "status": "Resolved"}
    ]
    return {"device_id": device_id, "alerts": alerts}

@app.get("/history/{device_id}")
def get_scan_history(device_id: str):
    """
    Returns simplified historical logs.
    """
    history = [
        {"date": "2025-10-01", "risk": "Low"},
        {"date": "2025-10-05", "risk": "Medium"},
        {"date": "2025-10-10", "risk": "High"},
    ]
    return {"device_id": device_id, "history": history}

# ==============================
# System & Debug
# ==============================

@app.get("/status")
def get_status():
    """
    Returns system health and version info.
    """
    return {
        "backend": "FastAPI Dummy Backend v1.0",
        "status": "Running",
        "active_scans": len(scan_results)
    }
