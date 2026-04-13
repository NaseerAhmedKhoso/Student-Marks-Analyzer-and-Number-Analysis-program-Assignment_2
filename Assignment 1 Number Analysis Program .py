even_count = 0

for i in range(1, 11):
    if i % 2 == 0:
        print(i, "Even", end="")
        even_count += 1
    else:
        print(i, "Odd", end="")
        odd_count+=1
    if i % 3 == 0:
        print(", Divisible by 3")
    else:
        print()

print("Total even numbers:", even_count)






