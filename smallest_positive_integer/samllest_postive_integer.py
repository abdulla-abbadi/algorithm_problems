import unittest

"""
Problem:
    Given an array A with N integers find the smallest positive integer that is not in A.

    Examples:

    A = [4, 2, 3, 1, 6] => 5
    A = [3, 1, 2] => 4
    A = [-1, -3, -2] => 1
    A = [-3, -4, 0, 1, 3] => 2

"""
def find_the_smallest_postive_integer(a):
    cur = 0
    for n in a:
        if cur - n == -1:
            cur = n
        elif cur - n < -1:
            return cur + 1
    return cur + 1



"""----------- tests -------------------"""
class TestFindTheSmallestIntegerMethod(unittest.TestCase):

    def test_the_smallest_within_the_range(self):
        a = [1, 2, 3, 5, 6]
        EXPECTED = 4
        current = find_the_smallest_postive_integer(a)
        self.assertEqual(current, EXPECTED)

    def test_the_smallest_out_of_the_range(self):
        a = [1, 2, 3, 4]
        EXPECTED = 5
        current = find_the_smallest_postive_integer(a)
        self.assertEqual(current, EXPECTED)

    def test_all_negative_integers(self):
        a = [-1, -2, -3]
        EXPECTED = 1
        current = find_the_smallest_postive_integer(a)
        self.assertEqual(current, EXPECTED)

    def test_mixed_negative_and_positive_integers(self):
        a = [-1, -3, 0, 1, 3]
        EXPECTED = 2
        current = find_the_smallest_postive_integer(a)
        self.assertEqual(current, EXPECTED)


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    unittest.main(testRunner=runner)