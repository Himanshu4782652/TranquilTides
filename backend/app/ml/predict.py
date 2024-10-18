import pickle
import numpy as np
import os


# Load the trained model from the models folder
def load_model(model_path="models/trained_model.pkl"):
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found at {model_path}")

    with open(model_path, "rb") as f:
        model = pickle.load(f)
    return model


# Make predictions using the loaded model and input features
def make_prediction(anxiety, depression, schizophrenia, bipolar_disorder):
    # Prepare input features as a numpy array (reshaping for the model)
    features = np.array([[anxiety, depression, schizophrenia, bipolar_disorder]])

    # Load the trained model
    model = load_model()

    # Use the model to make a prediction
    prediction = model.predict(features)

    # Return the prediction result
    return prediction[0]


# Example usage (can be used for testing the script independently)
if __name__ == "__main__":
    # Example user input values (replace with actual form inputs)
    anxiety = 3.5
    depression = 4.0
    schizophrenia = 2.0
    bipolar_disorder = 3.0

    # Get the prediction
    predicted_value = make_prediction(
        anxiety, depression, schizophrenia, bipolar_disorder
    )
    print(f"Predicted Outcome: {predicted_value}")
