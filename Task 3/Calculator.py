class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        print("Addition:", self.num1 + self.num2)

    def subtraction(self):
        print("Subtraction:", self.num1 - self.num2)

    def multiplication(self):
        print("Multiplication:", self.num1 * self.num2)

    def division(self):
        print("Division:", self.num1 / self.num2)


cal = Calculator(20, 10)

cal.addition()
cal.subtraction()
cal.multiplication()
cal.division()