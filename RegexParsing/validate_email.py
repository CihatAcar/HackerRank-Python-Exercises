"""
A valid email address meets the following criteria:
It's composed of a username, domain name, and extension assembled in this format: username@domain.extension
The username starts with an English alphabetical character, and any subsequent characters consist of one or
more of the following: alphanumeric characters, -,., and _.
The domain and extension contain only English alphabetical characters.
The extension is 1, 2  or 3  characters in length.
Given n  pairs of names and email addresses as input, print each name and email address pair
having a valid email address on a new line.
Hint: Try using Email.utils() to complete this challenge.

Input Format
The first line contains a single integer, n, denoting the number of email addresses.
Each line i of the n  subsequent lines contains a name and an email address
as two space-separated values following this format:
name <user@email.com>

Constraints
0 < n < 100

Output Format
Print the space-separated name and email address pairs containing valid email addresses only.
Each pair must be printed on a new line in the following format:
name <user@email.com>
You must print each valid email address in the same order as it was received as input.

Sample Input:
2
DEXTER <dexter@hotmail.com>
VIRUS <virus!@variable.:p>

Sample Output
DEXTER <dexter@hotmail.com>
"""



import email.utils
import re


def is_valid_email(user_email):
    """"
    email.utils.parseaddr: which should be the value of some address-containing field such as
    To or Cc – into its constituent username and email address parts.
    Returns a tuple of that information, unless the parse fails, in which case a 2-tuple of ('', '') is returned.

    `^`: Asserts the start of the string.
    `[a-zA-Z]`: Matches any single English alphabetical character (uppercase or lowercase).
    `[\w.-]*`: Matches zero or more occurrences of word characters (alphanumeric characters and underscore), dot (.),
    or hyphen (-). This allows the username part of the email address to contain
    additional characters after the first alphabetical character.
    `@`: Matches the "@" symbol, which separates the username and domain parts of the email address.
    `[a-zA-Z]+`: Matches one or more occurrences of English alphabetical characters.
    This is the domain name part of the email address, which should consist of at least one alphabetical character.
    `\.`: Escapes the dot (.) character to match it literally. It is used to separate the domain name from the extension.
    `[a-zA-Z]{1,3}`: This is the extension part of the email address, which should be 1, 2, or 3 characters in length.
    `$`: Asserts the end of the string.

    Putting it all together, the regular expression pattern ensures that the email address adheres to the following rules:

    - The email address must start with an alphabetical character.
    - The username part can contain any alphanumeric characters, underscore (_), dot (.), or hyphen (-).
    - The domain part must contain at least one alphabetical character.
    - The extension part must be between 1 to 3 alphabetical characters in length.
    - The pattern matches the entire email address string from start to end.
    """
    _, address = email.utils.parseaddr(user_email)
    pattern = r'^[a-zA-Z][\w.-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$'
    if not re.match(pattern, address):
        return False
    return True


def main():
    n = int(input("Enter the number of pairs: "))

    for _ in range(n):
        name, email_address = input().split()
        if is_valid_email(email_address):
            print(f"{name} {email_address}")


if __name__ == "__main__":
    main()
