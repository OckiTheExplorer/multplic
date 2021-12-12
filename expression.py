
import random

_INPUT_STR = "_____"
OPERATORS = ["×", "+", "-", "/"]


class NoOperatorsError(Exception):
    """Raised when the input operators are empty."""
    pass


class NotEnoughMathProblems(Exception):
    """Raised when nrow*ncol is smaller than max_problems."""
    pass
class Expressions:

    def  __init__(self, nrow, ncol, operators, lhs_ints, rhs_ints, repeating):
        self.nrow = nrow
        self.ncol = ncol
        self.N = self.nrow * self.ncol

        self.lhs_ints = lhs_ints
        self.rhs_ints = rhs_ints
        self.max_problems = len(lhs_ints) * len(rhs_ints) * len(operators)

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
            raise NoOperatorsError("A test cannot be generate without operators.")

        if self.max_problems < self.N and not self.repeating:
            raise NotEnoughMathProblems(f"Not enough math problems. The number of possible math problems, {self.max_problems}, must be equal to or greater than the number of requested math problems, {self.N}.")
        
    def _set_repeating_exps(self, exp_types):

        self.expressions = [exp_types[self._random_sign()](self._random_int(self.lhs_ints), self._random_int(self.rhs_ints)) for i in range(self.N)]

    def _set_non_repeating_exps(self, exp_types):

        records_dict = {}
        while len(records_dict) < self.N:


            record = exp_types[self._random_sign()](self._random_int(self.lhs_ints), self._random_int(self.rhs_ints))
            
            records_dict[record.txt] = record

        self.expressions = list(records_dict.values())
        
    def _random_sign(self):
        return self.operators[random.randint(0, len(self.operators)) - 1]

    def _random_int(self, ints):
        return ints[random.randint(0, len(ints)) - 1]


class Addition:

    def __init__(self, x, y):

        self.x = x
        self.y = y
        self.rhs = x + y
        self.txt = f"{x} + {y} = {_INPUT_STR}"        
        self.answer = f"{x} + {y} = {self.rhs}"

class Subtraction:

    def __init__(self, x, y):

        self.x = x
        self.y = y
        self.rhs = x - y
        self.txt = f"{x} - {y} = {_INPUT_STR}"        
        self.answer = f"{x} - {y} = {self.rhs}"

class Multiplication:

    def __init__(self, x, y):

        self.x = x
        self.y = y
        self.rhs = x * y
        self.txt = f"{x} × {y} = {_INPUT_STR}"        
        self.answer = f"{x} × {y} = {self.rhs}"

class Division:

    def __init__(self, divident, rhs):

        self.rhs = rhs
        self.y = divident
        self.x = divident * rhs
        self.txt = f"{self.x} / {self.y} = {_INPUT_STR}"        
        self.answer = f"{self.x} / {self.y} = {self.rhs}"