print(20 / 6)  # return answer with decimal part
print(20 // 6)  # return number without decimal part
# use to test if number you enter is divisible by 5
a = int(input("enter number: "))
if a % 2 == 0:
    print("a, is even number")
else:
    print("a, is odd number")
    print(a)

a = int(input("Enter amount purchase: "))
if a > 1000:
    print(a*0.05)
    print("discount= ", a*0.05)
else:
    print("no discount charged")
    print(a)


age = int(input("Enter your age: "))
nationality =(input("Enter your nationality: "))
if (age >= 18) and (nationality == "Kenyan" or "KENYAN" or "Kenyan"):
    print("eligible to vote")
else:
    print("you are not eligible to vote")
    print(age)
    print(nationality)


