def solution(array, commands):
    answer = []
    
    for com in commands:
        temp = list(array[com[0]-1:com[1]])
        answer.append(sorted(temp)[com[2]-1])
    
    return answer