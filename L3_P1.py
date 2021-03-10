#L3 : P1 Write a Python program which accepts a sequence of comma separated numbers from user and generate a list and a tuple with those numbers.

numbers = input('Enter comma separated numbers : ')
list = numbers.split(',')
tuple = tuple(list)
print('List : ', list)
print('tuple : ', tuple)
