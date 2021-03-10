#L3 : P4 Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2.
color_list_1 = {'Red', 'Green', 'Blue'}
color_list_2 = {'Red', 'White', 'Purple'}
print(color_list_1.difference(color_list_2))