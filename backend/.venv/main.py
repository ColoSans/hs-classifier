from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "HS-Classifier API v0.1"}

@app.post("/classify")
def classify(payload: dict):
    # Aquí iría tu lógica real; de momento un dummy:
    return {"hs_code": "000000", "confidence": 0.5}
