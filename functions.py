
"""Useful mathematical functions in Python."""


def greet_user(name):
    """Display a personalized greeting."""
    return f"Welcome, {name}! Let's learn Python."


def check_prime(number):
    """Check whether a number is prime."""
    if number < 2:
        return False

    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False

    return True


def calculate_factorial(number):
    """Return the factorial of a non-negative integer."""
    if number < 0:
        raise ValueError("Factorial cannot be calculated for negative numbers.")

    answer = 1
    for value in range(1, number + 1):
        answer *= value

    return answer


if __name__ == "__main__":
    print(greet_user("Itika Saxena"))
    print("Is 23 a prime number?", check_prime(23))
    print("Factorial of 6:", calculate_factorial(6))
