# 🎓 Student Performance Predictor

An end-to-end Machine Learning web application that predicts a student's final grade (G3) using academic and personal information.

## 🚀 Live Demo

Coming Soon (Will be deployed on Render)

---

## 📌 Project Overview

This project predicts a student's final grade (G3) using a Machine Learning model trained on the UCI Student Performance Dataset.

The application provides a simple web interface where users can enter student information and receive a predicted final grade instantly.

---

## ✨ Features

- End-to-End Machine Learning Pipeline
- Data Ingestion
- Data Transformation using One-Hot Encoding
- Random Forest Regression Model
- Model Serialization using Joblib
- Flask Web Application
- Real-time Prediction
- Clean Project Structure

---

## 🛠️ Tech Stack

### Programming Language
- Python

### Libraries
- Pandas
- NumPy
- Scikit-learn
- Flask
- Joblib

### Machine Learning Model
- Random Forest Regressor

---

## 📂 Project Structure

```
Student-Performance-Predictor/
│
├── artifacts/
│   ├── model.pkl
│   ├── preprocessor.pkl
│   ├── train.csv
│   ├── test.csv
│   └── raw.csv
│
├── data/
│
├── notebooks/
│   ├── EDA.ipynb
│   └── Pipeline.ipynb
│
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   │
│   ├── pipeline/
│   │   └── predict_pipeline.py
│   │
│   ├── config.py
│   └── utils.py
│
├── templates/
│   └── index.html
│
├── app.py
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Machine Learning Workflow

### 1. Data Ingestion

- Reads the dataset
- Splits data into train and test sets

### 2. Data Transformation

- Separates features and target
- Applies One-Hot Encoding to categorical columns
- Saves preprocessing pipeline

### 3. Model Training

- Trains Random Forest Regressor
- Evaluates model performance
- Saves trained model (`model.pkl`)

### 4. Prediction

New Input

↓

Preprocessor

↓

Random Forest Model

↓

Predicted Grade (G3)

---

## 📊 Model Performance

| Metric | Value |
|---------|-------|
| MAE | **1.19** |
| RMSE | **1.99** |
| R² Score | **0.81** |

---

## ▶️ Installation

Clone the repository

```bash
git clone https://github.com/Mritunj-ya/Student-Performance-Predictor.git
```

Move inside the project

```bash
cd Student-Performance-Predictor
```

Create Virtual Environment

```bash
python -m venv .venv
```

Activate Environment (Windows)

```bash
.venv\Scripts\activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Run Flask Application

```bash
python app.py
```

Open in Browser

```
http://127.0.0.1:5000
```

---

## 📈 Future Improvements

- Better UI Design
- More Input Features
- Hyperparameter Tuning
- Cloud Deployment
- Docker Support
- CI/CD Pipeline

---

## 👨‍💻 Author

**Mritunjay Mahato**

GitHub:
https://github.com/Mritunj-ya