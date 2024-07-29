
# ------------------------------------------------------------------------
# Q1

def func1(length, start, steps):
    list1 = []
    while length != 0 :
        #print(start)
        list1.append(start)
        length -= steps
        start += 1
    return list1

#print(func1(5, 15, 1))

# # ------------------------------------------------------------------------
# # Q2

# def func2 (num):

#     if (num % 5 == 0 and num % 3 == 0):
#         print ('Fizz Buzz')

#     elif (num % 3 == 0):
#         print ('Fizz')
    
#     elif (num % 5 == 0):
#         print ('Buzz')
    
#     else:
#         print('Not Recognized')

# func2(9)

# ------------------------------------------------------------------------
# Q3

# user_input = input("Enter String : ")

# def func3(user_input):
#     return (user_input[::-1])

# print (func3("MOhamed"))

# ------------------------------------------------------------------------
# Q4

# def func4(user_name, mail):

#     if (user_name != "" and str(user_name).isalpha()):
#         print (f'Hello {user_name} , Your Mail is {mail}')
#     else:
#         print('User Name is inCorrect')

# func4('ksja','sls')

# mail = 'mohamedsadek@gmail.com'
# if (mail == r'\s?[A-Z0-9_-+%]+@[A-Z0-9_-+%]+\.[A-Z0-9]\s?'):
#     print ('its mail')
# else:
#     print ('not mail')

# ------------------------------------------------------------------------
# Q5

# def fuc6(str):
#     word = ''
#     store  = []

#     for i in range(0, len(str) - 1):
#         if (str[i + 1] > str[i]):
#             word += str[i]
#         else:
#             word += str[i] + str[i + 1]
#             store.append(word)
#             word = ''
#     print (max(store, key = len))

# fuc6 ('moameabcdefjh')

# ------------------------------------------------------------------------
# Q6


user_input = input('Enter your number : ')
num_count = 0
numper = 0

while user_input  != "Done":
    if (user_input == 'Done'):
          break
    
    elif (user_input.isalpha() == True):
            print ('Not Valid .')
            user_input = input('Enter your number : ')
    else:
            numper += int(user_input)
            num_count += 1 
            user_input = input('Enter your number : ')

print (f'{numper}, {num_count}, {numper/num_count}')