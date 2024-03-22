from flask_wtf import FlaskForm
from flask import Flask, render_template, redirect, url_for
from wtforms import StringField, TextAreaField, SelectField, RadioField
from wtforms.validators import InputRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'blank'

class Questionnaire(FlaskForm):
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
def feedback():
    form = Questionnaire()
    if form.validate_on_submit():
        with open('feedback.txt', 'a') as file:
            file.write(f"Name: {form.name.data}\n")
            file.write(f"Course: {form.course.data}\n")
            file.write(f"Short-form Answer: {form.short_answer.data}\n")
            file.write(f"Long-form Answer: {form.long_answer.data}\n")
            file.write(f"Overall Satisfaction: {form.satisfaction.data}\n")
            file.write(f"Would recommend: {form.recommend.data}\n")
            file.write(f"Suggestions for Improvement: {form.improvements.data}\n")
            file.write('\n')
        return redirect(url_for('thank_you'))
    return render_template('Example.html', form=form)

@app.route('/thank-you')
def thank_you():
    return 'Thank you for your feedback!'

if __name__ == '__main__':
    app.run(debug=True)