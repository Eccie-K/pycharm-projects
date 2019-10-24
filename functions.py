#function is a block of code  that perfoms a speciic task
# functions are defined
# functions are called by themselves

def addition():
    x = 2
    y = 4
    z = 10
    answer = x+y+z
    print("total sum", answer)


def school_grading():
    marks = 20
    if marks <= 50:
        print("you failed")
    else:
        print("you passed")

#functions are written in small letters

def division():
    q = 10
    w = 2
    div = q/w
    print("answer =", div)


# find the area of a triangle - 0.5bh

def triangle_area():
    base = 5
    height = 7
    area = 0.5*(base*height)
    print("area=", area)


# create a function to check the largest or equal from two variables

def large_equal():
    a = 5
    b = 7
    print(max(a, b))



division()
triangle_area()
large_equal()

# advantages of using functions
# 1.splits a large code into small programs
# 2. Simplicity and easy reading of code
# 3. Functions can be used severally
# Functions are neede in object oriented programming


