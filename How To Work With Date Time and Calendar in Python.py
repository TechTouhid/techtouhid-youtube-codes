import time  # in order to work with the time we need this module
from datetime import date  # in order to work with the date we need this module
import calendar  # in order to work with the calender we need this module

# To know the current time
current_time = time.localtime(time.time())

print(current_time)

# Current time with understandable form
formatted_time = time.asctime(current_time)
print(formatted_time)

# To take a custom Time tuple
struct_time = time.strptime("6 sep 20", "%d %b %y")
print(struct_time)

# To know the date of today
today = date.today()
print(f"Today is : {today}")

# To know the year month and day form today's date
print(today.year)
print(today.month)
print(today.day)

# A simple program to calculate your birthday
my_birthday = date(2000, 6, 24)

my_age = abs(my_birthday.year - date.today().year)

print(f'I am {my_age} years old.')

# To customize the date format
formatted_date = date.today().strftime("%d-%m-%y")
print(formatted_date)

# To customize the date format
formatted_date2 = date.today().strftime("%A %d %B %Y")
print(formatted_date2)

# Take the time tuple form today's date
struct_time_today = today.timetuple()
print(struct_time_today)

# looping over the struct time tuple
for i in struct_time_today:
    print(i)

# To take the calendar form a year
print(calendar.calendar(2020))

# To take the calendar form a month
print(calendar.month(2020, 9))

# To know a year is leap year or not
print(calendar.isleap(2001))

# Know the leap days between two year
print(calendar.leapdays(2000, 2020))
