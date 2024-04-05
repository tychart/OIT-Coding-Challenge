import re

# This is the lookup table for the conversions from 
# Roman Numerals to integers 
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

i2r_lookup_table: dict = {
    1000: 'M', 
    900: 'CM', 
    500: 'D', 
    400: 'CD',
    100: 'C', 
    90: 'XC', 
    50: 'L', 
    40: 'XL',
    10: 'X', 
    9: 'IX', 
    5: 'V', 
    4: 'IV',
    1: 'I',
    0: ''
}

# List of allowed characters
roman_numerals = ["I", "V", "X", "L", "C", "D", "M"]

# Create a regex pattern to match any character not in the list
pattern = '[^' + ''.join(roman_numerals) + ']+'

def lookup_char(in_char: str) -> int:
    return r2i_lookup_table[in_char]

def highest_numeral(in_int: int) -> list:
    highest_numeral = ""
    highest_int = 0
    for val in i2r_lookup_table.keys():
        if val > in_int:
            return [highest_int, i2r_lookup_table[highest_int]]
        highest_int = val
    return None


def roman_to_number(in_str: str) -> str:
    print("Running roman_to_number")
    
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

# Algorithm thoughts/notes
# CXL
# 100 + 10 + (50 - (2)10)
# 100 + 40

def int_to_roman(in_str: str) -> str:
    curr_int: int = int(in_str)
    out_str: str = ""
    while curr_int > 0:
        sub_int, temp_str = highest_numeral(curr_int)
        print(f"Subbing {sub_int}")
        curr_int -= sub_int
        out_str += temp_str
    return out_str


def parse_string(in_str: str) -> str:
    

    if in_str[0] in roman_numerals:
        # Check to make sure the user entered in only roman numerals
        match = re.search(pattern, in_str)
        if match:
            return f"Invalid input: First character is a Roman numaral, but non-Roman numeral characters found in input string '{in_str}'"
            # print(f"Error String '{in_str}' contains a character not in the list.")
        else:
            return roman_to_number(in_str)
            
    
    if in_str[0].isnumeric():
        if in_str.isnumeric():
            return int_to_roman(in_str)
        else:
            return f"Invalid input: First character is an integer, but non-number characters found in input string '{in_str}'"
    else:
        return f"Invalid input: First character is neither an integer nor a roman numeral. Please check string and try again '{in_str}'"
    

#test?


def main():
    while True:
        in_str = input("Please enter the number (Roman or Integer) to convert (Enter 'quit' to quit)\n")
        if in_str == "quit":
            return
        print(f"Result: {parse_string(in_str)}")

# print(f"This is the thing: {in_str}")

main()