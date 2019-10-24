# given a number, check if it is negative,positive or zero

number = int(input("enter a number:"))

if number < 0:
    print("negative number")

elif number > 0:
    print("positive number")

elif number == 0:
    print("zero")

else:
    print("not a number")
