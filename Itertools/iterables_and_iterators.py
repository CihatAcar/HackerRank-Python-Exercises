"""
You are given a list of N lowercase English letters.
For a given integer K, you can select any K indices (assume 1-based indexing) with a uniform probability from the list.

Find the probability that at least one of the K indices selected will contain the letter: 'a'.

Input Format
The input consists of three lines. The first line contains the integer N, denoting the length of the list.
The next line consists of N space-separated lowercase English letters, denoting the elements of the list.
The third and the last line of input contains the integer K, denoting the number of indices to be selected.

Output Format
Output a single line consisting of the probability that at least one of the K indices selected contains the letter: 'a'.
Note: The answer must be correct up to 3 decimal places.

Sample Input
4
a a c d
2

Sample Output
0.8333
Explanation
All possible unordered tuples of length 2 comprising of indices from 1 to 4 are:
(1,2) (1,3) (1,4) (2,3) (2,4) (3,4)
Out of these 6 combinations, 5 of them contain either index 1 or index 2
which are the indices that contain the letter 'a'.
Hence, the answer is 5/6.
"""
from itertools import combinations


def calculate_probability(lst, k):
    # Calculate total combinations
    total_combinations = list(combinations(lst, k))

    # Calculate combinations that contain 'a'
    a_combinations = [comb for comb in total_combinations if 'a' in comb]

    # Calculate and print probability
    probability = len(a_combinations) / len(total_combinations)
    print('{:.4f}'.format(probability))


n = int(input()) # this parameter actually not needed.
lst = input().split()
k = int(input())

calculate_probability(lst, k)
