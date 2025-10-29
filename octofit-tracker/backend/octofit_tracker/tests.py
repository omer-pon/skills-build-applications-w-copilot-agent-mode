from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create(name='Test User', email='test@example.com', team=self.team)

    def test_user_creation(self):
        self.assertEqual(self.user.name, 'Test User')
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertEqual(self.user.team, self.team)

    def test_activity_creation(self):
        activity = Activity.objects.create(user=self.user, activity='Running', duration=30)
        self.assertEqual(activity.user, self.user)
        self.assertEqual(activity.activity, 'Running')
        self.assertEqual(activity.duration, 30)

    def test_leaderboard_creation(self):
        leaderboard = Leaderboard.objects.create(user=self.user, points=100)
        self.assertEqual(leaderboard.user, self.user)
        self.assertEqual(leaderboard.points, 100)

    def test_workout_creation(self):
        workout = Workout.objects.create(user=self.user, workout='Pushups', reps=50)
        self.assertEqual(workout.user, self.user)
        self.assertEqual(workout.workout, 'Pushups')
        self.assertEqual(workout.reps, 50)
