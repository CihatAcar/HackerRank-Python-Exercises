"""
start() & end()
These expressions return the indices of the start and end of the substring matched by the group.
Code
import re
m = re.search(r'\d+','1234')
m.end()
4
m.start()
0

Task
You are given a string S.
Your task is to find the indices of the start and end of string k in S.

Input Format
The first line contains the string S.
The second line contains the string k.

Output Format
Print the tuple in this format: (start _index, end _index).
If no match is found, print (-1, -1).

Sample Input
aaadaa
aa

Sample Output
(0, 1)
(1, 2)
(4, 5)
"""
import re


def find_substring(s, k):
    pattern = re.compile('(?=({}))'.format(k))  # adding positive lookahead
    matches = pattern.finditer(s)
    found = False
    for match in matches:
        found = True
        print((match.start(), match.start() + len(k) - 1))  # using length of 'k' to find end position
    if not found:
        print((-1, -1))


s = input().strip()
k = input().strip()
find_substring(s, k)
