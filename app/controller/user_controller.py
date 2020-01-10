from flask_restplus import Namespace, Resource
from flask_jwt_extended import jwt_required

from model.user_model import User
from serializer.user_serializer import serializer

ns = Namespace('user', description='USER Operations')

@ns.route('/')
class UserController(Resource):
    @jwt_required
    @ns.marshal_with(serializer)
    def get(self):
        users = []
        for user in User.objects.all():
            users.append(user)

        return users
