from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'CST Docker'


@app.route('/about')
def about():
    return "We're CST Developers from MCIT"

@app.route('/careers')
def careers():
    return "You can find the careers section here, about to be developed"