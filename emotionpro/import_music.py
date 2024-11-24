import csv
from django.core.management.base import BaseCommand
from musicapp.models import Song

class Command(BaseCommand):
    help = 'Import songs from CSV file into the database'

    def handle(self, *args, **kwargs):
        with open("C:/Users/HP PC/Desktop/musicplayer/emotionpro/updated_musicData.csv", mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Insert each row into the Song model
                Song.objects.create(
                    name=row['name'],
                    artist=row['artist'],
                    song_url=row['id'],  # This is now the Spotify URL
                    mood=row['mood']
                )
        self.stdout.write(self.style.SUCCESS('Successfully imported songs!'))
