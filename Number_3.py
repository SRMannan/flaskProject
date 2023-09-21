import flask
from flask import Flask , render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    name = "Sharry"
    return render_template('index.html', name=name)


@app.route('/Sharry')
def sharry():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)