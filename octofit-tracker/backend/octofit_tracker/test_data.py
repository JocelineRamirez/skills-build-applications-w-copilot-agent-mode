from bson import ObjectId
from datetime import timedelta

test_data = {
    "users": [
        {"_id": ObjectId(), "username": "student1", "email": "student1@example.com", "password": "password1"},
        {"_id": ObjectId(), "username": "student2", "email": "student2@example.com", "password": "password2"},
        {"_id": ObjectId(), "username": "student3", "email": "student3@example.com", "password": "password3"},
    ],
    "teams": [
        {"_id": ObjectId(), "name": "Team A", "members": []},
        {"_id": ObjectId(), "name": "Team B", "members": []},
    ],
    "activities": [
        {"_id": ObjectId(), "user": None, "activity_type": "Running", "duration": timedelta(minutes=30)},
        {"_id": ObjectId(), "user": None, "activity_type": "Cycling", "duration": timedelta(minutes=45)},
        {"_id": ObjectId(), "user": None, "activity_type": "Swimming", "duration": timedelta(minutes=60)},
    ],
    "leaderboard": [
        {"_id": ObjectId(), "user": None, "score": 100},
        {"_id": ObjectId(), "user": None, "score": 90},
        {"_id": ObjectId(), "user": None, "score": 80},
    ],
    "workouts": [
        {"_id": ObjectId(), "name": "Morning Run", "description": "A 5km run to start the day"},
        {"_id": ObjectId(), "name": "Cycling Session", "description": "A 20km cycling session"},
        {"_id": ObjectId(), "name": "Swimming Laps", "description": "30 minutes of swimming laps"},
    ],
}