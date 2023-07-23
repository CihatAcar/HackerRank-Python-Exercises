"""
You have given 4 integers with following:
x = int(input())
y = int(input())
z = int(input())
n = int(input())

Use list comprehension!

Sample Input:
1
1
1
2

Sample Output:
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

Print the list in lexicographic increasing order.
Print a list of all possible coordinates given by x, y, z on a 3D grid where the sum of i + j + k  is not equal to n.
"""

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    coordinates = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
    print(coordinates)