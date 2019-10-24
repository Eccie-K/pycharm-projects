# checking whether a year is leap or not

year = int(input("enter the year in numbers:"))

if year % 4 != 0:
    print("this is not a leap year")
elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
    print("it is a leap year")

elif year % 4 == 0 and year % 100 != 0:
    print("leap year")

else:
    print("leap year")