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
                'name': 'Classic Full Lace Wig',
                'link': '',
                'images': ['image/hair_product/p-1.jpg']
            },
            {
                'id': 2,
                'name': 'Premium Human Hair Toupee',
                'link': '',
                'images': ['image/hair_product/p-2.jpg']
            },
            {
                'id': 3,
                'name': 'Natural Lace Front Wig',
                'link': '',
                'images': ['image/hair_product/p-3.jpg']
            },
            {
                'id': 4,
                'name': 'Invisible Hair System',
                'link': '',
                'images': ['image/hair_product/p-4.jpg']
            },
            {
                'id': 5,
                'name': 'Natural Looking Hair System',
                'link': '',
                'images': ['image/hair_product/p-5.jpg']
            },
            {
                'id': 6,
                'name': 'Lace Front Men\'s Wig',
                'link': '',
                'images': ['image/hair_product/p-6.jpg']
            },
            {
                'id': 7,
                'name': 'Invisible Hair Replacement',
                'link': '',
                'images': ['image/hair_product/p-7.jpg']
            },
            {
                'id': 8,
                'name': 'Classic Full Lace Wig',
                'link': '',
                'images': ['image/hair_product/p-8.jpg']
            },
            {
                'id': 9,
                'name': 'Premium Human Hair Toupee',
                'link': '',
                'images': ['image/hair_product/p-9.jpg']
            },
            {
                'id': 10,
                'name': 'Natural Lace Front Wig',
                'link': '',
                'images': ['image/hair_product/p-10.jpg']
            },
            {
                'id': 11,
                'name': 'Invisible Hair System',
                'link': '',
                'images': ['image/hair_product/p-11.jpg']
            },
            {
                'id': 12,
                'name': 'Natural Looking Hair System',
                'link': '',
                'images': ['image/hair_product/p-12.jpg']
            },
            {
                'id': 13,
                'name': 'Lace Front Men\'s Wig',
                'link': '',
                'images': ['image/hair_product/p-13.jpg']
            },
            {
                'id': 14,
                'name': 'Invisible Hair Replacement',
                'link': '',
                'images': ['image/hair_product/p-14.jpg']
            },
            {
                'id': 15,
                'name': 'Classic Full Lace Wig',
                'link': '',
                'images': ['image/hair_product/p-15.jpg'],
                'label': {'type': 'new', 'text': 'New', 'position': 'left'}
            },
            {
                'id': 16,
                'name': 'Premium Human Hair Toupee',
                'link': '',
                'images': ['image/hair_product/p-16.jpg'],
                'label': {'type': 'new', 'text': 'New', 'position': 'left'}
            },
            {
                'id': 17,
                'name': 'Natural Lace Front Wig',
                'link': '',
                'images': ['image/hair_product/p-17.jpg'],
                'label': {'type': 'new', 'text': 'New', 'position': 'left'}
            },
            {
                'id': 18,
                'name': 'Invisible Hair System',
                'link': '',
                'images': ['image/hair_product/p-18.jpg'],
                'label': {'type': 'new', 'text': 'New', 'position': 'left'}
            },
            {
                'id': 19,
                'name': 'Natural Looking Hair System',
                'link': '',
                'images': ['image/hair_product/p-19.jpg'],
                'label': {'type': 'new', 'text': 'New', 'position': 'left'}
            }
        ]
        return render_template('index.html', products=products)

    return app