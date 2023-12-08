'''
https://adventofcode.com/2023/day/1
'''
import string

def load_input(file_name):
    with open(file_name, 'r') as file:
        data = file.read()
    return data
        

def parse_calibration_doc(str):
    sum = 0
    str = str.split('\n')[:-1]
    for line in str:
        digits = []
        for char in line:
            if char in string.ascii_letters:
                continue
            elif len(digits) == 1:
                digits.append(int(char))
                continue
            digits.append(int(char))
        sum += digits[0] * 10 + digits[-1]
    return sum


puzzel_input = load_input('01.txt')
print(parse_calibration_doc(puzzel_input))
