from flask import request, jsonify, redirect, url_for
import functools

from api.core.login import LoginHandler


def require_authentication(redirect_to_login=False):
    def handle_error_return(error):
        if redirect_to_login:
            return redirect(url_for("app.login"))
        else:
            return jsonify({
                "error": error.get("message")
            }), error.get("status")

    def decorator(f):
        @functools.wraps(f)
        def decorated_function(*args, **kwargs):
            token = request.headers.get('Authorization')
            if token is None:
                return handle_error_return({
                    "error": "Token missing",
                    "status": 400
                })
            if "Bearer" not in token:
                return handle_error_return({
                    "error": "Bad token",
                    "status": 400
                })

            token = token.replace("Bearer ", "")
            if LoginHandler().authenticate_with_token(token=token):
                return f(*args, **kwargs)

            return handle_error_return({
                "error": "Invalid token",
                "status": 401
            })

        return decorated_function
    return decorator
