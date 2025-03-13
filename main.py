class Calculator:
    def __init__(self):
        self.operations = {
            "+": self.add,
            "-": self.subtract,
            "*": self.multiply,
            "/": self.divide,

        }

    def add(self, x, y):
        return x + y
    def subtract(self, x, y):
        return x - y
    def multiply(self, x, y):
        return x * y
    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            raise ZeroDivisionError("Cannot divide by zero")
        

#TEST CASE
if __name__ == "__main__":
    answer = Calculator()
    result = answer.operations["+"](10, 4)
    print(f"the subtraction of {10} - {4} = {Calculator.subtract(0 ,10, 4)}")

    result = answer.operations["-"](3, 4)
    print(result)

    result = answer.operations["*"](3, 4)
    print(result)

    result = answer.operations["/"](3, 4)
    print(result)
