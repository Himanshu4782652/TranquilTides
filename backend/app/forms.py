from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange


class LoginForm(FlaskForm):
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=4, max=20)]
    )
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")


class SignupForm(FlaskForm):
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=4, max=20)]
    )
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Sign Up")


class MentalHealthAssessmentForm(FlaskForm):
    anxiety = IntegerField(
        "Anxiety Level (0-10)", validators=[DataRequired(), NumberRange(min=0, max=10)]
    )
    depression = IntegerField(
        "Depression Level (0-10)",
        validators=[DataRequired(), NumberRange(min=0, max=10)],
    )
    schizophrenia = IntegerField(
        "Schizophrenia Disorders Level (0-10)",
        validators=[DataRequired(), NumberRange(min=0, max=10)],
    )
    bipolar = IntegerField(
        "Bipolar Disorder Level (0-10)",
        validators=[DataRequired(), NumberRange(min=0, max=10)],
    )
    submit = SubmitField("Submit Assessment")
