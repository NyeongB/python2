import functools

def comparator(a, b):
    
    num1 = int(str(a)+str(b))
    num2 = int(str(b)+str(a))
    
    if num1 < num2:
        return 1
    else :
        return -1

def solution(numbers):
    
    numbers.sort(key=functools.cmp_to_key(comparator))
    
    answer = ''.join(map(str,numbers))
    
    return str(int(answer))