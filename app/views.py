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

@app.route('/single_products', methods=['GET', 'POST'])
def single_products():
    return render_template('single_product.html');

@app.route('/all_products', methods=['GET', 'POST'])
def all_products():
    return render_template('all_product.html');

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