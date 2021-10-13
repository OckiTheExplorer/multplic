
import random

_INPUT_STR = "_____"
OPERATORS = ["×", "+", "-", "/"]


class NoOperatorsError(Exception):
    """Raised when the input operators are empty."""
    pass
class Expressions:

    def  __init__(self, nrow, ncol, operators, repeating):

        
        self.nrow = nrow
        self.ncol = ncol
        self.N = self.nrow * self.ncol
        self.operators = operators
        self.repeating = repeating
        self.expressions = []

        self._check_input()

        exp_types = {
            "+": Addition,
            "-": Subtraction,
            "×": Multiplication,
            "/": Division}

        if repeating:
            self._set_repeating_exps(exp_types)
        else:
            self._set_non_repeating_exps(exp_types)

    def _check_input(self):
        if len(self.operators) == 0:
            raise NoOperatorsError("[operators] cannot be empty.")
        
    def _set_repeating_exps(self, exp_types):

        self.expressions = [exp_types[self._random_sign()](random.randint(1, 10), random.randint(1, 10)) for i in range(self.N)]

    def _set_non_repeating_exps(self, exp_types):
        records_dict = {}
        while len(records_dict) < self.N:
            record = exp_types[self._random_sign()](random.randint(1, 10), random.randint(1, 10))
            records_dict[record.txt] = record

        self.expressions = list(records_dict.values())

        
        
    def _random_sign(self):
        return self.operators[random.randint(0, len(self.operators)) - 1]


class Addition:

    def __init__(self, x, y):

        self.x = x
        self.y = y
        self.txt = f"{x} + {y} = {_INPUT_STR}"        
        self.answer = f"{x} + {y} = {x + y}"

class Subtraction:

    def __init__(self, x, y):

        self.x = x
        self.y = y
        self.txt = f"{x} - {y} = {_INPUT_STR}"        
        self.answer = f"{x} - {y} = {x - y}"

class Multiplication:

    def __init__(self, x, y):

        self.x = x
        self.y = y
        self.txt = f"{x} × {y} = {_INPUT_STR}"        
        self.answer = f"{x} × {y} = {x * y}"

class Division:

    def __init__(self, x, y):

        self.x = x
        self.y = y
        self.txt = f"{x} / {y} = {_INPUT_STR}"        
        self.answer = f"{x} / {y} = {round(x / y, 2)}"