pass_count = 0
fail_count = 0
highest = 0

for i in range(1, 6):
    marks = int(input("Enter marks for student: "))

    if marks >= 80:
        print("Student", 1, ": A-Excellent")
        pass_count += 1
    elif marks >= 60:
        print("Student", 2, ": B-Great")
        pass_count += 1
    elif marks >= 50:
        print("Student", 3, ": C-Passing")
        pass_count += 1
    else:
        print("Student", 4, ":Fail")
        fail_count += 1

    if marks > highest:
        highest = marks

print("Total Passed:", pass_count)
print("Total Failed:", fail_count)
print("Highest Marks:", highest)