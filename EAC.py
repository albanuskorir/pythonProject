# write a program to check if you are eligible to vote: and you must be an East African Citizen (Kenya, Tanzania, Uganda, and above 18 years)
age = int(input("Enter your age: "))
country = input("country: ").caption()
counries = ["Kenya", "uganda", "Tanzania"]
if age >= 18 and "country" in "countries":
    print("Eligible to vote")
else:
    print("Not Eligible to vote")
    print(age)
    print(country)

