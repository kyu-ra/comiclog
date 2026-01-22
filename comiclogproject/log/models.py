from django.db import models
import datetime

# Create your models here.

# Information to log:
    # Comic Name
    # Issue number (if applicable)
    # Publication year 
    # Era (if applicable)
    # Rating

eras = [
    ["Golden Age", datetime.date(1942,2,1)],
    ["Silver Age", datetime.date(1956,10,1)],
    ["Bronze Age", datetime.date(1970,4,1)],
    ["Post-Crisis", datetime.date(1985,4,1)],
    ["New 52", datetime.date(2011,8,31)],
    ["Rebirth", datetime.date(2016,5,25)],
    ["Infinite Frontier", datetime.date(2021,3,2)]
]

class Comic(models.Model):
    comic_name = models.CharField("Comic Name", max_length=200)
    issue_num = models.IntegerField("Issue Number", blank=True, null=True)
    pub_date = models.DateField("Date Published")

    # To define what era the comic was from. this needs to be moved outside the model
    def whatEra(pubdate):
        i = len(eras) - 1
        while i < len(eras):
            if(pubdate > eras[i][1]):
                return eras[i]
            else:
                i -= 1

    read = models.BooleanField("Read", default=False)

    RATINGS = {
        "5": "Loved",
        "4": "Liked",
        "3": "Neutral",
        "2": "Didn't Like",
        "1": "Hated",
    }
    rating = models.CharField("Rating", max_length=1, choices=RATINGS, blank=True, null=True)

    def __str__(self):
        return self.comic_name
 