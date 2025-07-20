def decorator (func):
    print("decorator is called")
    func()
    print("decorator is finished")
    return decorator
@decorator  
def my_function():
    print("hello word ")