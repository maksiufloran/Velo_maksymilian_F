from django.db import models

# Create your models here.
class Artist(models.Model):
    # id will be added automatically
    first_name = models.CharField(max_length=51) # 51 because this is the length of the longest name
    last_name = models.CharField(max_length=81) # same thing
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'artist'

class Hit(models.Model):
    # id will be added automatically
    title = models.CharField(max_length=100) # title of the song
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title_url = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'hit'