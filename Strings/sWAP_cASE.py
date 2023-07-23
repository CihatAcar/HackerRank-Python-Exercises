"""
You are given a string and your task is to swap cases. In other words,
convert all lowercase letters to uppercase letters and vice versa.

For Example:
Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2

Function Description
Complete the swap_case function in the editor below.
swap_case has the following parameters:
string s: the string to modify

Returns
string: the modified string

Sample Input:
HackerRank.com presents "Pythonist 2"

Sample Output:
hACKERrANK.COM PRESENTS "pYTHONIST 2"
"""


def swap_case(s):
    modified_s = ""
    for string in s:
        if not string.isalpha():
            modified_s += string
        elif string.isupper():
            modified_s += string.lower()
        elif string.islower():
            modified_s += string.upper()
    return modified_s


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
