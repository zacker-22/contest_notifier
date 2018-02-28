# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 11:52:54 2017

@author: HP 15 AB032TX
"""


import bs4
import requests
from bs4 import BeautifulSoup 
import datetime
def codechef():
	url2="http://codechef.com/contests"
	uclient=requests.get(url2)
	page_html=uclient.text

	page_html= page_html.replace("</>","")
	ps = BeautifulSoup(str(page_html), "html.parser")


	contestInfo = ps.findAll("table", {"class": "dataTable"})[1]

	allRows = contestInfo.findAll("tr")
	#print allRows[1:]

	#print ("Upcoming Contests:\n")
	#headRow = allRows[1].findAll("td")
	#print headRow,"here"
	Months=["None","Jan","Feb","Mar","April","May","June","July","Aug","Sep","Oct","Nov","Dec"]
	contests=[]
	for i in range(len(allRows)-1):
	    k= allRows[i+1].findAll("td")
	    #Start Date Standardization 
	    startDate=k[2].text.split(" ")
	    endDate=k[3].text.split(" ")

	    startDate[1]=str(Months.index(startDate[1]))
	    endDate[1]=str(Months.index(endDate[1]))

	    start_date=""
	    
	    for i in startDate:
	    	if len(i)>=1 :
	    		start_date+=i+" "
	    end_date=""
	    for i in endDate:
	    	if len(i)>=1:
	    		end_date+=i+" "

	    start_date=datetime.datetime.strptime(start_date,"%d %m %Y %H:%M:%S ")
	    end_date=datetime.datetime.strptime(end_date,"%d %m %Y %H:%M:%S ")
	    contestName = k[1].text
	    contests.append((contestName,str(start_date),str(end_date)))

	return contests
