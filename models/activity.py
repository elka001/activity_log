# MODEL DEFINITIONS FOR SWAGGER DOCUMENTATION
from flask_restx import fields
from app import activity_ns

activity_model = activity_ns.model('Activity', {
    'id': fields.Integer(readonly=True, description='The unique identifier of an activity.'),
    'name': fields.String(required=True, description='The name of an activity.'),
    'description': fields.String(required=True, description='The description of an activity.'),
    'duration': fields.String(required=True, description='The duration of an activity.'),
    'date': fields.String(required=True, description='The date of an activity.'),
    'user_id': fields.Integer(required=True, description='The ID of a user this activity belongs to.')
})
