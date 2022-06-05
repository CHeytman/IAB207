from flask import *

mybp = Blueprint('main',__name__)

@mybp.route('/')
def index():
    return render_template('index.html')

@mybp.route('/event')
def event():
    return render_template('event.html')

@mybp.route('/event_create')
def event_create():
    return render_template('event_create.html')

@mybp.route('/booking')
def booking():
    return render_template('booking.html')

