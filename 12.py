# Write a Python function that checks if a given number is prime or not from 1 to 200.
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
for n in range(1, 201):
    if is_prime(n):
        print(n)