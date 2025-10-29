from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members')

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    activity = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()

class Leaderboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leaderboard_entries')
    points = models.PositiveIntegerField()

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workouts')
    workout = models.CharField(max_length=100)
    reps = models.PositiveIntegerField()
