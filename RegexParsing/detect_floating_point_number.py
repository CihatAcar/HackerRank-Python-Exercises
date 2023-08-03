"""
You are given a string N.
Your task is to verify that N is a floating point number.
In this task, a valid float number must satisfy all of the following requirements:
> Number can start with +, - or . symbol.
For example:

✔ +4.50
✔ -1.0
✔ .5
✔ -.7
✔ +.4
✖ -+4.5

> Number must contain at least 1 decimal value.
For example:

✖ 12.
✔ 12.0

> Number must have exactly one . symbol.
> Number must not give any exceptions when converted using float(N).

Input Format
The first line contains an integer T, the number of test cases.
The next T line(s) contains a string N.

Output Format
Output True or False for each test case.

Sample Input:
4
4.0O0
-1.00
+4.54
SomeRandomStuff

Sample Output:
False
True
True
False

Explanation 0
4.0O0: O is not a digit.
-1.00: is valid.
+4.54: is valid.
SomeRandomStuff: is not a number.
"""
import re


def check_float(num):
    if re.match(r'^[+-]?[0-9]*\.[0-9]+$', num):
        return True
    return False


T = int(input().strip())
for _ in range(T):
    print(check_float(input().strip()))
