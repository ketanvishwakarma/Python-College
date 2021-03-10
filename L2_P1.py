#L2 : P1 Write a python program to print the factorial of given number using for loop.

factorial = 1
x = int(input('Enter Number : '))
if x < 0: 
    print('Factorial Not Exits')
if x == 0:
    print('1')
else:
    for i in range(1, x+1):
        factorial *= i
    print(factorial)