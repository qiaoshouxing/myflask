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
        products = [
            {
                'id': 1,
                'name': 'Pleated skater skirt',
                'link': '',
                'images': ['image/product/p-1.jpg', 'image/product/p-2.jpg']
            },
            {
                'id': 2,
                'name': 'Tailored blazer jacket',
                'link': '',
                'images': ['image/product/p-3.jpg', 'image/product/p-4.jpg'],
                'label': {'type': 'new', 'text': 'New', 'position': 'left'}
            },
            {
                'id': 3,
                'name': 'Girls floral ruffle top',
                'link': '',
                'images': ['image/product/p-5.jpg', 'image/product/p-6.jpg']
            },
            {
                'id': 4,
                'name': 'Tailored blazer jacket',
                'link': '',
                'images': ['image/product/p-7.jpg', 'image/product/p-8.jpg'],
                'label': {'type': 'new', 'text': 'New', 'position': 'left'}
            },
            {
                'id': 5,
                'name': 'Tailored blazer jacket',
                'link': '',
                'images': ['image/product/p-9.jpg', 'image/product/p-10.jpg'],
                'label': {'type': 'new', 'text': 'New', 'position': 'left'}
            },
            {
                'id': 6,
                'name': 'Tailored blazer jacket',
                'link': '',
                'images': ['image/product/p-11.jpg', 'image/product/p-12.jpg'],
                'label': {'type': 'new', 'text': 'New', 'position': 'left'}
            },
            {
                'id': 7,
                'name': 'Tailored blazer jacket',
                'link': '',
                'images': ['image/product/p-13.jpg', 'image/product/p-14.jpg'],
                'label': {'type': 'new', 'text': 'New', 'position': 'left'}
            },
            {
                'id': 8,
                'name': 'Tailored blazer jacket',
                'link': '',
                'images': ['image/product/p-15.jpg', 'image/product/p-16.jpg'],
                'label': {'type': 'new', 'text': 'New', 'position': 'left'}
            },
            {
                'id': 9,
                'name': 'Tailored blazer jacket',
                'link': '',
                'images': ['image/product/p-17.jpg', 'image/product/p-18.jpg'],
                'label': {'type': 'new', 'text': 'New', 'position': 'left'}
            },
            {
                'id': 10,
                'name': 'Tailored blazer jacket',
                'link': '',
                'images': ['image/product/p-19.jpg', 'image/product/p-20.jpg'],
                'label': {'type': 'new', 'text': 'New', 'position': 'left'}
            },
            {
                'id': 11,
                'name': 'Tailored blazer jacket',
                'link': '',
                'images': ['image/product/p-21.jpg', 'image/product/p-22.jpg'],
                'label': {'type': 'new', 'text': 'New', 'position': 'left'}
            },
            {
                'id': 12,
                'name': 'Tailored blazer jacket',
                'link': '',
                'images': ['image/product/p-23.jpg', 'image/product/p-24.jpg'],
                'label': {'type': 'new', 'text': 'New', 'position': 'left'}
            }
        ]
        return render_template('index.html', products=products)

    return app