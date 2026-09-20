from sklearn.ensemble import RandomForestRegressor
import numpy as np

# Small baseline model for a working demo. Retrain later with your collected dataset.
_X = np.array([[15,35,25,45],[30,60,28,55],[50,90,30,65],[75,130,32,75],[100,180,34,80]])
_y = np.array([20,35,55,78,105])
_model = RandomForestRegressor(n_estimators=80, random_state=42).fit(_X, _y)

def predict(r):
    x = np.array([[r["pm25"], r["pm10"], r["temperature"], r["humidity"]]])
    pred = float(_model.predict(x)[0])
    return {
        "next_pm25": round(pred, 1),
        "horizon": "next reading",
        "model": "Random Forest baseline"
    }
