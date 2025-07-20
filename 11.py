def sum_of_evens(numbers):
    return sum(n for n in numbers if n % 2== 0)
user_input = input("enter numbers :")
numbers = [int(x) for x in user_input.split()]
result = sum_of_evens(numbers)
print(result)