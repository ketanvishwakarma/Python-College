#L2 : P3 Write a python program find the difference between two dates.
import datetime as my_date
x = my_date.date(1999,10,29)
y = my_date.date(2021,3,11)
diff = y-x
print(diff.days,'Days')