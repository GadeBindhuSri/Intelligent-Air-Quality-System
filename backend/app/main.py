from datetime import datetime, timedelta
from random import uniform
from typing import Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from .ml import predict

app = FastAPI(title="Intelligent Air Quality API", version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

readings = []
now = datetime.now()
for i in range(24):
    readings.append({
        "timestamp": (now - timedelta(hours=23-i)).isoformat(),
        "pm25": round(uniform(15, 85), 1),
        "pm10": round(uniform(30, 130), 1),
        "temperature": round(uniform(24, 34), 1),
        "humidity": round(uniform(45, 80), 1),
        "co2": round(uniform(450, 1100), 0)
    })

class Reading(BaseModel):
    pm25: float
    pm10: float
    temperature: float
    humidity: float
    co2: Optional[float] = None

def aqi_category(pm25: float):
    # Demonstration category bands; replace with the exact standard selected by your project.
    if pm25 <= 30: return "Good"
    if pm25 <= 60: return "Satisfactory"
    if pm25 <= 90: return "Moderate"
    if pm25 <= 120: return "Poor"
    if pm25 <= 250: return "Very Poor"
    return "Severe"

@app.get("/")
def root():
    return {"message": "Air Quality API is running"}

@app.get("/api/health")
def health():
    return {"status": "ok"}

@app.get("/api/readings/latest")
def latest():
    return readings[-1]

@app.get("/api/readings")
def history(limit: int = 50):
    return readings[-max(1, min(limit, 500)):]

@app.post("/api/readings")
def add_reading(reading: Reading):
    item = {"timestamp": datetime.now().isoformat(), **reading.model_dump()}
    readings.append(item)
    if len(readings) > 500: readings.pop(0)
    return {"saved": True, "reading": item}

@app.get("/api/aqi")
def current_aqi():
    r = readings[-1]
    return {"pm25": r["pm25"], "category": aqi_category(r["pm25"])}

@app.get("/api/predictions")
def predictions():
    r = readings[-1]
    return predict(r)
