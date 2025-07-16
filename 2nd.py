while True:
    gender_input = int(input("""Enter your gender:
   1 for male 
   2 for female: """))
    user_input = int(input("Enter your age: "))
    if gender_input == 1:
         if user_input>=91:
          print("ek pau kabar mai hai uncle") 
    elif user_input>=21:
        print("feelding set")
     
    elif user_input<=18:
        print("doing study boy ")
    else:
        print("you are an adult male")   
    if gender_input == 2:
        if user_input>=90:
         print("Should we look into new teeth for you, Grandma")
        elif user_input>=19:
            print("eligible for muder ")
    
        elif user_input<=18:
             print("doing study ")
    else:
        print("invalid input ")



       