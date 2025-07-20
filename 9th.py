def squares_list(numbers):
    return [x**2 for x in numbers]
while True:
 user_input = input("enter the numbers :")
 if user_input.lower() == 'exit':
    break
 numbers = [int(x) for x in user_input.split()]
 print(squares_list(numbers))
