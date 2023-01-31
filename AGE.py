age = int(input("Enter your age: "))
nationality =input("Enter your nationality: ").lower()
if (age >= 18) and (nationality == "Kenyan"):
    print("eligible to vote")
else:
    print("you are not eligible to vote")
    print(age)
    print(nationality)
