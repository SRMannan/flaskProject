import flask
from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = "***"  ##dont push password in github 


class LoginForm(FlaskForm):
    username = StringField("username" , validators=[DataRequired()])
    password = PasswordField("password" , validators=[DataRequired()])
    submit = SubmitField("Submit")



@app.route('/HELLO')
def hello_world():
    return 'Hello, Flask!'


@app.route('/')
def idx():
    return render_template('idx.html')


@app.route('/form', methods=['GET', 'POST'])
def form():
    username = None
    password = None
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        form.username.data = ''
        form.password.data = ''

    return render_template("form.html", form=form, username=username , password = password)


if __name__ == '__main__':
    app.run(debug=True)
