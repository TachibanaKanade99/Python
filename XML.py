import calendar
cal = calendar.month(2017,11)
print("This is my calendar")
print(cal)
calendar.firstweekday()

from datetime import datetime
now = datetime.now()
a = now.day
b = now.month
c = now.year
print("%s/%s/%s" % (now.day, now.month, now.year))