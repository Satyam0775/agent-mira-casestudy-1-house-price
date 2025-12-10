import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor

# FIXED IMPORTS — must use src.<module>
from src.preprocess import preprocess_data
from src.model_utils import save_model, save_metrics
from src.config import RANDOM_STATE, TARGET_COLUMN


def train_models():
    print("Processing dataset...")
    df = preprocess_data()

    # Split features and target
    X = df.drop(TARGET_COLUMN, axis=1)
    y = df[TARGET_COLUMN]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=RANDOM_STATE
    )

    # Models to test
    models = {
        "Linear Regression": LinearRegression(),
        "Random Forest": RandomForestRegressor(n_jobs=-1, random_state=RANDOM_STATE),
        "XGBoost": XGBRegressor(
            n_estimators=300,
            learning_rate=0.1,
            max_depth=6,
            subsample=0.8,
            colsample_bytree=0.8,
            n_jobs=-1,
            random_state=RANDOM_STATE
        )
    }

    best_model = None
    best_rmse = float("inf")
    results = {}

    for name, model in models.items():
        print(f"\nTraining → {name}")
        model.fit(X_train, y_train)

        preds = model.predict(X_test)

        # Manual RMSE for older sklearn
        rmse = mean_squared_error(y_test, preds) ** 0.5
        r2 = r2_score(y_test, preds)

        results[name] = {"RMSE": rmse, "R2": r2}
        print(f"{name} | RMSE: {rmse:.2f} | R2: {r2:.4f}")

        if rmse < best_rmse:
            best_rmse = rmse
            best_model = model

    # Save best model + performance metrics
    save_model(best_model)
    save_metrics(results)

    print("\n✔ Training complete.")
    print("✔ Best model saved successfully.")


if __name__ == "__main__":
    train_models()
