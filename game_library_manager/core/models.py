from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User


class Genre(models.Model):
    name = models.CharField(max_length=64)
    game_count = models.IntegerField()
    image_background = models.URLField()
    description = models.TextField()
    last_cached = models.DateTimeField(auto_now=True)


class Game(models.Model):
    rawg_id = models.IntegerField()
    title = models.CharField(max_length=256)
    cover_url = models.URLField()
    genres = models.ManyToManyField(Genre)
    last_cached = models.DateTimeField(auto_now=True)


class BacklogEntry(models.Model):
    # allowed statuses
    BACKLOG = "Backlog"
    PLAYING = "Playing"
    DROPPED = "Dropped"
    FINISHED = "Finished"
    COMPLETED = "Completed"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=10,
        choices={
            BACKLOG: "Want to play",
            PLAYING: "Currently playing",
            DROPPED: "Gave up on it",
            FINISHED: "Beaten the game, but haven't collected all the achievements",
            COMPLETED: "100% the game",
        },
    )
    rating = models.PositiveIntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
