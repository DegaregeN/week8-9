import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import os

import warnings

# Ignore all warnings
warnings.filterwarnings("ignore")

# Define the mlruns path
mlruns_path = os.path.abspath("C:\\Users\\1221\\Desktop\\Acadamy AIM 2\\week8-9\\mlflow\\runs")

# Convert Windows path to a file URI
# Replacing backslashes manually
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
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Evaluate the model
    accuracy = model.score(X_test, y_test)
    print(f"Logged model with accuracy: {accuracy:.4f}")

    # Input example for logging
    input_example = X_train.iloc[:1]

    # Log the model with input example
    mlflow.sklearn.log_model(
        sk_model=model,
        artifact_path="RandomForest",
        input_example=input_example
    )

    # Log accuracy metric
    mlflow.log_metric("accuracy", accuracy)

print(f"MLruns saved at: {mlruns_path}")
