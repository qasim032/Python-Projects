num = int(input("What's num? "))
if (num % 400 == 0):
    print("It is a leap year")  # 1600, 2000 are leap years
elif (num % 100 == 0):
    print("It is not a leap year")  # 1900, 2100 are not leap years
elif (num % 4 == 0):
    print("It is a leap year")  # 2020, 2024 are leap years
else:
    print("It is not a leap year")  # 2021, 2023 are not leap years