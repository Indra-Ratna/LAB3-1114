"""
Indra Ratna
CS-UY 1114
Lab 3
"""
import datetime
days = 0
x = input("What is your birthday in yyyymmdd form?")
y = (datetime.datetime.now().strftime("%Y%m%d"))
print("Your date of birth is "+x+ " and today is "+ str(y))
user_day = str(int(x)%100)
user_month = x[4:6]
user_year= x[0:4]
today_day = str(int(y)%100)
today_month= y[4:6]
today_year= y[0:4]
alive_year = int(today_year)-int(user_year)
alive_month = int(today_month)-int(user_month)
alive_day = int(today_day)-int(user_day)
if(int(user_month)%2==0):
    days = 31
else:
    days = 30
if(today_month<user_month):
     alive_year= alive_year-1
if(today_day<user_day):
     alive_month=alive_month-1
     alive_day= (int(today_day))+(days-int(user_day))


print("Date of birth is "+user_month+"/"+user_day+"/"+user_year)
print("Today's date is "+today_month+"/"+today_day+"/"+today_year)
print("You have been alive for "+str(alive_year)+" years "+str(alive_month)+" month(s) and "+str(alive_day)+" day(s)")


