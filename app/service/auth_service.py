from flask import jsonify
from flask_jwt_extended import (
    set_access_cookies, set_refresh_cookies,
    create_access_token, create_refresh_token
)

from model.user_model import User
from util.exception import AuthSigninException


class AuthService(object):
    @staticmethod
    def signin(email, password):
        user = User.objects(email=email).first()
        if user is None or user.verify_password(password) is False:
            raise AuthSigninException("User {} doesn't exist".format(email))
        if user is not None and user.verify_password(password):
            access_token = create_access_token(identity=email)
            refresh_token = create_refresh_token(identity=email)

            resp = jsonify({'Authorization': access_token})
            set_access_cookies(resp, access_token)
            set_refresh_cookies(resp, refresh_token)
            return resp
