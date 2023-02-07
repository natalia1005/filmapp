from django.db import models

class Additional_inf(models.Model):

    SPECIES = {
        (0, 'Inne'),
        (1, 'Dramat historyczny'),
        (2, 'Komedia'),
        (3, 'Familijny'),
        (4, 'Musical'),
        (5, 'Komedia rom.'),
    }

    duration = models.PositiveSmallIntegerField(default=0)
    species = models.PositiveSmallIntegerField(default=0, choices=SPECIES)

class Movie(models.Model):
    title = models.CharField(blank=False, unique=True, max_length=64)
    year = models.PositiveSmallIntegerField(default=2000)
    description = models.TextField(default="")
    premiere = models.DateField(null=True, blank=True)
    imdb_rating = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    poster = models.ImageField(upload_to="plakaty", null=True, blank=True)
    additional = models.OneToOneField(Additional_inf, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title + ' (' + str(self.year) + ')'

    def title_with_year(self):
        return "{} ({})".format(self.title, self.year)


class Rate(models.Model):
    review = models.TextField(default="", blank=True)
    stars = models.PositiveSmallIntegerField(default=10)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

class Actor(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    movie = models.ManyToManyField(Movie, related_name="aktorzy")
