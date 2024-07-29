# print ('HELLO')

# ---------------------------------------------------------------------------------------------
# Q1 

# * Write a Python program to read first n lines of a file (input).

# def func (num):
#     my_file = open('TEST.TXT', 'r')
#     for i in range(num):
#         list = my_file.readline()
#         print (list , end = "")
# func(4)


# ---------------------------------------------------------------------------------------------
# Q2

# * Write a Python program to read a random line from a file.

# import random
# import linecache

# my_file = open('TEST.TXT', 'r')
# Rand_line = linecache.getline('TEST.TXT' ,random.randint(1, len(my_file.readlines())))
# print (Rand_line, end = "")

# ---------------------------------------------------------------------------------------------
# Q3

# * Write a Python program that takes a text file and returns the number of words inside.
# Note: Some words can be separated by a comma with no space.

# import re
# my_file = open('TEST.TXT', 'r')
# lines = my_file.read()
# line = re.split(" |,|\n", lines)
# print(line)
# print(len(line))

# ---------------------------------------------------------------------------------------------
# # Q4

import os

def function_1(name, age, address, file_Name):
    def function_2():
        if (os.path.isfile(f'{file_Name}.txt') == True):
            print("Sorry This file is exist")
            return 
        else:
            New_file = open(f'{file_Name}.txt', 'w')
        def function_3():
            New_file.write(f'Name : {name}\nAge : {age}\nAddress : {address}')
            New_file.close()
            New_filer = open('TEST2.TXT', 'r')
            print(New_filer.read())
        function_3()
    function_2()

function_1('Mohamed', 25, 'Qena', 'TEST2.TXT')
