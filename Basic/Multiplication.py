number = int(input("What is the number? "))
print(f"The table of {number} is: ")
for i in range(1,11):
    print(f"{number} * {i} = {number*i}")