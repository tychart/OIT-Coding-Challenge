import re

# This is the lookup table for the conversions from 
# Roman numerals to integers 
r2i_lookup_table: dict = {
    "": 0,
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

# This is the lookup table for the conversions from 
# integers to Roman numerals 
i2r_lookup_table: dict = {
    0: '',
    1: 'I',
    4: 'IV',
    5: 'V',
    9: 'IX',
    10: 'X',
    40: 'XL',
    50: 'L',
    90: 'XC',
    100: 'C',
    400: 'CD',
    500: 'D',
    900: 'CM',
    1000: 'M'
}

# List of allowed characters
roman_numerals = ["I", "V", "X", "L", "C", "D", "M"]

# Create a regex pattern to match any character not in the list
pattern = '[^' + ''.join(roman_numerals) + ']+'

def lookup_char(in_char: str) -> int:
    return r2i_lookup_table[in_char]

# Finds the largest numeral that can be used, then returns it along
# with the integer represintation 
def highest_numeral(in_int: int) -> list:
    highest_numeral = ""
    highest_int = 0
    for val in i2r_lookup_table.keys():
        if val > in_int:
            return [highest_int, i2r_lookup_table[highest_int]]
        highest_int = val
    return [highest_int, i2r_lookup_table[highest_int]]

def roman_to_number(in_str: str) -> str:
    last_char: str = ""
    this_char: str = ""
    running_total: int = 0

    for character in in_str:
        last_char = this_char
        this_char = character
        if lookup_char(this_char) <= lookup_char(last_char):
            running_total += lookup_char(this_char)
        else:
            running_total += lookup_char(this_char) - (2 * lookup_char(last_char))
    return str(running_total)

# Algorithm thoughts/notes (While I was thinking)
# CXL
# 100 + 10 + (50 - (2)10)
# 100 + 40

def int_to_roman(in_str: str) -> str:
    curr_int: int = int(in_str)
    out_str: str = ""
    while curr_int > 0:
        sub_int, temp_str = highest_numeral(curr_int)
        curr_int -= sub_int
        out_str += temp_str
    return out_str


def parse_string(in_str: str) -> str:

    if in_str[0] in roman_numerals:
        # Check to make sure the user entered in only roman numerals
        match = re.search(pattern, in_str)
        if match:
            return f"Invalid input: First character is a Roman numaral, but non-Roman numeral characters found in input string '{in_str}'"
        else:
            return roman_to_number(in_str)
    
    if in_str[0].isnumeric():
        if in_str.isnumeric():
            return int_to_roman(in_str)
        else:
            return f"Invalid input: First character is an integer, but non-number characters found in input string '{in_str}'"
    else:
        return f"Invalid input: First character is neither an integer nor a roman numeral. Please check string and try again '{in_str}'"
    
def main():
    while True:
        in_str = input("Please enter the number (Roman or Integer) to convert (Enter 'quit' to quit)\n")
        if in_str == "quit":
            return
        print(f"Result: {parse_string(in_str)}")


main()