import mlflow
import mlflow.sklearn
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report
)
import os
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

# Ignore all warnings
warnings.filterwarnings("ignore")

# Define the mlruns path
mlruns_path = os.path.abspath("C:\\Users\\1221\\Desktop\\Acadamy AIM 2\\week8-9\\mlflow\\runs")

# Convert Windows path to a file URI
mlruns_uri = "file:///" + mlruns_path.replace("\\", "/")

# Ensure the directory exists
os.makedirs(mlruns_path, exist_ok=True)

# Set the MLflow tracking URI
mlflow.set_tracking_uri(mlruns_uri)

# Load dataset
df = pd.read_csv('C:\\Users\\1221\\Desktop\\Acadamy AIM 2\\week8-9\\data\\creditcard.csv')

# Feature and target separation
X = df.drop('Class', axis=1)
y = df['Class']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Set up MLflow experiment
mlflow.set_experiment("fraud_detection_experiment")

# Train and log the model with MLflow
with mlflow.start_run():
    # Train the model
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)

    # Calculate evaluation metrics
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    # Display the metrics
    print(f"Accuracy: {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")
    print(f"F1 Score: {f1:.4f}")

    # Log metrics to MLflow
    mlflow.log_metric("accuracy", accuracy)
    mlflow.log_metric("precision", precision)
    mlflow.log_metric("recall", recall)
    mlflow.log_metric("f1_score", f1)

    # Input example for logging
    input_example = X_train.iloc[:1]

    # Log the model with MLflow
    mlflow.sklearn.log_model(
        sk_model=model,
        artifact_path="RandomForest",
        input_example=input_example
    )

    # Generate confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    cm_df = pd.DataFrame(cm, index=["Actual 0", "Actual 1"], columns=["Predicted 0", "Predicted 1"])

    # Save the confusion matrix as an image
    plt.figure(figsize=(6, 4))
    sns.heatmap(cm_df, annot=True, cmap='Blues', fmt='d')
    plt.title("Confusion Matrix")
    plt.savefig("confusion_matrix.png")

    # Log confusion matrix as artifact
    mlflow.log_artifact("confusion_matrix.png")

    # Generate and save evaluation report as a CSV
    report = classification_report(y_test, y_pred, output_dict=True)
    report_df = pd.DataFrame(report).transpose()
    report_df.to_csv("evaluation_report.csv", index=True)

    # Log the evaluation report as an artifact
    mlflow.log_artifact("evaluation_report.csv")

print(f"MLruns saved at: {mlruns_path}")
