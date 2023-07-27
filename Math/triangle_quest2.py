"""
You are given a positive integer N.
Your task is to print a palindromic triangle of size N.

For example, a palindromic triangle of size 5 is:
1
121
12321
1234321
123454321

You can't take more than two lines. The first line (a for-statement) is already written for you.
You have to complete the code using exactly one print statement.

Note:
Using anything related to strings will give a score of 0.
Using more than one for-statement will give a score of 0.

Input Format
A single line of input containing the integer N.

Output Format
Print the palindromic triangle of size N as explained above.

Sample Input
5

Sample Output
1
121
12321
1234321
123454321
"""
"""
Explanation of solution code for this problem:
In this code, 10**i - 1 generates a number that has i digits of 9. 
For example, when i=1, 10**i - 1 equals 9, when i=2, 10**i - 1 equals 99, 
when i=3, 10**i - 1 equals 999, and so on. 
Then (10**i - 1)//9 generates a number that has i digits of 1, 
because 9, 99, 999, etc. divided by 9 equals 1, 11, 111, ... 
Finally, ((10**i - 1)//9)**2 generates the palindromic triangle, 
because the square of 1, 11, 111, ... equals 1, 121, 12321, ...
"""
# More than 2 lines will result in 0 score. Do not leave a blank line also
for i in range(1, int(input()) + 1):
    print(((10 ** i - 1) // 9) ** 2)
