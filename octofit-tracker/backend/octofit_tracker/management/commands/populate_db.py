from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data in correct order (children before parents)
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()
        for user in User.objects.all():
            if user.pk:
                user.delete()
        for team in Team.objects.all():
            if team.pk:
                team.delete()


        # Create teams and save
        marvel = Team(name='Marvel', description='Marvel Superheroes')
        marvel.save()
        dc = Team(name='DC', description='DC Superheroes')
        dc.save()

        # Create users and save
        spiderman = User(name='Spider-Man', email='spiderman@marvel.com', team=marvel)
        spiderman.save()
        ironman = User(name='Iron Man', email='ironman@marvel.com', team=marvel)
        ironman.save()
        wonderwoman = User(name='Wonder Woman', email='wonderwoman@dc.com', team=dc)
        wonderwoman.save()
        batman = User(name='Batman', email='batman@dc.com', team=dc)
        batman.save()

        # Create workouts and save
        cardio = Workout(name='Cardio Blast', description='High intensity cardio', difficulty='Hard')
        cardio.save()
        strength = Workout(name='Strength Training', description='Build muscle', difficulty='Medium')
        strength.save()

        # Create activities
        Activity.objects.create(user=spiderman, type='Running', duration=30, calories=300, date='2025-12-01')
        Activity.objects.create(user=ironman, type='Cycling', duration=45, calories=400, date='2025-12-02')
        Activity.objects.create(user=wonderwoman, type='Swimming', duration=60, calories=500, date='2025-12-03')
        Activity.objects.create(user=batman, type='Yoga', duration=40, calories=200, date='2025-12-04')

        # Create leaderboard and save
        marvel_leaderboard = Leaderboard(team=marvel, points=700)
        marvel_leaderboard.save()
        dc_leaderboard = Leaderboard(team=dc, points=600)
        dc_leaderboard.save()

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
