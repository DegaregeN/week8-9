from flask import Flask, request, jsonify
import pickle
import os

app = Flask(__name__)

# Load trained model
model_path = 'C:/Users/1221/Desktop/Acadamy AIM 2/week8-9/mlflow/models/model.pkl'

# Check if the model file exists
if not os.path.isfile(model_path):
    raise FileNotFoundError(f"Model file not found at: {model_path}")

# Load the model
with open(model_path, 'rb') as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    
    # Ensure 'features' are present in the data
    if 'features' not in data:
        return jsonify({'error': 'No features provided'}), 400
    
    prediction = model.predict([data['features']])
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


