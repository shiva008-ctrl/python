total_bottles=int(input("Enter the bottle:"))
daily_use=int(input("enter boottles you are drink:"))
day=1
while total_bottles>0:
    drink =min(daily_use,total_bottles)
    total_bottles-=drink
    if total_bottles==0:
     print(f"day{day}:drank{drink}bottles.0 left.")
     print("plese refill the bottles!")
    elif 40<=total_bottles<=50:
       print(f"day{day}:drank{drink}bottles. only 40 to 50 left.")
    else:
       print(f"day{day}: drank{drink}bottles.{total_bottles}left.")
       day+=1