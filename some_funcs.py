def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b * a  # FAIL


def divide(a, b):
    if b == 0:
        raise ValueError("Делитель не может быть нулем.")
    return a / b


print(add(3, 4))
