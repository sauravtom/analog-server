import flask
from datetime import datetime

app = flask.Flask(__name__)
app.secret_key = 'justsomerandomstring001'
app.config['SESSION_TYPE'] = 'filesystem'


@app.route('/')
def index():
    #print datetime.now().ctime().
    return flask.render_template('homepage.html')

@app.route('/api')
def foo():
    return "hello world"


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
