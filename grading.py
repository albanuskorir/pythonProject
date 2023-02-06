# write a program to create a grading system using the following condition
# score    grade
# 70-100    A
# 60-69     B
# 50-59     C
# 40-49     D
# 0-39      Fail
Bio = int(input("Enter Bio: "))
Chem = int(input("Enter Chem: "))
Comp = int(input("Enter Comp: "))
sum = int(Bio + Chem + Comp)
avg = sum/3
if avg >=70 and avg <= 100:
    print("your grade is A")
elif avg >=60 and avg <= 69:
    print("Your grade is B")
elif avg >= 50 and avg <= 59:
    print("Your grade is C")
elif avg >=40 and avg <= 49:
    print("Your garde is D")
elif avg >=0 and avg <=39:
    print("Fail")
else:
    print("out of range")

