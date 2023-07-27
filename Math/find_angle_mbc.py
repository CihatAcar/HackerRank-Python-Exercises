"""
ABC is a right triangle, 90' at B.
Therefore, ABC = 90.
Point M is the midpoint of hypotenuse AC.
You are given the lengths AB and BC.
Your task is to find MBC (angle O', as shown in the figure) in degrees.

Input Format
The first line contains the length of side AB.
The second line contains the length of side BC.

Output Format
Output MBC in degrees.
Note: Round the angle to the nearest integer.
Examples:
If angle is 56.5000001°, then output 57°.
If angle is 56.5000000°, then output 57°.
If angle is 56.4999999°, then output 56°.

Sample Input
10
10

Sample Output
45°
"""
"""
Explanation of the code:
This task involves finding an angle in a right-angled triangle, where the required angle (MBC or Θ) is opposite to 
the given side BC and adjacent to the half of the hypotenuse. As you know, the tangent of an angle in a right triangle 
is the ratio of the side opposite the angle to the side adjacent to the angle. Therefore, we can find the required angle 
using the arctangent function (atan), which gives the angle in radians. We then convert this angle to degrees.
"""
import math

AB = int(input())
BC = int(input())

angle = math.degrees(math.atan(AB/BC))
print(str(round(angle)) + chr(176))
