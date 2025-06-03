# method_overloading/calculator_example.py
class Calculator:
    def add(self, *args):
        if len(args) == 2 and all(isinstance(x, (int, float)) for x in args):
            # Traditional addition of two numbers
            return args[0] + args[1]
        elif len(args) > 2 and all(isinstance(x, (int, float)) for x in args):
            # Sum of multiple numbers
            return sum(args)
        elif len(args) == 1 and isinstance(args[0], list):
            # Sum of a list of numbers
            return sum(args[0])
        else:
            raise TypeError("Invalid input types for addition")

# Usage
calc = Calculator()
print(calc.add(5, 3))          # 8
print(calc.add(1, 2, 3, 4))    # 10
print(calc.add([1, 2, 3, 4]))  # 10