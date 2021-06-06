from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'CST Docker'


@app.route('/check')
def check_route():
    return 'Checking Routesr'

@app.route('/about')
def about():
    return "We're CST Developers from MCIT"