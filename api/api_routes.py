import traceback

from flask import Blueprint, request, jsonify
from api.constants import ApiConstants
from api.login import login_handler

api = Blueprint('api', __name__)


@api.route('/login', methods=['POST'])
def login():
    try:
        response = login(request)

        if response is None:
            return ApiConstants.ERROR_NONE
        if response.get("error") is not None:
            return response

        return response
    except Exception as e:
        print(traceback.format_exc())
        return ApiConstants.ERROR_500
