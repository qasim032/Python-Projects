while True:
    try:
        number = int (input("What's the number? "))
        if number%2==0:
            print("The number is Even")
        else:
            print("The number is odd")
        break
    except ValueError:
        print("Invalid input. Please enter integers only.")   
#4m