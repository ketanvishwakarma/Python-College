#L1 : Practical 1 : Write a menu driven program to implement a calculator in python.
while True:
    print('Operation Menu \n 1: Add\n 2: Sub\n 3: Mul\n 4: Div');
    choice = input('Select Operation : ')
    if choice in {'1','2','3','4'}:
        n1 = int(input('Enter First Number : '))
        n2 = int(input('Enter Second Number : '))
        if choice == '1':
            print(n1+n2)
        elif choice == '2':
            print(n1-n2)
        elif choice == '3':
            print(n1*n2)
        elif choice == '4':
            print(n1/n2)
    else: print('invalid input')