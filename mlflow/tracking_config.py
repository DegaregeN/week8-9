
import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load dataset
df = pd.read_csv('../data/creditcard.csv')

# Feature and target separation
X = df.drop('Class', axis=1)
y = df['Class']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Set up MLflow experiment
mlflow.set_experiment("fraud_detection_experiment")

# Train model and log
with mlflow.start_run():
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Log model and metrics
    mlflow.sklearn.log_model(model, "RandomForest")
    accuracy = model.score(X_test, y_test)
    mlflow.log_metric("accuracy", accuracy)
    print(f"Logged model with accuracy: {accuracy:.4f}")