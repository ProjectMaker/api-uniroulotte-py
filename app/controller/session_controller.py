from flask_restplus import Namespace, Resource
from flask import request, jsonify, make_response
from flask_jwt_extended import unset_jwt_cookies
from service.auth_service import AuthService
from util.exception import AuthSigninException

ns = Namespace('session', description='SESSION Operations')


@ns.route('/signin')
class SigninController(Resource):
    @ns.response(401, 'User not found')
    def post(self):
        json_data = request.get_json()
        email = json_data['email']
        password = json_data['password']
        try:
            return AuthService.signin(email, password)
        except AuthSigninException as err:
            ns.abort(401, err)


@ns.route('/signout')
class SignoutController(Resource):
    def post(self):
        response = make_response()
        unset_jwt_cookies(response)
        return response
