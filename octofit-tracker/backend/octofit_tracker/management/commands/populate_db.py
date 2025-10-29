from django.core.management.base import BaseCommand
from django.conf import settings
from django.db import connection
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Connect to MongoDB
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Clear existing data
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Create unique index on email for users
        db.users.create_index('email', unique=True)

        # Teams
        marvel = {'name': 'Team Marvel'}
        dc = {'name': 'Team DC'}
        marvel_id = db.teams.insert_one(marvel).inserted_id
        dc_id = db.teams.insert_one(dc).inserted_id

        # Users (super heroes)
        users = [
            {'name': 'Spider-Man', 'email': 'spiderman@marvel.com', 'team_id': marvel_id},
            {'name': 'Iron Man', 'email': 'ironman@marvel.com', 'team_id': marvel_id},
            {'name': 'Wonder Woman', 'email': 'wonderwoman@dc.com', 'team_id': dc_id},
            {'name': 'Batman', 'email': 'batman@dc.com', 'team_id': dc_id},
        ]
        db.users.insert_many(users)

        # Activities
        activities = [
            {'user_email': 'spiderman@marvel.com', 'activity': 'Running', 'duration': 30},
            {'user_email': 'ironman@marvel.com', 'activity': 'Cycling', 'duration': 45},
            {'user_email': 'wonderwoman@dc.com', 'activity': 'Swimming', 'duration': 60},
            {'user_email': 'batman@dc.com', 'activity': 'Yoga', 'duration': 40},
        ]
        db.activities.insert_many(activities)

        # Leaderboard
        leaderboard = [
            {'user_email': 'spiderman@marvel.com', 'points': 100},
            {'user_email': 'ironman@marvel.com', 'points': 90},
            {'user_email': 'wonderwoman@dc.com', 'points': 110},
            {'user_email': 'batman@dc.com', 'points': 95},
        ]
        db.leaderboard.insert_many(leaderboard)

        # Workouts
        workouts = [
            {'user_email': 'spiderman@marvel.com', 'workout': 'Pushups', 'reps': 50},
            {'user_email': 'ironman@marvel.com', 'workout': 'Situps', 'reps': 40},
            {'user_email': 'wonderwoman@dc.com', 'workout': 'Squats', 'reps': 60},
            {'user_email': 'batman@dc.com', 'workout': 'Plank', 'reps': 5},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
