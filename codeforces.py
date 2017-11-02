# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 11:52:54 2017

@author: HP 15 AB032TX
"""
import bs4
import requests
from bs4 import BeautifulSoup 
import datetime
def codeforces():
	

	url2="http://codeforces.com/contests"
	uclient=requests.get(url2)
	page_html=uclient.text;
	ps = BeautifulSoup(page_html, "html.parser")
	contestInfo = ps.findAll("div", {"class": "datatable"})[0]
	allRows = contestInfo.findAll("tr")
	#print allRows
	#print ("Upcoming Contests:")
	#headRow = allRows[1].findAll("td")
	#print headRow,"here"
	Months=["None","Jan","Feb","Mar","April","May","June","July","Aug","Sep","Oct","Nov","Dec"]
	Contests=[]
	for i in range(len(allRows)-1):
	    k= allRows[i+1].findAll("td")
	    #Start Date Standardization 
	    start_date=k[2].text.strip().split("/")
	    mon=start_date[0]
	    mon=str(Months.index(mon))
	    start_date[0]=mon
	    start_date="/".join(start_date)
	    start_date=datetime.datetime.strptime(start_date,"%m/%d/%Y %H:%M")
	    
	    #End date Calculation from Duration ans Start Date

	    duration=k[3].text.strip().split(":")[::-1]
	    duration_in_minutes=int(duration[0])+60*int(duration[1])
	    	#duration_in_minutes+=(60**i)*int(duration[i])
	    #print duration_in_minut
	    end_date=start_date+datetime.timedelta(minutes=duration_in_minutes)
	    #print end_date,start_date,duration    
	    Contests.append((str(k[0].text.strip()),str(start_date),str(end_date)))
	    print Contests
	    return Contests
	    #print "Contest Name: "+str(k[0].text.strip()),"Contest Duration: " + str(start_date) + " - " + str(end_date)
codeforces()