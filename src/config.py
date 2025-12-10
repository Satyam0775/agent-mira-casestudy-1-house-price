import os

# ---------------------------------------------------------
# BASE_DIR = Project Root (Task/)
# ---------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Example: C:/Users/satya/Downloads/Casestudy 1/Task

# ---------------------------------------------------------
# DATA PATHS
# ---------------------------------------------------------
RAW_DATA_PATH = os.path.join(BASE_DIR, "data", "raw", "Case Study 1 Data.xlsx")
PROCESSED_DATA_PATH = os.path.join(BASE_DIR, "artifacts", "processed_data.csv")

# ---------------------------------------------------------
# MODEL & METRICS PATHS
# ---------------------------------------------------------
MODEL_PATH = os.path.join(BASE_DIR, "models", "final_model.pkl")
METRICS_PATH = os.path.join(BASE_DIR, "artifacts", "metrics.json")
LOG_PATH = os.path.join(BASE_DIR, "artifacts", "model_logs.txt")

# ---------------------------------------------------------
# TRAINING PARAMETERS
# ---------------------------------------------------------
TARGET_COLUMN = "Price"
RANDOM_STATE = 42
