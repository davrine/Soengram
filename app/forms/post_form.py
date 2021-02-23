from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import SubmitField, TextAreaField
from wtforms.validators import DataRequired

from app.utils.file import ALLOWED_EXTENSIONS


class CreatePostForm(FlaskForm):
    post_image = FileField(
        'Image',
        render_kw={'style': 'height: auto'},
        validators=[
            FileRequired(message='Must attach a photo'),
            FileAllowed(ALLOWED_EXTENSIONS, 'File type not allowed')
        ]
    )

    description = TextAreaField(
        'Caption',
        render_kw={'rows': 5, 'style': 'height: auto'},
        validators=[
            DataRequired(message='Caption required')
        ]
    )

    submit = SubmitField("Create a Post")
