#Ira Aggarwal
#2018039
#Section A
#Group 7 

import datetime
import urllib.request

def get_date(dateFormat,n):
    now= datetime.datetime.now()
    if (n!=0):
        later = now+datetime.timedelta(days=n)
    else:
        later=now

    return later.strftime(dateFormat)

def weather_response(location,api):
	one = "http://api.openweathermap.org/data/2.5/forecast?q="+location+"&APPID="+api
	two=str(urllib.request.urlopen(one).read())
	return (two) 

def has_error(location,output):
	fnd= output.find('"city not found"')
	ind1= output.find('"name"')
	ind2= output.find(',',ind1)
	ind3= output[ind1 +8: ind2-1]
	"""to upper/to lower"""
	if (ind3 !=location):
		return True

def get_temperature(output,n,t ="03:00:00"):
	date=get_date("%Y-%m-%d",n)
	t1 =output.find(str(date))
	u = output.rfind('"temp"',0,t1)
	v = output.find(',', u)
	temp= output[u+7:v]
	temp= float(temp)
	return temp
	

def get_humidity(output,n,t='03:00:00'):
	date=get_date("%Y-%m-%d",n)
	t = output.find(str(date))
	u = output.rfind('"humidity"',0,t)
	v = output.find(',', u)
	hum= output[u+11:v]
	hum=int(hum)
	return hum
	

def get_pressure(output,n,t='03:00:00'):
	date=get_date("%Y-%m-%d",n)
	t = output.find(str(date))
	u = output.rfind('"pressure"',0,t)
	v = output.find(',', u)
	press= output[u+11:v]
	press=float(press)
	return press
	

def get_wind(output,n,t='03:00:00'):
	date=get_date("%Y-%m-%d",n)
	t = output.find(str(date))
	u = output.rfind('"speed"',0,t)
	v = output.find(',', u)
	wspeed= output[u+8:v]
	wspeed=float(wspeed)
	return wspeed
	


def get_sealevel(output,n,t='03:00:00'):
	date=get_date("%Y-%m-%d",n)
	t = output.find(str(date))
	u = output.rfind('"sea_level"',0,t)
	v = output.find(',', u)
	slvl= output[u+12:v]
	slvl= float(slvl)
	return slvl
	









	


