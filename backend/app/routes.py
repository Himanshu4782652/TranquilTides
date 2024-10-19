from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User, Assessment, db
from .forms import LoginForm, SignupForm, MentalHealthAssessmentForm
from .predict import predict_mood

# Define the main blueprint
main = Blueprint("main", __name__)


# Home page
@main.route("/")
def index():
    return render_template("index.html")


# Dashboard page (requires login)
@main.route("/dashboard")
@login_required
def dashboard():
    # Query the database for assessments for the logged-in user
    assessments = Assessment.query.filter_by(user_id=current_user.id).all()
    return render_template("dashboard.html", assessments=assessments)


# About page
@main.route("/about")
def about():
    return render_template("about.html")


# Contact page
@main.route("/contact")
def contact():
    return render_template("contact.html")


# Profile page (requires login)
@main.route("/profile")
@login_required
def profile():
    return render_template("profile.html")


# Mental Health Assessment form (requires login)
@main.route("/assessment", methods=["GET", "POST"])
@login_required
def assessment():
    form = MentalHealthAssessmentForm()
    if form.validate_on_submit():
        # Predict mood based on the form inputs
        result = predict_mood(
            form.anxiety.data,
            form.depression.data,
            form.schizophrenia.data,
            form.bipolar.data,
        )
        # Save the assessment to the database
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
        flash("Your assessment has been saved!", "success")
        return redirect(url_for("main.dashboard"))
    return render_template("assessment.html", form=form)


# Signup page
@main.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash("Account created successfully! Please log in.", "success")
        return redirect(url_for("main.login"))
    return render_template("signup.html", form=form)


# Login page
@main.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash("Logged in successfully.", "success")
            return redirect(url_for("main.dashboard"))
        flash("Invalid username or password", "danger")
    return render_template("login.html", form=form)


# Logout route (requires login)
@main.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "info")
    return redirect(url_for("main.index"))


# View assessment results (requires login)
@main.route("/results/<int:id>")
@login_required
def results(id):
    assessment = Assessment.query.get_or_404(id)
    if assessment.user_id != current_user.id:
        flash("You do not have permission to view this assessment.", "danger")
        return redirect(url_for("main.dashboard"))
    return render_template("results.html", assessment=assessment)


# Update Profile (requires login)
@main.route("/profile/update", methods=["GET", "POST"])
@login_required
def update_profile():
    if request.method == "POST":
        new_username = request.form.get("username")
        current_user.username = new_username
        db.session.commit()
        flash("Profile updated successfully!", "success")
        return redirect(url_for("main.profile"))
    return render_template("update_profile.html")
