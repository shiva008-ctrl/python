# Write a Python program that uses map() to convert a list of temperatures from Celsius to Fahrenheit
temperatures_celsius = [10, 20, 30, 40, 50]
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
temperatures_fahrenheit = list(map(celsius_to_fahrenheit, temperatures_celsius))
print(temperatures_fahrenheit)