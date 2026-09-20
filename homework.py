def flip_num(num):
    if num // 10 == 0:
        return num
    last = num % 10
    rest = flip_num(num // 10) 
    return last * pow(10, len(str(rest))) + rest 

def flip_name(s):
    if len(s) == 1:
        return s
    return flip_name(s[1:]) + s[0]

def is_power4(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    if n % 4 == 0:
        return is_power4(n // 4)
    return False
