from flask import request
from flask_restplus import Namespace, Resource
from flask_jwt_extended import jwt_required

from model.devis_model import Devis
from serializer.devis_serializer import serializer
from service.devis_service import DevisService
ns = Namespace('devis', description='DEVIS Operations')


@ns.route('/')
class DevisController(Resource):
    @jwt_required
    @ns.doc('list_devis')
    @ns.marshal_with(serializer)
    def get(self):
        users = []
        for user in Devis.objects.limit(50).order_by('-created_at'):
            users.append(user)

        return users

    @ns.doc('create_devis')
    def post(self):
        DevisService.create(**request.get_json())
        return {}
