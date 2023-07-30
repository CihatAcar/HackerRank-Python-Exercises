"""
You are given a set A and n other sets.
Your job is to find whether set A is a strict superset of each of the N sets.
Print True, if A is a strict superset of each of the N sets. Otherwise, print False.
A strict superset has at least one element that does not exist in its subset.

Example
Set ([1,3,4]) is a strict superset of set ([1,3]).
Set ([1,3,4]) is not a strict superset of set ([1,3,4]).
Set ([1,3,4]) is not a strict superset of set ([1,3,5]).

Input Format
The first line contains the space separated elements of set A.
The second line contains integer n, the number of other sets.
The next n lines contains the space separated elements of the other sets.

Output Format
Print True if set A is a strict superset of all other N sets. Otherwise, print False.

Sample Input:
1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
2
1 2 3 4 5
100 11 12

Sample Output:
False

Explanation:
Set A is the strict superset of the set ([1,2,3,4,5]) but not of the set ([100,11,12]) because 100 is not in set A.
Hence, the output is False.
"""
"""
Explanation of the solution code:
In Python, the > operator is used to check if a set is a strict superset of another set. 
If all elements of the second set are in the first set, 
and the first set has at least one element that the second set doesn't have, 
A > B returns True. Otherwise, it returns False.
"""
A = set(map(int, input().split()))
num_other_sets = int(input())

is_strict_superset = True
for _ in range(num_other_sets):
    other_set = set(map(int, input().split()))
    if not (A > other_set):
        is_strict_superset = False
        break

print(is_strict_superset)
