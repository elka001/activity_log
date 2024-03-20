# MODEL DEFINITIONS FOR SWAGGER DOCUMENTATION
from flask_restx import fields, Namespace

user_ns = Namespace('users', description='Operations related to users:')

user_model = user_ns.model('User', {
    'id': fields.Integer(readonly=True, description='The unique identifier of a user.'),
    'username': fields.String(required=True, description='The username of a user.'),
    'email': fields.String(required=True, description='The email address of a user.')
})
