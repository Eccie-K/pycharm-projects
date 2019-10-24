# calculating the number of units or electricity
def electricity(units):
    if units <80:
        print("your charge is:", units*3.40)

    elif units >80 and units <1050:
        print("your charge is:", units*4)

    elif units >1050 and units <2000:
        print("your charge is:", units*4.50)
    elif units>2000:
        print("your charge is", units*5.20)

electricity(units = 5000)

