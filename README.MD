# Calculator

Calculator class performing these mathematical functions:
- addition,
- subtraction,
- multiplication,
- division,
- X root of number.
- Also includes function to reset value back to 0.
# Table of contents

- [Calculator](#Calculator)

- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

# Installation
[(Back to top)](#table-of-contents)


``` python
> pip install git+https://github.com/GoldenDawn369/calculator
```

``` python
>>> from calculator.calculator import Calculator
```



# Usage
[(Back to top)](#table-of-contents)

After installation is done the you'll have to instantiate a Calculator class and play with it by running methods:
```python
>>> calc = Calculator()
>>> calc.add(3)
3.0
>>> calc.subtract(-7)
10.0
>>> calc.multiply(42)
420.0
>>> calc.divide(7)
60.0
calc.root(-1)
0.016666666666666666
>>> calc.reset()
0.0
>>> calc.value = 7 #Calls setter to set value to 7
7
>>> print(calc.value) # Calls getter to return current value
7

```


# License
[(Back to top)](#table-of-contents)


[LICENSE](https://github.com/GoldenDawn369/calculator/blob/main/LICENSE.txt)
