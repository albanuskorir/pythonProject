# Create a class named Temperature. Make two methods:
# i) convert_fahrenheit - it will take celsius and print it into fahrenheit
# i) convert_celsius - it will take fahrenheit and will convert  it into celsius
class Temperature:
    def __init__(self, convert_fahrenheit, convert_celsius):
        self.convert_fahrenheit = convert_fahrenheit
        self.convert_celsius = convert_celsius

    def fahrenheit(self):
        return (self.convert_celsius * 1.8) + 32

    def celsius(self):
        return (self.convert_fahrenheit * 1.8) - 32


Temp = Temperature(30, 45)
print(Temp.fahrenheit())
print(Temp.celsius())