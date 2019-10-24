# function to find the largest of 3 variables

def maximum(a, b, c):
    variables = [a, b, c]
    return max(variables)

a = 8
b = 10
c = 15

print(max(a, b, c))


def maximum(x, y, z):
    if (x >= y) and (x >= y):
        largest = x

    elif (y >= x) and (y >= x):
        largest = y
    else:
        largest = z

    return largest

x = 50
y = 70
z = 56

print(max(x, y, z))