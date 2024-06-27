import unittest
from unittest.mock import patch
import io

from sum.sum_of_positives import sum_of_positives


class TestSumOfPositives(unittest.TestCase):
    def test_valid_int_numbers(self):
        """
        Basic function test of the addition of integers
        """
        assert sum_of_positives(3, 2) == 5
        assert sum_of_positives(1, 1) == 2

    @unittest.skip("Step 2")
    def test_valid_float_numbers(self):
        """
        Test of the addition of numbers (integer and/or float),
        the result is rounded down (after the addition)
        """
        assert sum_of_positives(3.1, 2) == 5
        assert sum_of_positives(3.6, 2.5) == 6

    @unittest.skip("Step 3")
    def test_valid_float_string_numbers(self):
        """
        Test of the addition of any input that can be converted to number,
        the result is rounded down (after the addition)
        """
        assert sum_of_positives("3.1", 2) == 5
        assert sum_of_positives("3.8", 2.3) == 6
        assert sum_of_positives("3", 2) == 5
        assert sum_of_positives(3.9, "2.8") == 6

    @unittest.skip("Step 4")
    def test_invalid_numbers(self):
        """
        Test of invalid numbers, these are: 0 or negative
        The app gives back the desired type of exception with at least a desired part of message
        """
        with self.assertRaises(ValueError) as ve:
            sum_of_positives(-3, 2)
        self.assertIn("positive", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            sum_of_positives(3, -2)
        self.assertIn("positive", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            sum_of_positives(0, 2)
        self.assertIn("not zero", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            sum_of_positives(2, 0)
        self.assertIn("not zero", str(ve.exception))

    @unittest.skip("Step 5")
    def test_invalid_not_number(self):
        """
        Test the exception raising in case of any input is not valid
        The app gives back the desired type of exception with at least a desired part of message
        """
        with self.assertRaises(ValueError) as ve:
            sum_of_positives("3,1", 2)
        self.assertIn("valid number", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            sum_of_positives(2, "3,1")
        self.assertIn("valid number", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            sum_of_positives("a", 2)
        self.assertIn("valid number", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            sum_of_positives(1, "2a")
        self.assertIn("valid number", str(ve.exception))

        with self.assertRaises(TypeError) as ve:
            sum_of_positives(1, [2, 1])
        self.assertIn("number or string", str(ve.exception))

        with self.assertRaises(TypeError) as ve:
            sum_of_positives(1, ["2", 1])
        self.assertIn("number or string", str(ve.exception))

    @unittest.skip("Step 6")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_message(self, mock_out):
        """
        Test the message output part if the message is valid
        """
        sum_of_positives(1, 2, "test")
        self.assertIn("The message is:\n", mock_out.getvalue())
        self.assertIn("test", mock_out.getvalue())

    @unittest.skip("Step 7")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_no_message(self, mock_out):
        """
        Test the message output part if the message is not valid (null, empty, not string)
        """
        sum_of_positives(1, 2)
        self.assertNotIn("The message is:", mock_out.getvalue())

        sum_of_positives(1, 2, "")
        self.assertNotIn("The message is:", mock_out.getvalue())

        sum_of_positives(1, 2, 3)
        self.assertNotIn("The message is:", mock_out.getvalue())

        sum_of_positives(1, 2, [3])
        self.assertNotIn("The message is:", mock_out.getvalue())

        sum_of_positives(1, 2, ["3"])
        self.assertNotIn("The message is:", mock_out.getvalue())

    @unittest.skip("Step 8")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_all_uppercase_message(self, mock_out):
        """
        Test the message output part if the message contains only upper case letters
        """
        sum_of_positives(1, 2, "UPPERCASE LETTERS ONLY")
        self.assertIn("The message is:\n", mock_out.getvalue())
        self.assertIn("uppercase letters only\n", mock_out.getvalue())

    @unittest.skip("Step 9")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_not_all_uppercase_message(self, mock_out):
        """
        Test the message output part if the message contains not only upper case letters
        """
        sum_of_positives(1, 2, "UPPERCASE Letters")
        self.assertIn("The message is:\n", mock_out.getvalue())
        self.assertIn("UPPERCASE Letters\n", mock_out.getvalue())

        sum_of_positives(1, 2, "no uppercase letter")
        self.assertIn("The message is:\n", mock_out.getvalue())
        self.assertIn("no uppercase letter\n", mock_out.getvalue())


if __name__ == "__main__":
    unittest.main()
