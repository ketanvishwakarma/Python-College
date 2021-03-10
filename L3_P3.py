#L3 : P3 Write a Python program to concatenate all elements in a list into a string and return it.

mylist = [29,10,1999,'is my birthdate']
string = ''
for element in mylist:
    string += str(element) + ' ' 
print(string)
