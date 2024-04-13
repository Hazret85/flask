from flask import render_template, redirect, url_for
from flask_login import login_user, login_required, logout_user
from app import app, db, login_manager
from models import User, Product
from forms import LoginForm, RegisterForm, ProductForm


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    error = None
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            return redirect(url_for('add'))
        else:
            error = 'Неверные учетные данные. Пожалуйста, попробуйте еще раз или зарегистрируйтесь.'
    return render_template('login.html', form=form, error=error)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/shop')
def shop():
    products = Product.query.all()
    return render_template('shop.html', products=products)


@app.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = ProductForm()
    if form.validate_on_submit():
        new_product = Product(name=form.name.data, description=form.description.data, price=form.price.data)
        db.session.add(new_product)
        db.session.commit()
        return redirect(url_for('shop'))
    return render_template('add.html', form=form)


@app.route('/delete/<id>', methods=['POST'])
def delete(id):
    product_delete = Product.query.get_or_404(id)
    db.session.delete(product_delete)
    db.session.commit()
    return redirect(url_for('shop'))
