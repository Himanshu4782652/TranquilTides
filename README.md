# Tranquil Tides - Mental Health Self-Assessment and Wellness Dashboard

## Overview

**Tranquil Tides** is a web-based application designed to help users monitor their mental health and overall well-being. By providing users with self-assessment tools, machine learning-based mood predictions, and personalized relaxation techniques, the platform empowers users to gain deeper insights into their mental state and track their progress over time.

The app is targeted at adults and older adults, focusing on mental health awareness and improvement through a user-friendly dashboard, dynamic data visualization, and predictive analytics.

---

## Key Features

- **Self-Assessment Tool**: Users can fill out detailed mental health assessments, entering data related to anxiety, depression, and other mental health factors.
- **Mood Prediction**: Using a trained machine learning model, the app predicts potential mental states and provides insights on the likelihood of specific disorders.
- **User Dashboard**: A personalized dashboard where users can view their mood trends, predictions, and insights through interactive charts and graphs.
- **Relaxation Techniques**: Personalized suggestions for relaxation exercises based on the user's mental health assessment and prediction results.
- **User Authentication**: Secure sign-up and login functionalities allowing users to create profiles, update personal information, and access their assessment history.
- **Database Management**: Stores user assessments, profile information, and mood predictions securely using SQLite.
- **Error Handling**: Custom error pages (e.g., 404 error) to improve user experience.

---

## Project Structure

```
TranquilTides/
├── backend/
│   ├── app/
│   │   ├── __init__.py              # Flask app initialization
│   │   ├── models.py                # SQLAlchemy database models
│   │   ├── routes.py                # Routes for handling requests and responses
│   │   ├── forms.py                 # WTForms for user authentication and assessments
│   │   ├── utils.py                 # Utility functions for loading the ML model and more
│   │   ├── predict.py               # ML model prediction logic
│   │   ├── ml/
│   │   │   ├── model.py             # Machine learning model setup and configuration
│   │   │   └── predict.py           # Code to load and use the trained model
│   │   ├── templates/               # HTML templates for the frontend
│   │   └── static/                  # Static files (CSS, JavaScript, images)
│   ├── config.py                    # Configuration for Flask app
│   ├── manage.py                    # Command-line manager to run the app and other commands
│   ├── requirements.txt             # Python dependencies
├── database/
│   ├── migrations/                  # Database migration files (if using Flask-Migrate)
│   └── seeds.sql                    # Optional: Initial database seed data
├── models/
│   └── trained_model.pkl            # Trained machine learning model for mood prediction
├── mood_prediction_model.ipynb       # Jupyter notebook for training the ML model
├── README.md                        # Project documentation (this file)
├── .gitignore                       # Files to ignore in Git version control
├── .gitattributes                   # Git attributes for line endings and more
```

---

## Technology Stack

### **Frontend**
- **HTML5/CSS3**: For building the structure and styling of web pages.
- **JavaScript**: For client-side interactivity.
- **Bootstrap**: To ensure responsive design and quick styling.
  
### **Backend**
- **Python**: Core programming language.
- **Flask**: Web framework for building backend APIs and routes.
- **SQLAlchemy**: ORM for interacting with the SQLite database.
- **Flask-WTF**: Form handling and validation.

### **Machine Learning**
- **scikit-learn**: Used for training the machine learning model.
- **Pandas, NumPy**: For data manipulation and preparation.
- **Pickle**: To save and load the trained machine learning model.

### **Database**
- **SQLite**: Lightweight database for storing user data and assessment history.

---

## Installation and Setup

### Step 1: Clone the Repository
First, clone the repository to your local machine:
```bash
git clone https://github.com/username/TranquilTides.git
cd TranquilTides
```

### Step 2: Create a Virtual Environment
Set up a virtual environment to manage your Python dependencies:
```bash
python3 -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

### Step 3: Install the Dependencies
Install the required Python packages using `pip`:
```bash
pip install -r requirements.txt
```

### Step 4: Set Up Environment Variables
Create a `.env` file in the root directory and define your environment variables:
```bash
# .env file example
SECRET_KEY=your_secret_key
DATABASE_URL=sqlite:///database.db
```

### Step 5: Initialize the Database
Initialize the SQLite database and apply migrations:
```bash
flask db init
flask db migrate
flask db upgrade
```

### Step 6: Run the Application
Finally, run the Flask development server:
```bash
python manage.py run
```

Open your browser and navigate to `http://127.0.0.1:5000/` to view the application.

---

## Machine Learning Model

The **Mood Prediction Model** is built using **scikit-learn** and trained on mental health-related datasets. It predicts the likelihood of mood disorders such as anxiety and depression based on user inputs.

- **Model Training**: The model was trained in a Jupyter notebook (`mood_prediction_model.ipynb`) and saved as a pickle file (`models/trained_model.pkl`).
- **Prediction**: The `predict.py` file loads this model to make predictions in real-time based on user data entered in the assessment form.

---

## Project Features

### **User Authentication**
Users can sign up and log in to the application to access personalized features such as assessment history, profile updates, and more.

### **Dynamic Dashboard**
The **Dashboard** page provides visual representations of user data using interactive charts and graphs (powered by libraries such as Plotly). Users can track their mental health trends over time.

### **Mood Assessment**
The **Assessment** page allows users to input their mental health data, which is processed and analyzed by the machine learning model to give predictions.

### **Relaxation Techniques**
Based on the predictions, the app suggests relaxation techniques to help users manage their mental health more effectively.

---

## Contribution

Contributions are welcome! If you'd like to contribute to the project, follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Contact

For any questions or support, feel free to reach out via the **Contact** page on the app or through email: [your-email@example.com](mailto:your-email@example.com).

---

This completes the **README.md** file. Let me know if you need any further adjustments!