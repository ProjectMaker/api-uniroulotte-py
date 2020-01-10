from flask_restplus import Model, fields

serializer = Model('User', {
    'id': fields.String(required=True, description='user id'),
    'email': fields.String(required=True, description='user email address')
})

