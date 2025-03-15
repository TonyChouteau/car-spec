import traceback
from flask import Blueprint, request, jsonify

from api.constants import ApiConstants
from api.core.login import LoginHandler

api = Blueprint('api', __name__)


@api.post('/login')
def login():
    try:
        username = request.form.get("username")
        password = request.form.get("password")
        if username is None or username == "" or password is None or password == "":
            return jsonify({
                "error": "Missing login or password"
            }), 400

        LoginHandler.authenticate(login, password)

    except Exception as e:
        print(traceback.format_exc())
        return jsonify({
            "error": ApiConstants.ERROR_500
        }), 500
