### Introduction

It is a Test-driven development (TDD) process based test.<br> 
With this the developer can create a calculator function with the following conditions:<br>
* It allows only positive numbers (integers or float), even if the numbers is in string format (in this case the decimal point must be the '.').<br>
* In case of valid input it returns an integer (rounded down).<br>
* In case of invalid input it throws a Value error with a small comment.<br>
* In case of any valid string message variable given, it writes it to the stdout after a "The message is:" header line.<br>
* In case of the message contains only upper case letters, it is converted to lower case.<br>

### How to run it

You can run the tests with:<br> 
`python -m pytest tests -vv`<br>

If you do not have `pytest` then you can install it with:<br>
`pip install pytest` or `python -m pip install pytest`<br>

### Solution steps

All tests are skipped except the first one, you can remove the @unittest.skip(..) decorator one by one.<br>

First, run only the first test case (which already enabled), it will pass.

Then remove the skip decorator from the second test case and re-run it. It will fail.<br>
Now update the `sum_of_positives(..)` method to pass the test.<br>

Repeat it with the next test cases, until the `sum_of_positives(..)` method passes through them all.
