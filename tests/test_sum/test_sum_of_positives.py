import unittest
from unittest.mock import patch
import io

from sum.sum_of_positives import sum_of_positives


class TestSumOfPositives(unittest.TestCase):
    def test_valid_int_numbers(self):
        assert sum_of_positives(3, 2) == 5
        assert sum_of_positives(1, 1) == 2

    @unittest.skip("Step 2")
    def test_valid_float_numbers(self):
        assert sum_of_positives(3.1, 2) == 5
        assert sum_of_positives(3.6, 2.5) == 6

    @unittest.skip("Step 3")
    def test_valid_float_string_numbers(self):
        assert sum_of_positives("3.1", 2) == 5
        assert sum_of_positives("3.9", 2.2) == 6

    @unittest.skip("Step 4")
    def test_invalid_numbers(self):
        with self.assertRaises(ValueError) as ve:
            sum_of_positives(-3, 2)

        self.assertIn("positive", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            sum_of_positives(0, 2)

        self.assertIn("positive", str(ve.exception))

    @unittest.skip("Step 5")
    def test_invalid_not_number(self):
        with self.assertRaises(ValueError) as ve:
            sum_of_positives("a", 2)

        self.assertIn("number", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            sum_of_positives(1, "2a")

        self.assertIn("number", str(ve.exception))

    @unittest.skip("Step 6")
    def test_invalid_str_number(self):
        with self.assertRaises(ValueError) as ve:
            sum_of_positives("3,1", 2)

        self.assertIn("valid numbers", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            sum_of_positives(2, "3,1")

        self.assertIn("valid numbers", str(ve.exception))

    @unittest.skip("Step 7")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_message(self, mock_out):
        sum_of_positives(1, 2, "test")
        self.assertIn("The message is:", mock_out.getvalue())
        self.assertIn("test", mock_out.getvalue())

    @unittest.skip("Step 8")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_none_message(self, mock_out):
        sum_of_positives(1, 2)
        self.assertNotIn("The message is:", mock_out.getvalue())

        sum_of_positives(1, 2, "")
        self.assertNotIn("The message is:", mock_out.getvalue())

        sum_of_positives(1, 2, 3)
        self.assertNotIn("The message is:", mock_out.getvalue())

    @unittest.skip("Step 9")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_all_uppercase_message(self, mock_out):
        sum_of_positives(1, 2, "UPPERCASETEST")
        self.assertIn("The message is:", mock_out.getvalue())
        self.assertIn("uppercasetest", mock_out.getvalue())

    @unittest.skip("Step 10")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_some_uppercase_message(self, mock_out):
        sum_of_positives(1, 2, "UPPERCASEtest")
        self.assertIn("The message is:", mock_out.getvalue())
        self.assertIn("UPPERCASEtest", mock_out.getvalue())


if __name__ == "__main__":
    unittest.main()
