from django.db import models
import datetime

from .ref import ComicRef as ref

# Create your models here.

# Information to log:
    # Comic Name
    # Issue number (if applicable)
    # Publication year 
    # Era (if applicable)
    # Rating

class Comic(models.Model):
    comic_name = models.CharField("Comic Name", max_length=200)
    issue_num = models.IntegerField("Issue Number", blank=True, null=True)
    pub_date = models.DateField("Date Published")
    pub_date_exact = models.BooleanField("Exact Publication Date Known", default=True)
    read = models.BooleanField("Read", default=False)
    ratingOptions = ref.RATINGS
    rating = models.CharField("Rating", max_length=1, choices=ratingOptions, blank=True, null=True)

    def __str__(self):
        name = self.comic_name
        if self.issue_num is not None:
            name += ", #" + str(self.issue_num)
        return name 