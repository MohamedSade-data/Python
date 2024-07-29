# # q1

# str = 'AAAHello World Mohamed Sadeq iti'
# count = 0

# for x in str:
#     if x in ['a', 'i', 'o', 'e', 'u']:
#         count += 1

# print (count)

# # --------------------------------------------------------------
# # q2



# listnum = [1, 2, 10, 3, -9, -80, 5, 300]
# listnum.sort()
# listnum.reverse() 
# print(listnum)

# # --------------------------------------------------------------
# # q3

# str = 'Hello World Mohamed iti Sadeq iti'
# count = 0

# str.count('ITI')


# # --------------------------------------------------------------
# # q4

# str = 'Hello World Mohamed Sadeq iti'

# for x in str:
#     if x in ['e', 'a', 'o', 'i', 'u']:
#         str = str.replace(x, '')

# print(str)

# # --------------------------------------------------------------
# # q5

# str = 'Hello World Mohamed Sadeq iti ii i i'

# for x in range(len(str)):
#    if str[x] == 'i':
#        print (x)

# # --------------------------------------------------------------
# # q6

# # num = 4

# print ('[', end = ' ')

# for i in range(1,4):
#     print ('[', end = ' ')
#     for x in range(1, i+1):
#         print (i * x, end = ' ')
#     print (']', end = ' ')
# print (']', end = ' ')

# # --------------------------------------------------------------
# # q7

# # for i in range(1, 5):
# #     for x in range(5, 0, -1):
# #         if x > i:
# #             print(" ", end = ' ')
# #         else:
# #             print('*', end = ' ')
# #     print(" ")


for i in range(1,6):
    print(" " * (5 - i) + i * "*")