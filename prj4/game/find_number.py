from enum import Enum


class Way(Enum):
    BIGGER = 0
    SMALLER = 1
    EQUAL = 2


class FindNumberGame:
    def __init__(self, secret_number: int):
        self.secret_number = secret_number

    def try_number(self, given_number: int) -> Way:
        if given_number > self.secret_number:
            return Way.BIGGER
        else:
            return Way.SMALLER
