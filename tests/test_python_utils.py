import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "python"))
sys.path.insert(0, str(ROOT / "algorithms"))

from text_utils import normalize_whitespace, word_count, is_palindrome
from validators import is_valid_email, is_indian_pin_code, is_strong_password
from statistics_utils import mean, describe
from searching import linear_search, binary_search
from sorting import merge_sort, quick_sort
from structures import Stack, Queue


class TextUtilsTests(unittest.TestCase):
    def test_normalize_whitespace(self):
        self.assertEqual(normalize_whitespace("  hello   world "), "hello world")

    def test_word_count(self):
        self.assertEqual(word_count("One, two; three!"), 3)

    def test_palindrome_ignores_punctuation(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))

    def test_not_palindrome(self):
        self.assertFalse(is_palindrome("python"))


class ValidatorTests(unittest.TestCase):
    def test_email_structure(self):
        self.assertTrue(is_valid_email("student@example.com"))
        self.assertFalse(is_valid_email("bad-address"))

    def test_pin_code(self):
        self.assertTrue(is_indian_pin_code("831001"))
        self.assertFalse(is_indian_pin_code("031001"))

    def test_password_policy(self):
        self.assertTrue(is_strong_password("Strong#123"))
        self.assertFalse(is_strong_password("weak"))


class StatisticsTests(unittest.TestCase):
    def test_mean(self):
        self.assertEqual(mean([2, 4, 6]), 4)

    def test_describe(self):
        result = describe([1, 2, 3])
        self.assertEqual(result["median"], 2)
        self.assertEqual(result["count"], 3)

    def test_empty_mean_rejected(self):
        with self.assertRaises(ValueError):
            mean([])


class AlgorithmTests(unittest.TestCase):
    def test_search(self):
        self.assertEqual(linear_search([4, 7, 9], 7), 1)
        self.assertEqual(binary_search([4, 7, 9], 9), 2)
        self.assertEqual(binary_search([], 2), -1)

    def test_sorting(self):
        values = [5, 1, 3, 3, -2]
        self.assertEqual(merge_sort(values), [-2, 1, 3, 3, 5])
        self.assertEqual(quick_sort(values), [-2, 1, 3, 3, 5])
        self.assertEqual(values, [5, 1, 3, 3, -2])

    def test_stack_and_queue(self):
        stack = Stack()
        stack.push("a")
        self.assertEqual(stack.pop(), "a")
        queue = Queue()
        queue.enqueue("first")
        queue.enqueue("second")
        self.assertEqual(queue.dequeue(), "first")


if __name__ == "__main__":
    unittest.main()
