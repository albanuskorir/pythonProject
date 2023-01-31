age = int(input("Enter your age: "))
m_income = int(input("Enter your monthly income: "))

if age >= 21 and m_income >= 21000:
    print("Congratulation you qualify for loan")
else:
    print("unfortunately, we are unable to offer you a loan at this time")
    print(age)
    print(m_income)
