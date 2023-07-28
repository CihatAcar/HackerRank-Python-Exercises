"""
Mr. Anant Asankhya is the manager at the INFINITE hotel. The hotel has an infinite amount of rooms.
One fine day, a finite number of tourists come to stay at the hotel.
The tourists consist of:
→ A Captain.
→ An unknown group of families consisting of K members per group where K ≠ 1.
The Captain was given a separate room, and the rest were given one room per group.
Mr. Anant has an unordered list of randomly arranged room entries.
The list consists of the room numbers for all of the tourists.
The room numbers will appear K times per group except for the Captain's room.
Mr. Anant needs you to help him find the Captain's room number.
The total number of tourists or the total number of groups of families is not known to you.
You only know the value of K and the room number list.

Input Format
The first line consists of an integer, K, the size of each group.
The second line contains the unordered elements of the room number list.

Output Format
Output the Captain's room number.

Sample Input
5
1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2

Sample Output
8

Explanation
The list of room numbers contains 31 elements. Since K is 5, there must be 6 groups of families.
In the given list, all of the numbers repeat 5 times except for room number 8.
Hence, 8 is the Captain's room number.
"""
"""
Explanation of the solution code:
In this script, set(rooms) gives us a set of unique room numbers, 
and sum(set(rooms))*K gives us the total if each room number was repeated K times. 
sum(rooms) gives us the actual total of the room numbers. 
The difference between these two sums is captain_room*(K-1), 
because the captain's room number is repeated one less time than the other room numbers. 
Therefore, dividing by K-1 gives us the captain's room number.
"""
K = int(input())
rooms = list(map(int, input().split()))

captain_room = (sum(set(rooms))*K - sum(rooms)) // (K-1)
print(captain_room)

# We could solve this problem also with using collections Counter method
from collections import Counter

K = int(input())
rooms = list(map(int, input().split()))

counts = Counter(rooms)
captain_room = next(room for room, count in counts.items() if count == 1)

print(captain_room)
