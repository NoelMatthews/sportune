from email.mime import application
from flask import Flask

application = Flask(__name__)

@application.route('/', methods=['POST','GET'])
def index():
    return 'running normally'