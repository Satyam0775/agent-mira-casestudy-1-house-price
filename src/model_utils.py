import json
import joblib

# FIXED IMPORT — MUST point to src.config
from src.config import MODEL_PATH, METRICS_PATH


def save_model(model):
    """Save the trained model to disk."""
    joblib.dump(model, MODEL_PATH)
    print(f"✔ Model saved at: {MODEL_PATH}")


def load_model():
    """Load the trained ML model."""
    return joblib.load(MODEL_PATH)


def save_metrics(metrics: dict):
    """Save training metrics to JSON file."""
    with open(METRICS_PATH, "w") as f:
        json.dump(metrics, f, indent=4)
    print(f"✔ Metrics saved at: {METRICS_PATH}")
