# print a multiplication table

number = int(input("enter your number:"))

print("multiplication table of", number)

for i in range(1, 13, 1):
    print(number * i)
