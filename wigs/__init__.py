import os

from config import config
from flask import Flask, render_template
#from flask_bootstrap import Bootstrap

def create_app(config_name = None):
    app = Flask(__name__, static_folder='assets', static_url_path='/assets')

    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'default')
    app.config.from_object(config[config_name])

    # a simple page that says hello
    @app.route('/')
    def index():
        return render_template('hello_world.html')

    return app