#program for admission booths

ticket = 30

age = float(input("enter your age:"))

if age > 65:
    print("you get a 50% discount", 0.5*ticket)

elif age < 6:
    print("Free", 0*ticket)

else:
    print("pay the whole amount", ticket)

#given the year 2016
#check whether it is a leap year or not
