import pickle
import os
import numpy as np


# Load the trained model
def load_model():
    model_path = os.path.join(os.getcwd(), "models", "trained_model.pkl")
    with open(model_path, "rb") as f:
        model = pickle.load(f)
    return model


def predict_mood(anxiety, depression, schizophrenia, bipolar):
    model = load_model()
    features = np.array([[anxiety, depression, schizophrenia, bipolar]])
    prediction = model.predict(features)

    # Convert prediction result to a meaningful string
    if prediction[0] == 0:
        return "Low likelihood of an eating disorder"
    elif prediction[0] == 1:
        return "Moderate likelihood of an eating disorder"
    else:
        return "High likelihood of an eating disorder"
