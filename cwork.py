# find the area of a circle (PI R^2)
r = int(input("Input radius= "))
pi = 3.142
area = (pi * r ** 2)
print(area)

#  write a program to prompt the user for hours worked, rate per hour and to compute gross-pay
#  (gross_pay = hours_worked * rate_per_hour)

hours_worked = int(input("Enter hours worked: "))
rate_per_hour = float(input("Enter rate: "))
gross_pay = int(input("enter gross pay: "))
gross_s = (hours_worked * rate_per_hour)
print(gross_s)

# create a list to display the following indexes
list = [0, 1, 2, 3, 4, 5]
print(list[-1])
print(list[:1])
print(list[2:4])
list.pop()
print(list)
list.reverse()
print(list)
print(6 in list)  # should return false 6 are not on the list
print(0 in list)  # should return true bcz 0 are in the list

