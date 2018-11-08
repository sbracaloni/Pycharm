A_CONSTANT = 45


def a_sum_function(a: int, b: int) -> int:
    return a + b


def a_mult_function(a: int, b: int) -> int:
    return a * b


class ACarClass:
    def __init__(self, color: str, speed: int):
        self.color = color
        self.speed = speed

    def describe(self) -> str:
        return f'I am a {self.color} car, with a speed of {self.speed} km/h'
