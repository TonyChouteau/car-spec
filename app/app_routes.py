from flask import Blueprint, render_template, redirect, url_for

app = Blueprint('app', __name__, template_folder='templates', static_folder='static')


@app.route('/')
def index():
    return redirect(url_for("app.garage"))


@app.route('/')
@app.route('/garage')
def garage():
    return render_template('garage.html')


@app.route('/users')
def users():
    return render_template('users.html')


@app.route('/shop')
def shop():
    return render_template('shop.html')


@app.route('/reference')
def reference():
    return render_template('reference.html')


@app.route('/parts')
def parts():
    return render_template('parts.html')


@app.route('/entretien')
def entretien():
    return render_template('entretien.html')


@app.route('/trackday')
def trackday():
    return render_template('trackday.html')
