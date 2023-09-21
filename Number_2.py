import flask
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Flask!'

@app.route('/Sharry')
def sharry():
    return 'Hello , Phaji'

if __name__ == '__main__':
    app.run(debug=True)