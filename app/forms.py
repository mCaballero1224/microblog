"""
app/forms.py
"""

import sqlalchemy as sa
from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

from app import db
from app.models import User


class LoginForm(FlaskForm):
    """
    Class representing a User login form.
    """

    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Sign In")


class RegistrationForm(FlaskForm):
    """
    Class representing a User registration form.
    """

    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    password2 = PasswordField(
        "Repeat Password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Register")

    def validate_username(self, username):
        """
        Checks for duplicate usernames in the database.
        A ValidationError is raised if the username is already taken.
        """
        user = db.session.scalar(sa.select(User).where(User.username == username.data))
        if user is not None:
            raise ValidationError("Please use a different username.")

    def validate_email(self, email):
        """
        Checks for duplicate emails in the database.
        A ValidationError is raised if the email is already in use by
        another user.
        """
        user = db.session.scalar(sa.select(User).where(User.email == email.data))
        if user is not None:
            raise ValidationError("Please use a different email address.")
