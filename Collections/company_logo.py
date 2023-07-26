"""
A newly opened multinational brand has decided to base their company logo on the three most common characters
in the company name. They are now trying out various combinations of company names and logos based on this condition.
Given a string s, which is the company name in lowercase letters,
your task is to find the top three most common characters in the string.
Print the three most common characters along with their occurrence count.
Sort in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.

For example, according to the conditions described above,
GOOGLE would have it's logo with the letters G, O, E.

Input Format
A single line of input containing the string S.

Output Format
Print the three most common characters along with their occurrence count each on a separate line.
Sort output in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.

Sample Input:
aabbbccde

Sample Output:
b 3
a 2
c 2

Explanation:
aabbbccde
Here, b occurs 3 times. It is printed first.
Both a and c occur 2 times. So, a is printed in the second line and c in the third line
because a comes before c in the alphabet.
Note: The string S has at least 3 distinct characters.
"""
from collections import Counter


def print_most_common_chars(s):
    counter = Counter(s)
    # Sort by count (descending) and then alphabetically
    sorted_counter = sorted(counter.items(), key=lambda x: (-x[1], x[0]))

    for char, count in sorted_counter[:3]:
        print(char, count)


s = input().strip()
print_most_common_chars(s)
