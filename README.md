# 🏡 House Price Prediction — Case Study 1 (Agent Mira)

### **Author:** Satyam Kumar 
### **Role:** Data Science Applicant  

---

## 🎯 Objective

The goal of this case study is to develop a machine learning model to predict house prices based on real-estate property features.  
The solution includes:

- Data preprocessing  
- Exploratory Data Analysis (EDA)  
- Model experimentation  
- Best model selection  
- API development for prediction  
- Multi-core processing support  
- Docker-based deployment readiness  

---

## 📂 Project Structure
Above
---

## 🧹 1. Data Preprocessing

Performed using **`src/preprocess.py`**:

- Handle missing values  
- Encode categorical variables  
- Parse and extract date components  
- Create engineered feature: `Property_Age`  
- Save cleaned dataset to:



artifacts/processed_data.csv


---

## 📊 2. Exploratory Data Analysis (EDA)

Located in:



notebooks/01_eda.ipynb


Includes:

- Price distribution  
- Correlation heatmap  
- Outlier analysis  
- Feature relationships  
- Summary statistics  

---

## 🤖 3. Model Training

Located in:



notebooks/02_model_experiments.ipynb
src/train.py


Models tested:

| Model              | RMSE      | R²     |
|-------------------|-----------|--------|
| Linear Regression | 153,449   | 0.51   |
| Random Forest     | 89,889    | 0.83   |
| **XGBoost**       | **87,992** | **0.84** |

XGBoost achieved the best performance.

The final trained model is saved at:

models/final_model.pkl

Training metrics saved at:

artifacts/metrics.json

--
## ⚙️ 4. API for Predictions

The prediction API is built using **FastAPI**.

### ▶ Running the API

uvicorn api.app:app --reload --port 8000

### ▶ API Documentation

Visit:

http://127.0.0.1:8000/docs

### ▶ Example POST Request

```json
{
  "Location": 3,
  "Size": 2000,
  "Bedrooms": 3,
  "Bathrooms": 2,
  "Year_Built": 2015,
  "Condition": 1,
  "Type": 2,
  "Sold_Year": 2025,
  "Sold_Month": 1
}


The API returns:

{
  "predicted_price": 548414.94
}

🐳 5. Docker Support (Deployment Ready)

Dockerfile located at:

deployment/Dockerfile

▶ Build image:
docker build -t house-price-app .

▶ Run container:
docker run -p 8000:8000 house-price-app

🎤 6. Presentation
A complete presentation summarizing:
EDA
Feature engineering
Model results

Deployment
Located at:
presentation/CaseStudy1_Presentation.pptx

✅ Conclusion
This project demonstrates a complete ML lifecycle:

Data cleaning
EDA
Model training

API deployment
Production readiness via Docker
The solution is modular, scalable, and suitable for a real-world ML deployment pipeline.
