while True:
    try:
        age = int (input("What's your age ? "))
        if age<18:
            print("You are child.")
        elif age<25:
            print("You are adult")
        elif age<51:
           print("You are young")
        elif age<80:
           print("You are old")
        elif age<100:
            print("Do or die")
        else:
            print("You are alien")
        break
    except ValueError:
        print("Invalid input. Please enter integers only.")
#5m