# Python Fundamentals & Problem Solving 

# Learning Outcomes assessed:

- Understanding of basic Python syntax
- Conditional statements
- Functions
- Basic loops
- Simple algorithms (problem solving)
- Basic command-line commands

---

# Assessment Structure

This assessment has two sections:

- **Form-based assessment:** multiple-choice questions and written responses about Python syntax, conditions, loops, functions, algorithms, and command-line commands.
- **Coding assessment:** complete the five functions described below and make the supplied unit tests pass.

You can answer the questions in any order.

## Scoring & Weighting

| Component | Weight |
| --- | ---: |
| Coding Section (unit tests) | **50%** |
| Form-Based Section (MCQs + written responses) | **50%** |

### Coding section

Your coding score is determined by the number of tests you pass.

```text
Coding Score = (P / T) × 50%
```

Where `T` is the total number of coding tests and `P` is the number of tests passed.

### Form-based section

Your form-based score is determined by the correct responses on the assessment form.

```text
Form Score = (C / Q) × 50%
```

Where `Q` is the total number of questions and `C` is the number answered correctly.

### Final Score & Pass Mark

```text
Final Score = Coding Score + Form Score
```

To pass the overall assessment, your final score must be **60% or higher**.

---

## Important: Set up the environment

Run these commands in order from the project directory:

```bash
chmod +x setup_environment.sh
./setup_environment.sh
```

If Python and pytest are already installed, you can skip the setup script and run:

```bash
python3 -m pytest tests/test_fundamentals.py -v
```

To run one test method:

```bash
python3 -m pytest tests/test_fundamentals.py::TestFunctions::test_print_multiples_output -v
```

Useful command-line commands include `pwd` (show current directory), `ls` (list files), `cd` (change directory), `mkdir` (create a directory), and `python3 -m pytest` (run tests).

---

# Fundamentals Coding Assessment — Version 2

This assessment consists of five Python functions. Each function has a partially written implementation. Your task is to **fix the bugs**, **complete the missing logic**, and **ensure all tests pass**.

## Project Structure

```text
fun-000-syntax-v2/
├── fundamentals.py
├── tests/
│   └── test_fundamentals.py
├── setup_environment.sh
└── README.md
```

## Question 1 — `print_multiples(n)`

Complete `print_multiples(n)` so it prints every positive multiple of **3** from `1` through `n`, inclusive. Print one number per line and print nothing if `n` is less than `1`.

Example:

```text
Input:  10
Output:
3
6
9
```

This question assesses function calls, loops, ranges, and output.

## Question 2 — `sum_is_odd(n)`

Calculate the sum of all integers from `1` through `n`, inclusive. Return `True` if that sum is odd and `False` if it is even. If `n` is less than `1`, return `False`.

Example: for `n = 3`, the sum is `1 + 2 + 3 = 6`, so the function returns `False`.

This question assesses variables, arithmetic, loops, and Boolean conditions.

## Question 3 — `countdown_odd(n)`

Print all odd numbers from `n` down to `1`, in descending order, one number per line. If `n` is less than `1`, print nothing.

Example:

```text
Input:  6
Output:
5
3
1
```

This question assesses `while` or `for` loops, conditionals, and updating a loop variable correctly.

## Question 4 — `classify_number(n)`

Return a label based on the integer supplied:

| Condition | Required return value |
| --- | --- |
| `n` is less than zero | `"Negative"` |
| `n` equals zero | `"Zero"` |
| `n` is positive and even | `"Positive Even"` |
| `n` is positive and odd | `"Positive Odd"` |

Use the exact capitalization and spacing shown. This question assesses `if` / `elif` / `else` and the modulo operator (`%`).

## Question 5 — `count_vowels(text)`

Return the number of vowels (`a`, `e`, `i`, `o`, `u`) in the supplied string. Count uppercase and lowercase vowels equally. Do not count `y` as a vowel. An empty string should return `0`.

Examples:

```text
Input:  "Hello World"
Output: 3

Input:  "PYTHON"
Output: 1
```

This question assesses string handling, loops, membership checks, and simple problem solving.

## Your Goal

Fix all functions in `fundamentals.py` so that:

- The code is valid Python.
- Every function follows its specification.
- The supplied unit tests pass.
- You can explain which loops, conditions, operators, and command-line commands you used.

Good luck!
