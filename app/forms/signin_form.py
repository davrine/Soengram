from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

from app.models import User


class SigninForm(FlaskForm):
    email = StringField(
        "Email",
        validators=[
            DataRequired(message="Enter an email address."),
            Email(message="Enter a valid email address.")
        ]
    )

    password = PasswordField(
        "Password",
        validators=[
            DataRequired(message="Enter a password."),
        ]
    )

    sign_in = SubmitField("Sign In")

    def validate(self) -> bool:
        if not super().validate():
            return False

        user = User.get_by_email(self.email.data)

        if not User.is_authenticated(user, self.password.data):
            self.email.errors.append('Incorrect username and/or password.')
            return False

        return True
