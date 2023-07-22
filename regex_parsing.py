"""
Let's dive into the interesting topic of regular expressions! You are given some input, and you are required to check whether they are valid mobile numbers.
A valid mobile number is a ten digit number starting with a 7, 8  or9 .

Concept:
A valid mobile number is a ten digit number starting with a 7, 8  or 9 .

Input Format:
The first line contains an integer N, the number of inputs.
N lines follow, each containing some string.

Constraints:
1 <= N <= 10
2 <= len(mobile_number) <= 15

Output Format
For every string listed, print "YES" if it is a valid mobile number and "NO" if it is not on separate lines. Do not print the quotes.

Sample Input:
2
9587456281
1252478965

Sample Output:
YES
NO
"""

import re

"This function is for checking the pattern of given input."


def is_valid_mobile_number(number):
    """
    r: The r before the pattern is called a "raw string" literal in Python. It indicates that the string should be 
    treated as-is, without any special character escaping. Raw strings are often used with regular expressions to 
    avoid any unintended behavior due to backslashes. It ensures that backslashes are not interpreted as escape 
    characters within the regular expression pattern. 
    ^: The caret symbol ^ is a special metacharacter in regular expressions. It asserts that the pattern should start 
    matching at the beginning of the string. 
    [789]: This is a character class. It matches any single character that is either 7, 8, or 9. 
    So, it will match a string that starts with any of these three digits. 
    \d{9}: The \d is a shorthand character class that matches any digit (equivalent to [0-9]). 
    The {9} following \d means that it should match exactly 9 digits. 
    So, this part of the pattern matches nine consecutive digits after the first character that matched the [789] part. 
    $: The dollar sign $ is another special metacharacter in regular expressions. 
    It asserts that the pattern should end matching at the end of the string.
    """
    pattern = r'^[789]\d{9}$'
    return bool(re.match(pattern, number))


def main():
    try:
        N = int(input().strip())

        for _ in range(N):
            mobile_number = input().strip()
            if is_valid_mobile_number(mobile_number):
                print("YES")
            else:
                print("NO")
    except ValueError:
        print("Invalid input. Please enter a valid number of inputs.")


if __name__ == "__main__":
    main()
