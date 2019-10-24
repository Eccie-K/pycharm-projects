def simple_interest(principle, rate, time):
    #principle = 45000
    #rate = 1.5
    #time = 24

    answer = principle*rate*time/100
    print("your simple interest is", answer)

simple_interest(principle = 500000, rate = 1.2, time = 24)
simple_interest(principle = 70000, rate = 1.2, time = 24)
simple_interest(principle = 3000000, rate = 1.2, time = 24)

#function that the area of a triangle

def area_triangle(base, height):
    area = 0.5*base*height
    print("area =", area)

area_triangle(base = 7, height = 12)
area_triangle(base = 2, height = 10)
area_triangle(base = 18, height = 6)