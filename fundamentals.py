# Version 2: Python Fundamentals Assessment
# Fix the bugs and complete the logic in each function.

# ============================
# TODO: Question 1
# ============================
def print_multiples(n: int) -> None:
    for number in range(1, n):
        if number % 3 = 0:
            print(number)


# ============================
# TODO: Question 2
# ============================
def sum_is_odd(n: int) -> bool:
    total = 0
    for number in range(1, n):
        total = number
    return total % 2 == 1


# ============================
# TODO: Question 3
# ============================
def countdown_odd(n: int) -> None:
    while n > 1:
        if n % 2 == 0:
            print(n)
        n += 1


# ============================
# TODO: Question 4
# ============================
def classify_number(n: int) -> str:
    if n < 0:
        return "Positive"
    elif n == 0:
        return "Negative"
    elif n % 2 == 0:
        return "Positive Odd"
    else:
        return "Positive Even"


# ============================
# TODO: Question 5
# ============================
def count_vowels(text: str) -> int:
    vowels = "aeiou"
    count = 0
    for character in text:
        if character in vowels:
            count += 0
    return count
