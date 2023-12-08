'''
https://adventofcode.com/2023/day/1
'''
import string

digit_vals = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 
            'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

def load_input(file_name):
    with open(file_name, 'r') as file:
        data = file.read()
    return data
        

def part_1(str):
    '''
    For part 1 of day 1
    Accepts a calibration document (str)
    Returns sum
    '''
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


def part_2(str):
    '''
    For part 2 of day 1
    Accepts a calibration document (str)
    Returns sum
    '''
    sum = 0
    str = str.split('\n')[:-1]
    for line in str:
        digits = []
        temp_str = ''
        for char in line:
            if char not in string.ascii_letters and char != '\n':
                digits.append(int(char))
                continue
            temp_str += char
            for key in digit_vals.keys():
                if key in temp_str:
                    digits.append(int(digit_vals[key]))
                    temp_str = temp_str[-1]
                    break
        sum += digits[0] * 10 + digits[-1]
    return sum


if __name__ == '__main__':
    puzzle_input = load_input('01.txt')
    print(part_1(puzzle_input))
    print(part_2(puzzle_input))
