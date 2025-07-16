bill_amount = int(input("enter bill amount: ,$"))
number_of_friends=int(input("enter number of friends:"))
amount_per_friends =bill_amount / number_of_friends
print("each friends should pay: $,amount_per_friends.2f" )
tip_persentage = int(input("enter tip persentage:(10,20,30,40,50)"))
if tip_persentage == 10:
    tip_amount = bill_amount *0.10
elif tip_persentage == 20:
    tip_amount = bill_amount *0.20
elif tip_persentage ==30:
    tip_amount = bill_amount *0.30
elif tip_persentage == 40:
    tip_amount = bill_amount *0.40
elif tip_persentage == 50:
    tip_amount = bill_amount *0.50
else:
  print("invaide input")
print("The tip amount is: $%.2f" % tip_amount)
total_with_tip = bill_amount + tip_amount
amount_per_friend_with_tip = total_with_tip / number_of_friends

print("Each friend should pay (including tip): $%.2f" % amount_per_friend_with_tip)
