# 🚲 Yulu Bike Demand Prediction

This project is a Machine Learning-based system that predicts hourly bike rental demand using environmental and time-related features.

## 📌 Project Overview
The goal of this project is to analyze bike-sharing data and build a predictive model that can estimate demand under different conditions such as weather, time, and season.

## ⚙️ Features
- Data preprocessing and feature engineering
- Model training using:
  - Linear Regression
  - Random Forest Regressor
- Model evaluation using:
  - MAE (Mean Absolute Error)
  - RMSE (Root Mean Squared Error)
  - R² Score
- Interactive UI built using Streamlit

## 🧠 Best Model
Random Forest Regressor performed the best with an R² Score of approximately 0.94, indicating strong prediction accuracy.

## 💻 How to Run the Project

1. Install required libraries:
2. Run the Streamlit app: streamlit run app.py
3. Open in browser: http://localhost:8501

⚠️ Note

The trained model file (best_model.pkl) is not uploaded due to GitHub size limitations. It can be generated locally by running the training notebook and saving the trained model.

🚀 Output
Predicts bike rental demand based on user inputs
Displays demand level: Low, Medium, or High
Provides a practical interface for testing the machine learning model
📊 Technologies Used
Python
Pandas
NumPy
Scikit-learn
Streamlit
Joblib
