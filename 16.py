# Use a lambda function in Python to sort a list of tuples based on the second element of each tuple.
data = [(1, 'apple'), (3, 'banana'), (2, 'cherry')]
sorted_date = sorted(data, key=lambda x: x[1])
print(sorted_date)