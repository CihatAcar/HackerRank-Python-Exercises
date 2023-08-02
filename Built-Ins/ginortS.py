"""
You are given a string S.
S contains alphanumeric characters only.

Your task is to sort the string S in the following manner:
- All sorted lowercase letters are ahead of uppercase letters.
- All sorted uppercase letters are ahead of digits.
- All sorted odd digits are ahead of sorted even digits.

Input Format
A single line of input contains the string S.

Output Format
Output the sorted string S.

Sample Input
Sorting1234

Sample Output
ginortS1324
"""


def sorting_key(element):
    if element.islower():
        # Sort all lowercase letters first (ASCII value - ord('a'))
        return 1, element
    elif element.isupper():
        # Then sort all uppercase letters (ASCII value - ord('A'))
        return 2, element
    elif int(element) % 2 == 1:
        # Then sort all odd digits (ASCII value - ord('0'))
        return 3, element
    else:
        # Then sort all even digits (ASCII value - ord('0'))
        return 4, element


s = input().strip()
print(''.join(sorted(s, key=sorting_key)))
