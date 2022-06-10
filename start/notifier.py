import datetime
import time
import requests
from plyer import notification

covidData = None

try:
    covidData = requests.get(
        "https://corona-rest-api.herokuapp.com/Api/rwanda")
except:
    print("Please check your internet connection")

if(covidData != None):
    data = covidData.json()
    # print(data)
    while (True):
        notification.notify(
            title="COVID-19 Stats on {}".format(datetime.date.today()),
            message="Total cases : {totalcases}\nToday cases : {todaycases}\nToday deaths :{todaydeaths}\nTotal active :{active}".format(
                totalcases=data['Success']['cases'],
                todaycases=data['Success']['todayCases'],
                todaydeaths=data['Success']['todayDeaths'],
                active=data['Success']["active"]),
            app_icon='bg.png',
            timeout=50
        )
        time.sleep(60*60)