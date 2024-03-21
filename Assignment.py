from flask_wtf import Form
from flask import Flask, render_template
from wtforms import StringField, TextAreaField, SelectField, RadioField, SubmitField
from wtforms.validators import InputRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'blank'

class Questionnaire(Form):
    name = StringField('name', validators=[InputRequired()])
    course = StringField('course', validators=[InputRequired()])
    short_answer = TextAreaField('short-answer', validators=[InputRequired()])
    long_answer = TextAreaField('long-answer', validators=[InputRequired()])
    satisfaction = SelectField('Overall Satisfaction', choices=[
        ('', 'Select Satisfaction Level'),
        ('very-satisfied', 'Very Satisfied'),
        ('satisfied', 'Satisfied'),
        ('neutral', 'Neutral'),
        ('unsatisfied', 'Unsatisfied'),
        ('very-unsatisfied', 'Very Unsatisfied')
    ], validators=[InputRequired()])
    recommend = RadioField('Would you recommend this course to others?', choices=[
        ('yes', 'Yes'),
        ('no', 'No')
    ], validators=[InputRequired()])
    improvements = TextAreaField('Suggestions for Improvement', validators=[InputRequired()])


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('Example.html')

if __name__ == '__main__':
    app.run(debug=True)