#L2 : P5 Write a python program to print Fibonacci series using function

def Fibonacci(n):
    n0 = count = 0
    n1 = 1 
    if n <= 0: 
        print('Fibonacci Not Exits')
    if n == 1:
        print(n0)
    else:
        print("Fibonacci series upto {} terms: ".format(n))
        while count < n:
            print(n0)
            current = n0 + n1
            n0 = n1
            n1 = current
            count += 1

n = int(input('Enter series lenght: '))
Fibonacci(n)