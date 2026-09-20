# Intelligent Air Quality Monitoring & Pollution Prediction System

A complete IoT + AI starter system for ESP32 air-quality monitoring.

## Stack
- ESP32 + particulate/environment sensors
- FastAPI + SQLite (demo) backend
- React + Vite dashboard
- Python machine-learning prediction baseline
- Docker-ready structure

## Quick start
### Backend
```powershell
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Open http://localhost:8000/docs

### Frontend
```powershell
cd frontend
npm install
npm run dev
```

Open the Vite URL shown in the terminal.

The backend starts with demo readings so the dashboard works before hardware is connected.

## ESP32
Open `hardware/esp32/air_quality_esp32.ino` in Arduino IDE, install the ESP32 board package, set Wi-Fi and `API_URL`, then upload.

The firmware posts JSON to `POST /api/readings`.

## API payload
```json
{"pm25":35.2,"pm10":58.4,"temperature":29.1,"humidity":62.0,"co2":650}
```

See `docs/hardware.md` for wiring and sensor notes.
