import random
from flask import render_template, request
from wtforms.ext.sqlalchemy.orm import model_form
from app import app
from  app import models
@app.route('/')
@app.route('/index')
def index():
    return render_template('home.html');


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html');

@app.route('/products', methods=['GET', 'POST'])
def products():
    res = models.Product.query.order_by(models.Product.price)[0:50]
    return render_template('products.html', product = res[random.randrange(0, 40)]);

@app.route('/signup')
def signup():

    MyForm = model_form(models.User, models.UserForm)

    form = MyForm(request.form)
    model = models.User()
    if request.method == 'POST' and form.validate_on_submit():


         form.populate_obj(model)

        # model.put()
        # flash("MyModel updated")
        # return redirect(url_for("index"))
    return render_template('signup.html', form=form);