#nested loops: aloop within a loop

for x in range(1, 20, 1): #parent loop
    print("*")
    for i in range(1, x, 1): #child loop
        print("#", end="") # end ="" prints horizontally
