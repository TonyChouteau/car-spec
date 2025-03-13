from flask import Blueprint, request

api = Blueprint('api', __name__)


@api.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Validate username and password (this is just a basic example)
    user = mongo.db.users.find_one({'username': username})
    if user and check_password_hash(user['password'], password):
        session['username'] = username  # Store the username in session
        return redirect(url_for('garage'))  # Redirect to the garage page
    else:
        return render_template('login.html', error="Invalid username or password.")
