from flask import Blueprint, render_template, redirect, url_for

from api.auth import require_authentication

app = Blueprint('app', __name__, template_folder='templates', static_folder='static')


@app.get('/login')
def login():
    return render_template('login.html')


@app.route('/')
@require_authentication(redirect_to_login=True)
def index():
    return render_template('home.html')


@app.route('/garage')
@require_authentication(redirect_to_login=True)
def garage():
    return render_template('garage.html')


@app.route('/users')
@require_authentication(redirect_to_login=True)
def users():
    return render_template('users.html')


@app.route('/shop')
@require_authentication(redirect_to_login=True)
def shop():
    return render_template('shop.html')


@app.route('/reference')
@require_authentication(redirect_to_login=True)
def reference():
    return render_template('reference.html')


@app.route('/parts')
@require_authentication(redirect_to_login=True)
def parts():
    return render_template('parts.html')


@app.route('/entretien')
@require_authentication(redirect_to_login=True)
def entretien():
    return render_template('entretien.html')


@app.route('/trackday')
@require_authentication(redirect_to_login=True)
def trackday():
    return render_template('trackday.html')
