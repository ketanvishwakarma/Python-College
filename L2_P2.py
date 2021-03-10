#L2 : P2 Write a python program to print the fibonacci series using while loop.

n0 = count = 0
n1 = 1 
n = int(input('Enter series lenght: '))
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