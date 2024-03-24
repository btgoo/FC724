from flask_wtf import FlaskForm
from flask import Flask, render_template, redirect, url_for
from wtforms import StringField, TextAreaField, SelectField, RadioField
from wtforms.validators import InputRequired

# Create a Flask application instance
app = Flask(__name__)

# Set a secret key for the application (needed for form security)
app.config['SECRET_KEY'] = 'blank'

# Define a form class using FlaskForm as a base class
class Questionnaire(FlaskForm):
    # Define form fields and validators
    name = StringField('name', validators=[InputRequired()]) #StringField since it is a short answer
    course = StringField('course', validators=[InputRequired()])
    short_answer = TextAreaField('short-answer', validators=[InputRequired()]) #TextArea since it is long answer
    long_answer = TextAreaField('long-answer', validators=[InputRequired()])
    satisfaction = SelectField('Overall Satisfaction', choices=[
        ('', 'Select Satisfaction Level'),
        ('very-satisfied', 'Very Satisfied'),
        ('satisfied', 'Satisfied'),
        ('neutral', 'Neutral'),
        ('unsatisfied', 'Unsatisfied'),
        ('very-unsatisfied', 'Very Unsatisfied')
    ], validators=[InputRequired()]) # SelectField since it is drop down
    recommend = RadioField('Would you recommend this course to others?', choices=[
        ('yes', 'Yes'),
        ('no', 'No') # RadioField since it is a multiple choice question
    ], validators=[InputRequired()])
    improvements = TextAreaField('Suggestions for Improvement', validators=[InputRequired()])

# Define a route for the homepage ('/') that handles GET and POST requests
@app.route('/', methods=['GET', 'POST'])
def feedback():
    # Create an instance of the Questionnaire form class
    form = Questionnaire()
    # If the form is submitted and validated
    if form.validate_on_submit():
        # Open 'feedback.txt' file in append mode and write form data
        with open('feedback.txt', 'a') as file:
            file.write(f"Name: {form.name.data}\n")
            file.write(f"Course: {form.course.data}\n")
            file.write(f"Short-form Answer: {form.short_answer.data}\n")
            file.write(f"Long-form Answer: {form.long_answer.data}\n")
            file.write(f"Overall Satisfaction: {form.satisfaction.data}\n")
            file.write(f"Would recommend: {form.recommend.data}\n")
            file.write(f"Suggestions for Improvement: {form.improvements.data}\n")
            file.write('\n')  # Add a newline for separation
        # Redirect to the 'thank_you' route
        return redirect(url_for('thank_you'))
    # Render the 'Example.html' template with the form instance
    return render_template('Example.html', form=form)

# Define a route for the 'thank-you' page
@app.route('/thank-you')
def thank_you():
    return 'Thank you for your feedback!'

# Run the application if the script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
