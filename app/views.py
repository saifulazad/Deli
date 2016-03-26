from flask import render_template, request
from wtforms.ext.sqlalchemy.orm import model_form
from app import app ,api
from  app import models


from flask_restful import Resource




class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/hi')


@app.route('/')
@app.route('/index')
def index():
    return render_template('home.html');


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html');


@app.route('/signup')
def signup():

    return render_template('signup.html');


@app.route('/single_products', methods=['GET', 'POST'])
def single_products():
    return render_template('single_product.html');


@app.route('/all_products', methods=['GET', 'POST'])
def all_products():
    return render_template('all_product.html');


@app.route('/collections', methods=['GET', 'POST'])
def collections():
    return render_template('collection_page.html');
