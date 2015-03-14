import flask
from flask_oauth import OAuth
from flask import request
from datetime import datetime
from gcm import GCM
from gcm.gcm import GCMException
from settings import *
from decorator import *
from flask_cors import CORS
from bot_response import *
from decorator import login_required, is_loggedin

app = flask.Flask(__name__)
cors = CORS(app, resources={r"/message": {"origins": ""}})
app.secret_key = 'justsomerandomstring001'
app.config['SESSION_TYPE'] = 'filesystem'

oauth = OAuth()

fb_credentials = {
    "app_id":"435021593331381",
    "app_secret": "89eaf7ceb2d806c5a48224c88973dbe0",
}

facebook = oauth.remote_app('facebook',
    base_url='https://graph.facebook.com/',
    request_token_url=None,
    access_token_url='/oauth/access_token',
    authorize_url='https://www.facebook.com/dialog/oauth',
    consumer_key=fb_credentials["app_id"],
    consumer_secret=fb_credentials["app_secret"],
    request_token_params={'scope': 'email'}
)

@app.route('/login/facebook')
def login_facebook():
    return facebook.authorize(callback=url_for('facebook_authorized',
        next=request.args.get('next', None),
        _external=True))

@app.route('/login/facebook/authorized')
@facebook.authorized_handler
def facebook_authorized(resp):
    next_url = request.args.get('next') or url_for('chat')
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    session['oauth_token'] = (resp['access_token'], '')
    me = facebook.get('/me')
    return redirect(next_url)

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


@facebook.tokengetter
def get_facebook_oauth_token():
    return session.get('oauth_token')


@app.route('/')
def login():
    currTime = datetime.now().strftime("%H-%M")
    hour, min = currTime.split("-")
    if int(hour) == 4:# and min == 36:
        gmc_send()
    return flask.render_template('login.html')

@app.route('/chat')
def chat():
    return flask.render_template('chat.html')


@app.route('/message', methods=['GET'])
@crossdomain(origin='*')
def message_input():
    msg = request.args.get('msg')
    if len(msg)<3:
        return "??"
        
    return sentiment(msg)

@app.route('/logout')
def logout():
    session['oauth_token'] = (None,)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
