"""
ABCXYZ company has up to 100 employees.
The company decides to create a unique identification number (UID) for each of its employees.
The company has assigned you the task of validating all the randomly generated UIDs.
A valid UID must follow the rules below:

It must contain at least 2 uppercase English alphabet characters.
It must contain at least 3 digits (0 - 9).
It should only contain alphanumeric characters (a, z - A & - Z).
No character should repeat.
There must be exactly 10 characters in a valid UID.
Input Format
The first line contains an integer T, the number of test cases.
The next T lines contains an employee's UID.
Output Format
For each test case, print 'Valid' if the UID is valid.
Otherwise, print 'Invalid', on separate lines. Do not print the quotation marks.

Sample Input
2
B1CD102354
B1CDEF2354

Sample Output
Invalid
Valid
Explanation
B1CD102354: 1 is repeating → Invalid
B1CDEF2354: Valid
"""
import re


def validate(uid):
    if (len(uid) == 10 and
            len(set(uid)) == len(uid) and
            re.search(r'[A-Z].*[A-Z]', uid) and
            len(re.findall(r'\d', uid)) >= 3 and
            uid.isalnum()):
        return 'Valid'
    else:
        return 'Invalid'


t = int(input())
for _ in range(t):
    uid = input()
    print(validate(uid))
