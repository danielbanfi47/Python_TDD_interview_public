### Introduction

It is a Test-driven development (TDD) process based test.<br> 
With this the developer can create a calculator function with the following conditions:<br>
* It is a calculator function (with some extra sub function).<br>
* It allows only positive numbers (which represents integers or float), even if the numbers is in string format (in this case the decimal point must be the '.').<br>
* In case of valid input, it returns an integer (rounded down after the addition).<br>
* In case of invalid input, it throws a specific error (Value or Type) with a small comment.<br>
* In case of any valid string message variable given, it writes that to the stdout after a separate "The message is:" header line.<br>
* In case of the message contains only upper case letters, it converts that to lower case.<br>

### How to run it

You can run the tests with:<br> 
`python -m pytest tests -vv`<br>

If you do not have `pytest` then you can install it with:<br>
`pip install pytest` or `python -m pip install pytest`<br>

### Solution steps

In the beginning all tests are skipped except the first one, you can remove the @unittest.skip(..) decorator one by one.<br>

So first, run only the first test case (which already enabled), which will pass.

Then remove the skip decorator from the second test case and re-run it. That will fail.<br>
Now update the `sum_of_positives(..)` method to pass the test.<br>

Repeat it with the next test cases, until the `sum_of_positives(..)` method passes through them all.
