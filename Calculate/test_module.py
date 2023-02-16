import unittest
import mean_var_std


class UnitTests(unittest.TestCase):
    def test_calculate(self):
        actual = mean_var_std.calculate([2, 6, 2, 8, 4, 0, 1, 5, 7])
        expected = {
            "mean": [
                [3.6666666666666665, 5.0, 3.0],
                [3.3333333333333335, 4.0, 4.333333333333333],
                3.888888888888889,
            ],
            "variance": [
                [9.555555555555557, 0.6666666666666666, 8.666666666666666],
                [3.555555555555556, 10.666666666666666, 6.222222222222221],
                6.987654320987654,
            ],
            "standard deviation": [
                [3.091206165165235, 0.816496580927726, 2.943920288775949],
                [1.8856180831641267, 3.265986323710904, 2.494438257849294],
                2.6434171674156266,
            ],
            "max": [[8, 6, 7], [6, 8, 7], 8],
            "min": [[1, 4, 0], [2, 0, 1], 0],
            "sum": [[11, 15, 9], [10, 12, 13], 35],
        }
        self.assertAlmostEqual(
            actual,
            expected,
            "Expected different output when calling 'calculate()' with '[2,6,2,8,4,0,1,5,7]'",
        )

    def test_calculate2(self):
        actual = mean_var_std.calculate([9, 1, 5, 3, 3, 3, 2, 9, 0])
        expected = {
            "mean": [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
            "variance": [
                [6.0, 6.0, 6.0],
                [0.6666666666666666, 0.6666666666666666, 0.6666666666666666],
                6.666666666666667,
            ],
            "standard deviation": [
                [2.449489742783178, 2.449489742783178, 2.449489742783178],
                [0.816496580927726, 0.816496580927726, 0.816496580927726],
                2.581988897471611,
            ],
            "max": [[6, 7, 8], [2, 5, 8], 8],
            "min": [[0, 1, 2], [0, 3, 6], 0],
            "sum": [[9, 12, 15], [3, 12, 21], 36],
        }
        self.assertAlmostEqual(
            actual,
            expected,
            "Expected different output when calling 'calculate()' with '[9,1,5,3,3,3,2,9,0]'",
        )

    def test_calculate_with_few_digits(self):
        self.assertRaisesRegex(
            ValueError,
            "List must contain nine numbers.",
            mean_var_std.calculate,
            [
                2,
                6,
                2,
                8,
                4,
                0,
                1,
            ],
        )


if __name__ == "__main__":
    unittest.main()
