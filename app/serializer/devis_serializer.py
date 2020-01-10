from flask_restplus import Model, fields

serializer = Model('Devis', {
    'id': fields.String(required=True, description='devis id'),
    'email': fields.String(required=True, description='devis user email'),
    'phone_number': fields.String(required=False, description='devis user phone number '),
    'firstname': fields.String(required=True, description='user firstname'),
    'lastname': fields.String(required=True, description='user lastname'),
    'price': fields.String(required=True, description='devis price'),
    'detail': fields.Raw(),
    'created_at': fields.Date(required=True, description='devis created at')
})

