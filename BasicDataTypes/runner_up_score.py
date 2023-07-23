"""
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
You are given n scores. Store them in a list and find the score of the runner-up.

Input Format
The first line contains n. The second line contains an array A[] of n integers each separated by a space.
Print the runner up score.

Sample Input:
5
2 3 6 6 5

Sample Output:
5
"""


n = int(input())
arr = map(int, input().split())

# Sort the set of array in descending order
arr_set = sorted(set(arr), reverse=True)

if len(arr_set) > 1:
    # Runner-up is a competitor or team taking second place in a contest.
    # So we need to second best score.
    runner_up_score = arr_set[1]
    print(runner_up_score)
