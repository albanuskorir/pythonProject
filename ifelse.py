# write a program to find the largest of 3 numbers.
num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))
num3 = int(input("enter the third number: "))
if num1 > num2 and num1 > num3:
    print("num1 is the largest")
elif num2 > num1 and num2 > num3:
    print("mum2 is the largest")
else:
    print("num3 is largest")
    print(num1)
    print(num2)
    print(num3)
