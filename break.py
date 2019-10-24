# break statement immediately terminates a loop entirely
# continue statement immediately terminates the current loop  iteration

n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)

print("end of loop")

#When n becomes 2, the break statement is executed. The loop is terminated completely, and program execution jumps to the print() statement on line 7.



n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)

print("end of loop")
#This time, when n is 2, the continue statement causes termination of that iteration. Thus, 2 isn’t printed. Execution returns to the top of the loop, the condition is re-evaluated, and it is still true. The loop resumes, terminating when n becomes 0, as previously.



