#L2 : P4 Write a python program to display Calendar of a given month and year.
import calendar as my_cal
year = int(input('Enter Year : '))
month = int(input('Enter Month : '))
print(my_cal.month(year,month))