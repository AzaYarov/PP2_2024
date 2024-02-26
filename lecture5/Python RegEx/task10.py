import re

def upper_split(s):
    pattern = r'[A-Z][a-z]*'
    words = re.findall(pattern, s)
    snake_case = ''
    for i in range(len(words)):
        if i < len(words) - 1:
            snake_case += words[i].lower() + '_'
        elif i == len(words) - 1: 
            snake_case += words[i].lower()
    return snake_case

s = input()
result = upper_split(s)
print(result)