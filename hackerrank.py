import requests
from bs4 import BeautifulSoup
import datetime
from subprocess import call
def hackerrank():
    url = "https://www.hackerrank.com/contests"
    r = requests.get(url)
    soup = BeautifulSoup(r.content,"html.parser")

    Contests = []

    active_contests = soup.find_all("ul" , {"class": "contests-active"})
    active_contests = active_contests[0].find_all("li")

    #Ignoring Project Euler
    for i in range(1,len(active_contests)): 
        contestName = active_contests[i].div.find_all("div", {"class": "contest-name"})
        status = active_contests[i].div.find_all("div", {"class": "contest-status"})
        startDate = status[0].find_all("meta", {"itemprop": "startDate"})
        endDate = status[0].find_all("meta", {"itemprop": "endDate"})
        date_posted = endDate[0]['content']
        last_date = datetime.datetime.strptime(date_posted, '%Y-%m-%dT%H:%M:%S.%fZ')+datetime.timedelta(minutes=330)
        start_date = datetime.datetime.strptime(startDate[0]['content'],'%Y-%m-%dT%H:%M:%S.%fZ')++datetime.timedelta(minutes=330)
        Contests.append((contestName[0].get_text(),str(start_date),str(last_date)))
    return Contests


   