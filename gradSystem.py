# Prompt the student to enter their marks to the system and calculate the grade
def grading_system(sum):
    infosec = int(input("Enter inforsec marks: "))
    python = int(input("Enter python marks: "))
    software = int(input("Enter software marks: "))
    sum = int(infosec + python + software)
    avg = sum/3
    if avg >=70 and avg <= 100:
        print("A")
    elif avg >=60 and avg <= 69:
        print("B")
    elif avg >= 50 and avg <= 59:
        print("C")
    elif avg >= 40 and avg <= 49:
        print("D")
    elif avg >= 0 and avg <= 39:
        print("Fail!")
    else:
        print("Out of range!!!")
        return sum


print(grading_system(sum))
