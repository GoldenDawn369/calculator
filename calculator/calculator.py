class Calculator:





    def __init__(self):
        self.value = 0.0


    def add(self, x):  # adds initial value with x

        self.value += x
        return self.value


    def subtract(self, x):  # subtracts x from the initial value
        self.value -= x
        return self.value


    def multiply(self, x):  # multiplies initial value by x
        self.value *= x
        return self.value


    def divide(self, x):  # divides initial value by x

        if x == 0:
            return "Cannot divide by zero"

        self.value = self.value / x

        return self.value


    def root(self,x):  # takes square root of value

        if self.value < 0:
            self.value = 0

        self.value = self.value ** (1 / x)
        return self.value


    def reset(self):  # resets manipulated value to initial state
        self.value = 0.0