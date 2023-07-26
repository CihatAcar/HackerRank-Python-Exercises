"""
You are given n words. Some words may repeat. For each word, output its number of occurrences.
The output order should correspond with the input order of appearance of the word.
See the sample input/output for clarification.
Note: Each input line ends with a "\n" character.

The sum of the lengths of all the words do not exceed
All the words are composed of lowercase English letters only.
Input Format
The first line contains the integer, n.
The next n lines each contain a word.

Output Format
Output 2 lines.
On the first line, output the number of distinct words from the input.
On the second line, output the number of occurrences for each distinct word according to their appearance in the input.

Sample Input
4
bcdef
abcdefg
bcde
bcdef

Sample Output
3
2 1 1
Explanation
There are 3 distinct words. Here, "bcdef" appears twice in the input at the first and last positions.
The other words appear once each.
The order of the first appearances are "bcdef", "abcdefg" and "bcde" which corresponds to the output.
"""
from collections import Counter, OrderedDict


def count_word_occurrences(words):
    word_counts = Counter(words)
    word_dict = OrderedDict()

    for word in words:
        if word not in word_dict:
            word_dict[word] = word_counts[word]

    print(len(word_dict))
    print(*word_dict.values())


# Get the number of words (n) from the user
n = int(input())

# Get the words as input and store them in a list
words = [input().strip() for _ in range(n)]

# Calculate and print the count of word occurrences
count_word_occurrences(words)
