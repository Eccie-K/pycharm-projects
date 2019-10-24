def BMI(height, weight):
    bmi = weight/(height**2)
    return bmi

# real code

height = 1.7
weight = 58
bmi = weight/(height**2)
print("your BMI is:", format(bmi) )

if bmi<=18:
    print("underweight")
elif bmi>=18 and bmi < 25:
    print("you are healthy")
elif bmi>=25 and bmi <35:
    print("overweight")
else:
    if bmi >= 35:
        print("obese")



