import re 

s = 'HelloAlmas'

pattern = r'(?<=[a-z])(?=[A-Z])'
#positive lookbehind assertion

result = re.split(pattern, s)

print(result)