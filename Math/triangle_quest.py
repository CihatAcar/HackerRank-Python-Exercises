"""
You are given a positive integer N. Print a numerical triangle of height N - 1 like the one below:
1
22
333
4444
55555
......

Can you do it using only arithmetic operations, a single for loop and print statement?
Use no more than two lines. The first line (the for statement) is already written for you.
You have to complete the print statement.
Note: Using anything related to strings will give a score of 0.

Input Format
A single line containing integer, N.

Output Format
Print N - 1 lines as explained above.

Sample Input
5

Sample Output
1
22
333
4444
"""
"""
Explanation of solution code:
The code works by iterating through the range 1 to N (excluding N). 
For each iteration, it calculates i * (10**i - 1)//9. 
This equation results in a number consisting of i repeated i times.
For example, when i=1, 10**i - 1 equals 9, so 1 * 9 // 9 equals 1. 
When i=2, 10**i - 1 equals 99, so 2 * 99 // 9 equals 22. And so on.
This approach uses only a for loop, an arithmetic operation and a print statement, 
thus fulfilling the constraints of the task.
"""
# More than 2 lines will result in 0 score. Do not leave a blank line also
for i in range(1, int(input())):
    print(i * (10 ** i - 1) // 9)
