import os

from config import config
from flask import Flask, render_template
from flask_bootstrap import Bootstrap4

def create_app(config_name = None):
    app = Flask(__name__, static_folder='assets', static_url_path='/assets')

    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'default')
    app.config.from_object(config[config_name])

    bootstrap = Bootstrap4(app)

    @app.route('/')
    def index():
        return render_template('index.html')

    return app