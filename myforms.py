from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,SelectField, FieldList,Form,FormField	
from wtforms.validators import DataRequired 


class HittingForm(Form):
    year = SelectField("Year:", choices=[('2019', '2019'), ('2020', '2020')], validators=[DataRequired()])
    types = SelectField("Category Type:", choices=[('Progressive', 'Progressive'), ('Per Game', 'Per Game')], validators=[DataRequired()])
    player = SelectField("Player:", choices=[("Player 1", "Player1"),("Player 2", "Player2")], validators=[DataRequired()])
    category = SelectField("Category:", choices=[(i,i) for i in range(100)], validators=[DataRequired()])

class Form1(FlaskForm):
    forms = FieldList( FormField(HittingForm), min_entries = 1 , max_entries = 10)
    submit = SubmitField()
