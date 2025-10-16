# ==============================
# AI-Driven Malware Detection Security (Dummy)
# ==============================
# Framework: FastAPI
# Description: Simulated security module for the backend prototype
# ================================================

from fastapi import FastAPI, HTTPException
from fastapi import Depends  
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from datetime import datetime, timedelta
import base64
import random  

# dummy configuration
DUMMY_KEY = "dummy123"
TOKEN_EXPIRY = 60
auth = HTTPBearer()

# holds token info
class TokenData(BaseModel):
    username: str
    expiry: str

# creates a dummy JWT token
def make_token(username: str):
    exp_time = datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRY)
    token_id = random.randint(1000, 9999)
    token_str = f"jwt-{username}-{token_id}"
    return TokenData(username=username, expiry=exp_time.isoformat())

# basic token to check used as dependency
def verify_token(credentials: HTTPAuthorizationCredentials = Depends(auth)):
    token = credentials.credentials.strip()
    
    if not token.startswith("jwt-") or len(token.split("-")) != 3:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    parts = token.split("-")
    user = parts[1] if len(parts) == 3 else "unknown"
    
    return {"username": user}

# dummy encryption using base64 to represent AES
def encrypt_data(text: str):
    if text == "":
        raise ValueError("Nothing to encrypt.")
    encoded = base64.b64encode(text.encode("utf-8"))
    return encoded.decode("utf-8")

def decrypt_data(data: str):
    try:
        raw = base64.b64decode(data.encode("utf-8"))
        return raw.decode("utf-8")
    except (ValueError, UnicodeDecodeError, base64.binascii.Error):
        raise HTTPException(status_code=400, detail="Failed to decode the provided data.")

# TLS dummy to show awareness of secure connection
def secure_connection():
    print("TLS 1.3 active - secure channel (demo)")

# quick demo run
if __name__ == "__main__":
    secure_connection()
    token = make_token("user01")
    print("Token:", token.dict())
    
    test_input = "Sensitive test data"
    enc = encrypt_data(test_input)
    print("Encrypted:", enc)
    print("Decrypted:", decrypt_data(enc))
