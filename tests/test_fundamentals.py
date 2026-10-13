from io import StringIO
import sys

import fundamentals as fun


class TestFunctions:
    def capture_output(self, function, *args):
        captured = StringIO()
        original_stdout = sys.stdout
        try:
            sys.stdout = captured
            function(*args)
        finally:
            sys.stdout = original_stdout
        return captured.getvalue().strip().splitlines() if captured.getvalue().strip() else []

    def test_print_multiples_output(self):
        cases = [
            (10, ["3", "6", "9"]),
            (3, ["3"]),
            (2, []),
            (0, []),
            (-5, []),
            (15, ["3", "6", "9", "12", "15"]),
        ]
        for n, expected in cases:
            assert self.capture_output(fun.print_multiples, n) == expected

    def test_sum_is_odd(self):
        cases = [
            (1, True),
            (2, True),
            (3, False),
            (4, False),
            (5, True),
            (6, True),
            (7, False),
            (0, False),
            (-3, False),
        ]
        for n, expected in cases:
            assert fun.sum_is_odd(n) is expected

    def test_countdown_odd_output(self):
        cases = [
            (6, ["5", "3", "1"]),
            (7, ["7", "5", "3", "1"]),
            (1, ["1"]),
            (0, []),
            (-2, []),
            (10, ["9", "7", "5", "3", "1"]),
        ]
        for n, expected in cases:
            assert self.capture_output(fun.countdown_odd, n) == expected

    def test_classify_number(self):
        cases = [
            (-10, "Negative"),
            (-1, "Negative"),
            (0, "Zero"),
            (1, "Positive Odd"),
            (2, "Positive Even"),
            (13, "Positive Odd"),
            (24, "Positive Even"),
        ]
        for n, expected in cases:
            assert fun.classify_number(n) == expected

    def test_count_vowels(self):
        cases = [
            ("Hello World", 3),
            ("PYTHON", 1),
            ("aeiou", 5),
            ("AEIOU", 5),
            ("rhythm", 0),
            ("", 0),
            ("Programming is fun!", 5),
            ("123!?", 0),
        ]
        for text, expected in cases:
            assert fun.count_vowels(text) == expected

    def test_functions_exist(self):
        for name in (
            "print_multiples",
            "sum_is_odd",
            "countdown_odd",
            "classify_number",
            "count_vowels",
        ):
            assert callable(getattr(fun, name, None)), f"{name} should be defined"
