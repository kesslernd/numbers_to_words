import re

def replace_numbers_with_words(input):
    return re.sub('\d+', process_match, input).capitalize()

def process_match(match):
    m = match.group(0)
    return number_to_word(int(m))

def number_to_word(number):
    less_than_twenty = {
        1: "one", 2: "two", 3: "three",
        4: "four", 5: "five", 6: "six",
        7: "seven", 8: "eight", 9: "nine",
        10: "ten", 11: "eleven", 12: "twelve",
        13: "thirteen", 14: "fourteen", 15: "fifteen",
        16: "sixteen", 17: "seventeen",18: "eighteen",
        19: "nineteen"
    }
    tens_increment = {
        2: "twenty", 3: "thirty", 4: "forty",
        5: "fifty", 6: "sixty", 7: "seventy",
        8: "eighty", 9: "ninety"
    }
    if number > 99:
        raise ValueError('number_to_word cannot parse numbers greater than 99')

    if number < 20:
        return less_than_twenty[number]
    else:
        first_digit = int(str(number)[0:1])
        second_digit = int(str(number)[1:])
        return '{}-{}'.format(tens_increment[first_digit], less_than_twenty[second_digit])

