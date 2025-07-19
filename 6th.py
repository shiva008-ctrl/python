# def my_function(**kids):
#     print("the last name of kid",kids["lname"])
# my_function(fname="abc",lname="kbc")

# default perameter values 

# def my_function(country="india"):
#   print("i am from " +country)
# my_function("uk ")
# my_function("thailand")
# my_function()
# my_function("wb")


# def my_function(food):
#     for x in food:
#         print(x)
# fruits = ["apple","banana","chery"]
# my_function(fruits)


# def my_function(x):
#     return 10+x
# print(my_function(5))
# my_function(3)

# print(my_function (6))



# def my_function(x,/):
#     print(x)
# my_function((3))



# print the no .of variable in this 
# input_str="aaabbbcccffff"
# count_dist={}
# for char in input_str:
#     if char in count_dist:
#         count_dist[char] += 1
#     else:
#         count_dist[char] = 1
#         for char in count_dist:
#             print(f"{char}:{count_dist[char]}")



# def my_function(*x):
#     my_function(x=5)

# def my_function(*,x):
#     print (x)
#     my_function(x=4)
# 5,10,c=5,d=15

# def my_function(a,b,/,*,c,d):
#     print(a+b+c+d)
# my_function(5,10,c=15,d=15)


# def is_palindrome(s):
#     if len(s) <= 1:
#         return True
#     if s[0] == s[-1]:
#         return is_palindrome(s[1:-1])
#     return False

# word = input("enter a word: ")
# if is_palindrome(word):
#     print(f"{word} is a palindrome")
# else:
#     print(f"{word} is not a palindrome")


import random
def guess_number(secret, attempts=1):
    while True:
            guess=int(input(f"Attempt {attempts}: Guess the number (between 1 and 10): "))
            if guess <secret:
             print("Too low! Try again.")
             return guess_number(secret, attempts + 1)
            elif guess>secret:
             print("Too high! Try again.")
             return guess_number(secret, attempts + 1)
            elif guess==secret:
             print(f"Congratulations! You've guessed the number {secret} in {attempts} attempts.")
            return attempts
guess_number(random.randint(1, 10))

