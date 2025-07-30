try:
     a=int(input("enter  a number"))
     b=input("enter string")
     print(a+b)
except (ValueError,TypeError) as  e:
    print(e)
print("hi")
