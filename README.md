It is a Test-driven development (TDD) process based test. 
With this the developer can create a calculator function with the following conditions:
It allows only positive numbers (integers or float), even if the numbers is in string format (in this case the decimal point must be the '.').
In case of valid input it returns with an integer (rounded down).
In case of invalid input it throws a Value error with a small comment.
In case of any valid string message variable given, it writes it to the stdout after a "The message is:" header line.
In case of the message contains only upper case letters, it is converted to lower case

You can run the tests with: 
`python -m pytest tests -vv`
All tests are skipped except the first one, you can remove the @unittest.skip(..) decorator one by one.

If you do not have `pytest` then you can install it with:
`pip install pytest`
