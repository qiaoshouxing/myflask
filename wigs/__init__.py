import os

from flask import Flask, render_template
#from flask_bootstrap import Bootstrap

def create_app(config_name = None):
    app = Flask(__name__)

    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'default')
    from config import config
    app.config.from_object(config[config_name])
    app.config.update()

    # a simple page that says hello
    @app.route('/')
    def index():
        return render_template('index.html')

    return app