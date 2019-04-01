from django.test import TestCase
from games.models import Game

class GameModelTests(TestCase):
    def setUp(self):
        Game.objects.create(title="smash bros.")
        Game.objects.create(title="smash bros X")
    
    def test_index_games(self):
        self.assertEqual(Game.objects.all.count(), 2)