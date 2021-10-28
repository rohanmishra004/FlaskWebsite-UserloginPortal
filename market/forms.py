from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField , SubmitField
from wtforms.validators import DataRequired, Length, EqualTo,Email, ValidationError
from market.models import User

class RegisterForm(FlaskForm):

    def validate_username(self , username_to_check): #FlaskForm class will check any function with validate_ {fieldname} here - 'username' to validate it 
        user = User.query.filter_by(username = username_to_check.data).first()
        if user:
            raise ValidationError('Username already exist ! Please change it to something else')

    def validate_email_address(self,email_address_to_check):
        email_address = User.query.filter_by(email_address = email_address_to_check.data).first()
        if email_address:
            raise ValidationError("Email already exists , Kindly change it ")    

    username = StringField(label='User Name:', validators=[Length(min=2, max = 30)])
    email_address = StringField(label='Email Address:',validators=[Email()])
    password1 = PasswordField(label='Password: ',validators=[Length(min=6)]) 
    password2 = PasswordField(label='Confirm Password:' ,validators=[EqualTo('password1')])
    submit = SubmitField(label='Create Account')


class LoginForm(FlaskForm):
    username = StringField(label='User Name:' , validators=[DataRequired()])
    password = PasswordField(label='password:' , validators=[DataRequired()])
    submit = SubmitField(label='Sign In')
