# Implement a generator function that reads a file line by line and yields each line as a string.

def read_lines(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line.rstrip('\n')
filename = input("Enter the filename: ")
for line in read_lines(filename):
    print(line)

