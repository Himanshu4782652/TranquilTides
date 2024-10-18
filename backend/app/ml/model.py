import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
import os


# Load your dataset (customize this with your actual dataset path or data source)
def load_data(file_path):
    return pd.read_csv(file_path)


# Prepare data for model training
def prepare_data(df):
    # Select the relevant features and target variable
    X = df[["anxiety", "depression", "schizophrenia", "bipolar_disorder"]]  # Features
    y = df[
        "eating_disorder"
    ]  # Target variable (you can replace this with any mental health metric)

    # Split data into training and testing sets
    return train_test_split(X, y, test_size=0.2, random_state=42)


# Train the model (Linear Regression in this case, can be replaced with other models)
def train_model(X_train, y_train):
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model


# Save the trained model as a .pkl file in the models folder
def save_model(model, filename="trained_model.pkl"):
    model_path = os.path.join("models", filename)
    with open(model_path, "wb") as f:
        pickle.dump(model, f)
    print(f"Model saved as {model_path}")


if __name__ == "__main__":
    # Example: Load dataset and train the model (customize as needed)
    data_file = "path_to_your_data.csv"  # Replace with your actual data file
    df = load_data(data_file)

    # Prepare the data for training
    X_train, X_test, y_train, y_test = prepare_data(df)

    # Train the model
    model = train_model(X_train, y_train)

    # Save the trained model in the 'models' folder
    save_model(model)
