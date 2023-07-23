"""Given the names and grades for each student in a class of N  students, store them in a nested list and print the
name(s) of any student(s) having the second lowest grade. Note: If there are multiple students with the second lowest
grade, order their names alphabetically and print each name on a new line.


Sample Input:
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

Sample Output:
Berry
Harry
"""

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    second_lowest_grade = sorted(set(score for name, score in students))[1]

    for name, score in sorted(students):
        if score == second_lowest_grade:
            print(name)
