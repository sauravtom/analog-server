import flask
from flask import request
from redis import Redis
from datetime import datetime
from gcm import GCM
from gcm.gcm import GCMException
from settings import *
from decorator import *
from flask_cors import CORS
from bot_response import *

app = flask.Flask(__name__)
cors = CORS(app, resources={r"/message": {"origins": ""}})
app.secret_key = 'justsomerandomstring001'
app.config['SESSION_TYPE'] = 'filesystem'


def gmc_send():
    gcm = GCM(publicAPIKey)
    msg = 'Sample message'
    data = {'msg': msg}

    ids = '12'
    try:
        response = gcm.plaintext_request(registration_id=ids, data=data)
        print response, "AASDASDS"
        print 'Your message was sent to devices'
    except GCMException as gcme:
        print gcme.message
    #except:
    #    print "SOME ERROR"


@app.route('/')
def index():
    currTime = datetime.now().strftime("%H-%M")
    hour, min = currTime.split("-")
    if int(hour) == 4:# and min == 36:
        gmc_send()
    return flask.render_template('homepage.html')


@app.route('/message', methods=['GET'])
@crossdomain(origin='*')
def message_input():
    msg = request.args.get('msg')
    print msg
    return sentiment(msg)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
