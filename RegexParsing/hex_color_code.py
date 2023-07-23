"""
CSS colors are defined using a hexadecimal (HEX) notation for the combination of Red, Green, and Blue color values (RGB).
Specifications of HEX Color Code
■ It must start with a '#' symbol.
■ It can have 3 or 6 digits.
■ Each digit is in the range of 0 to F.(1,2,3,4,5,6,7,8,9,0,A,B,C,D,E and F).
■ A - F letters can be lower case. (a,b,c,d,e and f are also valid digits).

Valid Hex Color Codes
#FFF
#025
#F0A1FB

Invalid Hex Color Codes
#fffabg
#abcf
#12365erff
"""

import re


def extract_hex_color_codes(css_code):
    """
    - `#`: Matches the '#' symbol, which indicates the start of a Hex Color Code.
    - `(?:)`: A non-capturing group that allows us to apply quantifiers to a group of characters.
    It's used here to specify that the entire group should be repeated 1 or 2 times.
    - `[0-9a-fA-F]{3}`: Matches exactly 3 hexadecimal digits (0-9 and a-f, both uppercase and lowercase).
    This allows for short Hex Color Codes like '#ABC'.
    - `[0-9a-fA-F]{1,2}`: Matches 1 or 2 hexadecimal digits. This allows for full Hex Color Codes like '#FFCC33'.
    - `\b`: Asserts a word boundary, ensuring that the Hex Color Code is not part of a longer word.

    The regular expression pattern ensures that the Hex Color Code must start with a '#' symbol
    and can have either 3 or 6 hexadecimal digits (with or without the '#' symbol).
    It matches valid Hex Color Codes within the CSS property values.
    """
    pattern = r'#(?:[0-9a-fA-F]{3}){1,2}\b'
    #  re.findall: return a list of all non-overlapping matches as strings.
    return re.findall(pattern, css_code)


def main():
    n = int(input())
    # "\n".join(): concatenates css code into a single multi-line string
    css_code_lines = "\n".join(input() for _ in range(n))

    valid_hex_color_codes = []
    # re.findall(r'{(.*?)}': find all occurrences of text within curly braces (parantheses) in the entire CSS code.
    # re.DOTALL Ensure "." in the pattern also matches newline characters,
    # so it can capture the content within curly braces, even if it spans multiple lines.
    property_values = re.findall(r'{(.*?)}', css_code_lines, re.DOTALL)
    for prop_val in property_values:
        hex_color_codes = extract_hex_color_codes(prop_val)
        valid_hex_color_codes.extend(hex_color_codes)

    for color_code in valid_hex_color_codes:
        print(color_code)


if __name__ == "__main__":
    main()
