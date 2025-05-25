while True:
    try:
        number1 = int(input("What's the first number:  "))
        number2 = int(input("What's the second number:  "))
        operation = input("Enter the operation you want to perform +,-,*,/,%: ")
    except ValueError:
        print("Invalid input. Please enter integers only.")
        continue
    match operation:
        case '+':
            print("The sum is ",number1+number2)
            break
        case '-':
            print("The subtraction is ",number1-number2)
            break
        case '*':
            print("The multiplication is ",number1*number2)
            break
        case '/':
            try:
                print("The division is ",number1/number2)
                break
            except ZeroDivisionError:
                print("Couldn't divide integer by zero causing infinity")
                continue
        case '%': 
            try:
                print("The remainder is ",number1%number2)
                break
            except ZeroDivisionError:
                print("Couldn't divid integer by zero causing infinity")
                continue
        case _:
            print("Invalid operation")
            continue
#16m