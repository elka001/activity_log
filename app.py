from flask import Flask, request
from flask_restx import Api, Resource, abort
from models.activity import activity_ns, activity_model
from models.user import user_ns, user_model
from utils import load_data, get_next_id, save_and_respond, find_item_by_id, save_data

# ENDPOINTS
# /users
# /users/<int:id>
# /users/<int:user_id>/activities
# /activities
# /activities/<int:id>
# /activities/<int:activity_id>/users

USERS_FILE = 'data/users.json'
ACTIVITIES_FILE = 'data/activities.json'

app = Flask(__name__)
api = Api(app,
          version='1.0',
          title='Activity Log API',
          description='A simple API for managing and logging your daily activities!')

# INITIAL DATA
users = load_data(USERS_FILE)
activities = load_data(ACTIVITIES_FILE)

# REGISTER NAMESPACES WITH THE MAIN API
api.add_namespace(user_ns)
api.add_namespace(activity_ns)


# USER OPERATIONS
@user_ns.route('/')
class UserList(Resource):
    @user_ns.doc('list_users')
    @user_ns.marshal_list_with(user_model)
    def get(self):
        """List all users"""
        current_users = load_data(USERS_FILE)
        return current_users

    @user_ns.doc('create_user')
    @user_ns.expect(user_model, validate=True)
    @user_ns.marshal_with(user_model, code=201)
    def post(self):
        """Create a new user"""
        current_users = load_data(USERS_FILE)
        new_user_data = request.json
        if any(user['email'] == new_user_data['email'] for user in current_users):
            abort(400, 'A user with that email already exists.')
        new_user_data['id'] = get_next_id(current_users)
        current_users.append(new_user_data)
        save_data(USERS_FILE, current_users)
        return new_user_data, 201, {'Location': f'/users/{new_user_data["id"]}'}


@user_ns.route('/<int:id>')
@user_ns.param('id', 'The user identifier')
@user_ns.response(404, 'User not found.')
class UserService(Resource):
    @user_ns.doc('get_user')
    @user_ns.marshal_with(user_model)
    def get(self, id):
        """Display a user's information by their ID"""
        current_users = load_data(USERS_FILE)
        user = find_item_by_id(current_users, id)
        if user is None:
            abort(404, "User not found.")
        return user

    @user_ns.doc('update_user')
    @user_ns.expect(user_model, validate=True)
    @user_ns.marshal_with(user_model)
    def put(self, id):
        """Update a user's information by their ID"""
        current_users = load_data(USERS_FILE)
        user = find_item_by_id(current_users, id)
        if not user:
            abort(404, "User not found.")
        user.update(request.json)
        save_data(USERS_FILE, current_users)
        return user, 200, {'Location': f'/users/{id}'}

    @user_ns.doc('delete_user')
    @user_ns.response(204, 'User successfully deleted.')
    def delete(self, id):
        """Delete a user by their ID"""
        current_users = load_data(USERS_FILE)
        user_exists = any(user['id'] == id for user in current_users)
        if not user_exists:
            abort(404, "User not found.")
        current_users = [user for user in current_users if user['id'] != id]
        return save_and_respond(USERS_FILE, current_users, {}, 204)


@user_ns.route('/<int:user_id>/activities')
@user_ns.param('user_id', 'The user identifier for filtering activities')
@user_ns.response(404, 'User not found.')
class UserActivities(Resource):
    @activity_ns.marshal_list_with(activity_model)
    def get(self, user_id):
        """Show all activities for a specific user"""
        current_activities = load_data(ACTIVITIES_FILE)
        user_activities = [activity for activity in current_activities if activity['user_id'] == user_id]
        if not user_activities:
            abort(404, 'User not found or no activities for this user.')
        return user_activities


# ACTIVITY OPERATIONS
@activity_ns.route('/')
class ActivityList(Resource):
    @activity_ns.doc('list_activities')
    @activity_ns.marshal_list_with(activity_model)
    def get(self):
        """List all activities"""
        current_activities = load_data(ACTIVITIES_FILE)
        return current_activities

    @activity_ns.doc('create_activity')
    @activity_ns.expect(activity_model, validate=True)
    @activity_ns.marshal_with(activity_model, code=201)
    def post(self):
        """Create a new activity"""
        current_activities = load_data(ACTIVITIES_FILE)
        new_activity_data = request.json
        new_activity_data['id'] = get_next_id(current_activities)
        current_activities.append(new_activity_data)
        save_data(ACTIVITIES_FILE, current_activities)
        return new_activity_data, 201, {'Location': f'/activities/{new_activity_data["id"]}'}


@activity_ns.route('/<int:id>')
@activity_ns.param('id', 'The activity identifier')
@activity_ns.response(404, 'Activity not found.')
class ActivityService(Resource):
    @activity_ns.doc('get_activity')
    @activity_ns.marshal_with(activity_model)
    def get(self, id):
        """Display an activity's details by its ID"""
        current_activities = load_data(ACTIVITIES_FILE)
        activity = find_item_by_id(current_activities, id)
        if activity is None:
            abort(404, "Activity not found.")
        return activity

    @activity_ns.doc('update_activity')
    @activity_ns.expect(activity_model, validate=True)
    @activity_ns.marshal_with(activity_model)
    def put(self, id):
        """Update an activity's details by its ID"""
        current_activities = load_data(ACTIVITIES_FILE)
        activity = find_item_by_id(current_activities, id)
        if not activity:
            abort(404, "Activity not found.")
        for key in request.json:
            if key != 'id':
                activity[key] = request.json[key]
        save_data(ACTIVITIES_FILE, current_activities)
        return activity, 200, {'Location': f'/activities/{id}'}

    @activity_ns.doc('delete_activity')
    @activity_ns.response(204, 'Activity successfully deleted.')
    def delete(self, id):
        """Delete an activity by its ID"""
        current_activities = load_data(ACTIVITIES_FILE)
        activity_exists = any(activity['id'] == id for activity in current_activities)
        if not activity_exists:
            abort(404, "Activity not found.")
        current_activities = [activity for activity in current_activities if activity['id'] != id]
        return save_and_respond(ACTIVITIES_FILE, current_activities, {}, 204)


@activity_ns.route('/<int:activity_id>/users')
@activity_ns.param('activity_id', 'The activity identifier')
@activity_ns.response(404, 'Activity not found.')
class ActivityUsers(Resource):
    @activity_ns.doc('list_users_by_activity')
    @activity_ns.marshal_list_with(user_model)
    def get(self, activity_id):
        """List all users that did a specific activity"""
        current_activities = load_data(ACTIVITIES_FILE)
        current_users = load_data(USERS_FILE)
        activity = find_item_by_id(current_activities, activity_id)
        if activity is None:
            abort(404, "Activity not found.")
        users_in_activity = [user for user in current_users if user['id'] == activity['user_id']]
        return users_in_activity


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
