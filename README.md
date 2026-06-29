# Credict-card-Fraud-Detection1
Credit Card Fraud Detection is a machine learning and deep learning project designed to identify fraudulent credit card transactions and distinguish them from legitimate transactions.
Credit Card Fraud Detection
# Project Overview

Credit Card Fraud Detection is a Deep Learning-based system developed to identify fraudulent credit card transactions in real time. The project analyzes transaction data and predicts whether a transaction is legitimate or fraudulent. By learning patterns from historical transaction records, the model helps financial institutions reduce fraud-related losses and improve transaction security.

The system uses an Artificial Neural Network (ANN) trained on credit card transaction data containing features such as transaction amount, transaction time, and anonymized variables (V1–V28). The trained model can be integrated into a Streamlit web application for easy user interaction and fraud prediction.

# Objective
Detect fraudulent credit card transactions accurately.
Minimize financial losses caused by fraud.
Improve transaction security and customer trust.
Automate fraud detection using Deep Learning techniques.
Provide real-time fraud prediction through a user-friendly interface.
# Technologies Used
Programming Language: Python
Data Processing: Pandas, NumPy
Data Visualization: Matplotlib, Seaborn
Machine Learning Utilities: Scikit-learn
Deep Learning Framework: TensorFlow, Keras
Web Application: Streamlit
Model Serialization: Pickle
# Features
Data preprocessing and feature scaling.
Fraud and non-fraud transaction classification.
Deep Learning-based prediction using ANN.
Real-time transaction analysis.
User-friendly Streamlit interface.
High-performance fraud detection model.
Prediction probability score.
Model evaluation using multiple metrics.
Support for large transaction datasets.
Input Fields (Features Used)

# The model uses the following transaction features:

Time
V1
V2
V3
V4
V5
V6
V7
V8
V9
V10
V11
V12
V13
V14
V15
V16
V17
V18
V19
V20
V21
V22
V23
V24
V25
V26
V27
V28
Amount

# Target Variable:

Class (0 = Genuine Transaction, 1 = Fraudulent Transaction)
Model Workflow
Load credit card transaction dataset.
Perform data preprocessing.
Separate features and target variable.
Split data into training and testing sets.
Scale input features.
Build and train ANN model.
Evaluate model performance.
Save trained model.
Deploy using Streamlit.
Predict fraud status for new transactions.
Expected Output
Class = 0: Legitimate Transaction
Class = 1: Fraudulent Transaction

The system provides an instant prediction indicating whether the entered credit card transaction is likely to be fraudulent or genuine.

