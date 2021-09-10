import re

def swap_case(s):
    new_s = ''
    for i in s:
        if(re.search('[a-z]', i)):
            new_s = new_s + i.upper()
        elif(re.search('[A-Z]', i)):
            new_s = new_s + i.lower()
        else:
            new_s = new_s + i
    return new_s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)