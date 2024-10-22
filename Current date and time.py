from datetime import date, time, datetime
#calling the today
#function of date class
today=date.today()
now=datetime.now()
print("Today's date is:",today)
print("\n current time is:",now)

print("\nDate components",today.year,today.month,today.day)