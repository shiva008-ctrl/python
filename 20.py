# with open('demo.txt', 'r') as file:
#     hello = file.read()
#     print(hello)  
     
# with open('demo.txt', 'r') as file:
#     hello = file.read()
#     print(hello)


# genrato

# def count_of(n):
#     i=1
#     while i<=n :
#         yield i
#         i+=1
# gen = count_of(5)
# for _ in range(5):  
#     print(next(gen))
import threading

def task():
    print("Running in a thread")
thread = threading.Thread(target=task)
thread.start()
