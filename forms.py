from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, PasswordField, RadioField, DateField, SelectField
from wtforms.validators import DataRequired, InputRequired, Length, Email, EqualTo

class AddCommentForm(FlaskForm):
    name = StringField('თქვენი სახელი', validators=[InputRequired()])
    comment = StringField('დაამატეთ კომენტარი', validators=[InputRequired()])
    submit = SubmitField('დამატება' )
    



class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=20)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=6)])
    repeat_password = PasswordField('Repeat Password', validators=[InputRequired(), EqualTo('password')])
    gender = RadioField("Gender", choices=[('male', 'Male'), ('female', 'Female')], validators=[InputRequired()])
    birthday = DateField('Date of Birth', format='%Y-%m-%d', validators=[InputRequired()])
    country = SelectField('Country', choices=[('georgia', 'Georgia'), ('usa', 'USA')], validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired(), Email()])

    submit = SubmitField('Register')