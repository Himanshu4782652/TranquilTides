from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from .forms import LoginForm, SignupForm, MentalHealthAssessmentForm
from .models import User, Assessment, db
from .predict import predict_mood
from werkzeug.security import generate_password_hash, check_password_hash

main = Blueprint("main", __name__)


# Home page
@main.route("/")
def index():
    return render_template("index.html")


# User Dashboard (Protected Route)
@main.route("/dashboard")
@login_required
def dashboard():
    assessments = Assessment.query.filter_by(user_id=current_user.id).all()
    return render_template("dashboard.html", assessments=assessments)


# Login page
@main.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for("main.dashboard"))
        flash("Invalid username or password")
    return render_template("login.html", form=form)


# Signup page
@main.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash("Account created successfully! Please log in.")
        return redirect(url_for("main.login"))
    return render_template("signup.html", form=form)


# Mental Health Assessment
@main.route("/assessment", methods=["GET", "POST"])
@login_required
def assessment():
    form = MentalHealthAssessmentForm()
    if form.validate_on_submit():
        result = predict_mood(
            form.anxiety.data,
            form.depression.data,
            form.schizophrenia.data,
            form.bipolar.data,
        )
        new_assessment = Assessment(
            anxiety=form.anxiety.data,
            depression=form.depression.data,
            schizophrenia=form.schizophrenia.data,
            bipolar=form.bipolar.data,
            result=result,
            user_id=current_user.id,
        )
        db.session.add(new_assessment)
        db.session.commit()
        return redirect(url_for("main.dashboard"))
    return render_template("assessment.html", form=form)


# Logout
@main.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))
