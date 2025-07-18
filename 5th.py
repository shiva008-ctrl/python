
# Create a function greet(name) that prints “Hello, [name]!”
def greet(name):
    print(f"Hello, {name}!")
greet("sahil")
  
#Q2. Create a function add(a, b) that returns the sum of two numbers. Call the function with inputs
def add(a, b):
    return a + b
result = add(10, 20)
print("Sum:", result)

#Q3. Create a function display(*args) that accepts multiple arguments and prints them
def display(*args):
    for item in args:
        print(item)
display("Python", 123, True, 4.5)

# Q4. Create a function student_info(**kwargs) that accepts name, age, roll number as keyword arguments and prints them.
def student_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
student_info(name="Sahil", age=18, roll_number=101)