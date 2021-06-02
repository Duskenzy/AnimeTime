import webbrowser
import datetime
from datetime import date

def todaysDay():
    x = datetime.date.today()
    y = x.strftime("%A")
    return y

def calculateDate(startDate):
    days_from_start = int((date.today() - startDate).days / 7)
    return days_from_start

def actualEpisode():
    weeks_from_start = calculateDate(date(2021, 4, 25))
    newest_Ep_Num = 971 + weeks_from_start
    return newest_Ep_Num

def sundayAnimeTime():
    if todaysDay() == "Sunday":
        webbrowser.open("http://onepiece-tube.com/folge/%s-tBvZaU" % actualEpisode())

sundayAnimeTime()
