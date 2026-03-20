from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        app_label = 'octofit_tracker'

class Activity(models.Model):
    name = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    points = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    team = models.CharField(max_length=100)
    points = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    suggestion = models.CharField(max_length=255)
    class Meta:
        app_label = 'octofit_tracker'

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='pass', first_name='Tony', last_name='Stark')
        captain = User.objects.create_user(username='captain', email='captain@marvel.com', password='pass', first_name='Steve', last_name='Rogers')
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='pass', first_name='Bruce', last_name='Wayne')
        superman = User.objects.create_user(username='superman', email='superman@dc.com', password='pass', first_name='Clark', last_name='Kent')

        # Create activities
        Activity.objects.create(name='Running', user='ironman', team='Marvel', points=10)
        Activity.objects.create(name='Swimming', user='captain', team='Marvel', points=8)
        Activity.objects.create(name='Cycling', user='batman', team='DC', points=12)
        Activity.objects.create(name='Jumping', user='superman', team='DC', points=15)

        # Create leaderboard
        Leaderboard.objects.create(team='Marvel', points=18)
        Leaderboard.objects.create(team='DC', points=27)

        # Create workouts
        Workout.objects.create(name='Pushups', suggestion='Do 20 pushups')
        Workout.objects.create(name='Situps', suggestion='Do 30 situps')
        Workout.objects.create(name='Squats', suggestion='Do 40 squats')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
