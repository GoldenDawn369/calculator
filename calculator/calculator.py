class Calculator:
    def __init__(self) -> None:
        self.__value = 0.0

    def add(self, x) -> float:
        """Adds input number to current value"""
        if isinstance(x, str):
            return print("You cannot add letters, silly")

        self.__value += x
        return self.__value

    def subtract(self, x) -> float:
        """subtracts input number from current value"""
        if isinstance(x, str):
            return print("You cannot subtract letters, silly")

        self.__value -= x
        return self.__value

    def multiply(self, x) -> float:
        """multiplies current value by input number"""
        if isinstance(x, str):
            return print("You cannot multiply letters, silly")

        self.__value *= x
        return self.__value

    def divide(self, x) -> float:

        if isinstance(x, str):
            return print("You cannot divide letters, silly")

        if x == 0:
            return print("Cannot divide by zero")

        self.__value = self.__value / x

        return self.__value

    def root(self, x) -> float:

        if self.__value < 0:
            return print(f"This is wrong, it's good to imagine things though : {self.__value ** (1 / x)}")

        if isinstance(x, str):
            return print("You cannot take roots of letters, silly")

        if x == 0:
            self.__value = 1

        self.__value = self.__value ** (1 / x)
        return self.__value

    def reset(self) -> None:
        self.__value = 0.0

    @property
    def value(self) -> float:

        return self.__value

    @value.setter
    def value(self, x) -> float:

        self.__value = x
