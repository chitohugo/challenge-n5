import random


def generator_id():
    first_digit = random.randint(1, 9)
    other_digits = random.randint(0, 999)
    code = first_digit * 1000 + other_digits

    return code

