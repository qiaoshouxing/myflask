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
                'images': ['image/hair_product/p-1.jpg', 'image/hair_product/p-5.jpg'],
            },
            {
                'id': 2,
                'name': 'Premium Human Hair Toupee',
                'link': '',
                'images': ['image/hair_product/p-2.jpg', 'image/hair_product/p-6.jpg'],
                'label': {'type': 'new', 'text': 'New', 'position': 'left'}
            },
            {
                'id': 5,
                'name': 'Natural Lace Front Wig',
                'link': '',
                'images': ['image/hair_product/p-3.jpg', 'image/hair_product/p-5.jpg']
            },
            {
                'id': 6,
                'name': 'Invisible Hair System',
                'link': '',
                'images': ['image/hair_product/p-4.jpg', 'image/hair_product/p-6.jpg'],
                'label': {'type': 'new', 'text': 'New', 'position': 'left'}
            },
            {
                'id': 7,
                'name': 'Classic Full Lace Wig',
                'link': '',
                'images': ['image/hair_product/p-7.jpg', 'image/hair_product/p-8.jpg'],
                'label': {'type': 'hot', 'text': 'Hot', 'position': 'left'}
            },
            {
                'id': 8,
                'name': 'Premium Human Hair Toupee',
                'link': '',
                'images': ['image/hair_product/p-9.jpg', 'image/hair_product/p-10.jpg'],
                'label': {'type': 'new', 'text': 'New', 'position': 'left'}
            },
            {
                'id': 9,
                'name': 'Natural Looking Hair System',
                'link': '',
                'images': ['image/hair_product/p-11.jpg', 'image/hair_product/p-12.jpg']
            },
            {
                'id': 10,
                'name': 'Lace Front Men\'s Wig',
                'link': '',
                'images': ['image/hair_product/p-13.jpg', 'image/hair_product/p-14.jpg'],
                'label': {'type': 'sale', 'text': '-20%', 'position': 'left'}
            },
            {
                'id': 11,
                'name': 'Invisible Hair Replacement',
                'link': '',
                'images': ['image/hair_product/p-15.jpg', 'image/hair_product/p-16.jpg'],
                'label': {'type': 'new', 'text': 'New', 'position': 'left'}
            }
            #{
            #    'id': 5,
            #    'name': 'Tailored blazer jacket',
            #    'link': '',
            #    'images': ['image/product/p-9.jpg', 'image/product/p-10.jpg'],
            #    'label': {'type': 'new', 'text': 'New', 'position': 'left'}
            #},
            #{
            #    'id': 6,
            #    'name': 'Tailored blazer jacket',
            #    'link': '',
            #    'images': ['image/product/p-11.jpg', 'image/product/p-12.jpg'],
            #    'label': {'type': 'new', 'text': 'New', 'position': 'left'}
            #},
            #{
            #    'id': 7,
            #    'name': 'Tailored blazer jacket',
            #    'link': '',
            #    'images': ['image/product/p-13.jpg', 'image/product/p-14.jpg'],
            #    'label': {'type': 'new', 'text': 'New', 'position': 'left'}
            #},
            #{
            #    'id': 8,
            #    'name': 'Tailored blazer jacket',
            #    'link': '',
            #    'images': ['image/product/p-15.jpg', 'image/product/p-16.jpg'],
            #    'label': {'type': 'new', 'text': 'New', 'position': 'left'}
            #},
            #{
            #    'id': 9,
            #    'name': 'Tailored blazer jacket',
            #    'link': '',
            #    'images': ['image/product/p-17.jpg', 'image/product/p-18.jpg'],
            #    'label': {'type': 'new', 'text': 'New', 'position': 'left'}
            #},
            #{
            #    'id': 10,
            #    'name': 'Tailored blazer jacket',
            #    'link': '',
            #    'images': ['image/product/p-19.jpg', 'image/product/p-20.jpg'],
            #    'label': {'type': 'new', 'text': 'New', 'position': 'left'}
            #},
            #{
            #    'id': 11,
            #    'name': 'Tailored blazer jacket',
            #    'link': '',
            #    'images': ['image/product/p-21.jpg', 'image/product/p-22.jpg'],
            #    'label': {'type': 'new', 'text': 'New', 'position': 'left'}
            #},
            #{
            #    'id': 12,
            #    'name': 'Tailored blazer jacket',
            #    'link': '',
            #    'images': ['image/product/p-23.jpg', 'image/product/p-24.jpg'],
            #    'label': {'type': 'new', 'text': 'New', 'position': 'left'}
            #}
        ]
        return render_template('index.html', products=products)

    return app