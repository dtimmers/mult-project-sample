from unittest import TestCase


class TestBase(TestCase):

    def test_base(self):
        self.assertListEqual(["a", "a", "a"], 3 * ["a"])
