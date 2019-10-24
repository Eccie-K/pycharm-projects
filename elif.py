#elif
#for multiple conditions

points = float(input("enter your points"))

if points <= 100:
    print("you do not qualify")
elif points >100 and points <=500:
    print("you win a smart phone!")

elif points >500 and points <=1000:
    print("you win a tablet")

elif points>1000 and points <=5000:
    print("congratulations you win a trip to dubai")

else:
    print( "You won a car")
    if points>10000 and points <=20000:#nested  if statement
        print("you win a rav4")
    else:
        print("you won a crown")
