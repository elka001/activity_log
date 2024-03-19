# Activity Log API

This API was created to manage and log daily activities for users. 

It provides endpoints for creating, reading, updating, and deleting users and their associated activities.

### Samlpe data

User:
```
    {
        "id": 1,
        "username": "user1",
        "email": "user1@example.com"
    }
```
Activity:
```
    {
        "id": 1,
        "name": "name1",
        "description": "description1",
        "duration": "00:00",
        "date": "YYYY-MM-DD",
        "user_id": 1
    }
```
## How to get started

1. Download & install ```Docker Desktop```. Run it
2. Open CMD and clone this repository with ```git clone```. Or copy source code through ```Code``` -> ```Download ZIP```
3. Run the following commands inside the directory to start the server:
```
cd activity_log
docker-compose up
```
4. To access UI, navigate to ```http://localhost:5000``` in your browser of choice
5. Now you should see the ```Activity Log API``` and be able to interact with it

## RESTful API commands

### CREATE

**Create User**: ```curl -X POST http://localhost:5000/users/ -H "Content-Type: application/json" -d "{\"username\": \"newuser\", \"email\": \"newuser@example.com\"}"```

**Create Activity**: ```curl -X POST http://localhost:5000/activities/ -H "Content-Type: application/json" -d "{\"name\": \"name1\", \"description\": \"description1\", \"duration\": \"00:00\", \"date\": \"YYYY-MM-DD\", \"user_id\":  {user_id}}"```. Replace {user_id} with a new ID of the user you want to create. Same applies to all the information.

### READ

**Read Users**: ```curl -X GET http://localhost:5000/users/```

**Read Specific User**: ```curl -X GET http://localhost:5000/users/{user_id}```. Replace {user_id} with the actual ID of the user you want to retrieve.

**Read a Specific User's Activities**: ```curl -X GET http://localhost:5000/users/{user_id}/activities```. Replace {user_id} with the ID of the user whose activities you want to retrieve.

**Read Activities**: ```curl -X GET http://localhost:5000/activities/```

**Read Specific Activity**: ```curl -X GET http://localhost:5000/activities/{activity_id}```. Replace {activity_id} with the ID of the activity you want to retrieve.

**Read Users Participating in a Specific Activity**: ```curl -X GET http://localhost:5000/activities/{activity_id}/users```. Replace {activity_id} with the ID of the activity for which you want to list participating users.

### UPDATE

**Update User**: ```curl -X PUT http://localhost:5000/users/{user_id} -H "Content-Type: application/json" -d "{\"username\": \"updateduser\", \"email\": \"updateduser@example.com\"}"```. Replace {user_id} with the actual ID of the user you want to update.

**Update Activity**: ```curl -X PUT http://localhost:5000/activities/{activity_id} -H "Content-Type: application/json" -d "{\"name\": \"name1\", \"description\": \"description1\", \"duration\": \"00:00\", \"date\": \"YYYY-MM-DD\", \"user_id\": 1}"```. Replace {activity_id} with the ID of the activity you want to update.

### DELETE

**Delete User**: ```curl -X DELETE http://localhost:5000/users/{user_id}```. Replace {user_id} with the ID of the user you want to delete.

**Delete Activity**: ```curl -X DELETE http://localhost:5000/activities/{activity_id}```. Replace {activity_id} with the ID of the activity you want to delete.















