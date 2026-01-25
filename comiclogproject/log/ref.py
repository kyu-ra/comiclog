import datetime

# Reference information for Log

class ComicRef:
    
    global eras
    eras = [
    ["Golden Age", datetime.date(1942,2,1)],
    ["Silver Age", datetime.date(1956,10,1)],
    ["Bronze Age", datetime.date(1970,4,1)],
    ["Post-Crisis", datetime.date(1985,4,1)],
    ["New 52", datetime.date(2011,8,31)],
    ["Rebirth", datetime.date(2016,5,25)],
    ["Infinite Frontier", datetime.date(2021,3,2)]
    ]

    # To define what era the comic was from
    def whatEra(pubdate):
        i = len(eras) - 1
        while i < len(eras):
            if(pubdate > eras[i][1]):
                return eras[i]
            else:
                i -= 1

    RATINGS = {
        "5": "Loved",
        "4": "Liked",
        "3": "Neutral",
        "2": "Didn't Like",
        "1": "Hated",
    }