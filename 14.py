# Write a generator function in Python that yields the powers of 2 up to a given exponent

def powers_of_two(max_exponent):
    for exp in range(max_exponent + 1):
        yield 2 ** exp
for value in powers_of_two(5):
    print(value)