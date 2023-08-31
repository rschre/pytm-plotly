from unittest import TestCase

from app import Exercise


class Test(TestCase):
    def test_wrong_result(self):
        assert Exercise.check(1, 0, 0) != 1
        assert Exercise.check(0, 0, 1) != 1
        assert Exercise.check(2, 3, 5) != 0

    def test_correct_result(self):
        assert Exercise.check(1, 0, 0) == 0
        assert Exercise.check(0, 0, 1) == 0
        assert Exercise.check(2, 3, 5) == 1
