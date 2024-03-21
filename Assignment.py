from flask_wtf import Form
from flask import Flask, render_template
from wtforms import StringField, PasswordField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'blank'

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('Example.html')

if __name__ == '__main__':
    app.run(debug=True)