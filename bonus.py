# write a program to calculate the bobus of emplyees
salary = int(input("Enter your salary: "))
years = int(input("Enter year of service: "))
if years > 10:
    print(salary * 0.1)
elif years >= 6 and years <= 10:
    print(salary * 0.08)
else:
    print(salary * 0.05)
    print(salary)
    print(years)
