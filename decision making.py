#decision making....control statements
points = float(input("what are your points?"))
name = str(input("Enter your name"))

#use if, if else, elif
#conditional operators: >,>=,<,<=, ==(equal to),!=(not equal to)
#logical operators: and, or, not


if points <= 100:
    print("your points are",points)
    print("you do not qualify to move to the next level")

else:
    print("your points are", points)
    print("congratulations you move to the next level")

if name == "modcom":
    print("welcome to modcom")

else:
    print("sorry,your name was", name)


password = str(input("enter your password"))
if len(password)<8:
    print("password is too short")
else:
    print("password is fine")

#NB if else works for one condition