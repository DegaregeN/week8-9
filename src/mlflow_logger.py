
import mlflow
import mlflow.sklearn

def log_model(model, model_name):
    mlflow.sklearn.log_model(model, model_name)