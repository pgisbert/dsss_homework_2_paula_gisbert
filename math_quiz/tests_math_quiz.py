import unittest
from math_quiz import random_number_generation, random_operator_selection, generate_calculation


class TestMathGame(unittest.TestCase):

    def test_random_number_generation(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_number_generation(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_operator_selection(self):
        # Test if the random operator selected is one of the expected operators
        expected_operators = ['+', '-', '*', '/']
        for _ in range(100):  # Test a number of random selections
            operator = random_operator_selection()
            self.assertIn(operator, expected_operators)

    def test_generate_calculation(self):
            test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (5, 2, '-', '5 - 2', 3),
            (5, 2, '*', '5 * 2', 10),
            (6, 3, '/', '6 / 3', 2),
        ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = generate_calculation(num1, num2, operator)
                self.assertEqual(problem, expected_problem)
                self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
