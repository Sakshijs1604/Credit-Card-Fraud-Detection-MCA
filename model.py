import os
import pandas as pd
import joblib
import warnings

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

warnings.filterwarnings("ignore")


# ==========================================
# FILE PATH
# ==========================================

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

DATASET_FILE = os.path.join(
    BASE_DIR,
    "creditcard.csv"
)

MODEL_FILE = os.path.join(
    BASE_DIR,
    "fraud_model_6.pkl"
)

SCALER_FILE = os.path.join(
    BASE_DIR,
    "scaler_6.pkl"
)


# ==========================================
# ONLY 6 FEATURES
# ==========================================

FEATURES = [
    "Time",
    "V1",
    "V2",
    "V3",
    "V4",
    "Amount"
]

TARGET = "Class"


# ==========================================
# LOAD DATASET
# ==========================================

print("\n--- Loading Dataset ---")

data = pd.read_csv(
    DATASET_FILE
)

print(
    "Dataset loaded successfully!"
)

print(
    "Total transactions:",
    len(data)
)


# ==========================================
# SELECT ONLY 6 FEATURES
# ==========================================

X = data[
    FEATURES
]

y = data[
    TARGET
]


# ==========================================
# REMOVE MISSING VALUES
# ==========================================

X = X.fillna(
    X.median()
)


# ==========================================
# TRAIN TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(

    X,
    y,

    test_size=0.20,

    random_state=42,

    stratify=y
)


# ==========================================
# STANDARD SCALING
# ==========================================

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(
    X_train
)

X_test_scaled = scaler.transform(
    X_test
)


# ==========================================
# TRAIN MODEL
# ==========================================

print("\n--- Training Model ---")

model = LogisticRegression(

    max_iter=2000,

    class_weight="balanced",

    random_state=42
)

model.fit(
    X_train_scaled,
    y_train
)

print(
    "Model trained successfully!"
)


# ==========================================
# MODEL PREDICTION
# ==========================================

y_pred = model.predict(
    X_test_scaled
)


# ==========================================
# MODEL EVALUATION
# ==========================================

print("\n--- Model Evaluation ---")

accuracy = accuracy_score(
    y_test,
    y_pred
)

precision = precision_score(
    y_test,
    y_pred,
    zero_division=0
)

recall = recall_score(
    y_test,
    y_pred,
    zero_division=0
)

f1 = f1_score(
    y_test,
    y_pred,
    zero_division=0
)


print(
    "Accuracy:",
    round(accuracy * 100, 2),
    "%"
)

print(
    "Precision:",
    round(precision * 100, 2),
    "%"
)

print(
    "Recall:",
    round(recall * 100, 2),
    "%"
)

print(
    "F1 Score:",
    round(f1 * 100, 2),
    "%"
)


# ==========================================
# CONFUSION MATRIX
# ==========================================

cm = confusion_matrix(
    y_test,
    y_pred
)

print(
    "\nConfusion Matrix:"
)

print(cm)


# ==========================================
# SAVE MODEL
# ==========================================

joblib.dump(
    model,
    MODEL_FILE
)

joblib.dump(
    scaler,
    SCALER_FILE
)

print(
    "\nModel saved successfully!"
)
