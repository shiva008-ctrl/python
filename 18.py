# Create a Python program that uses filter() to remove all the vowels from a given string.
def remove_vowels(input_string):
    vowels = 'aeiouAEIOU'
    return ''.join(filter(lambda x: x not in vowels, input_string))
      
