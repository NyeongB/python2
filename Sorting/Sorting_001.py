'''
출제 : 프로그래머스
난이도 : 레벨 1
문제 : K번째수
날짜 : 22.05.09
유형 : 정렬
'''



def solution(arr, commands):

    answer = []

    for command in commands:
        i, j, k = command[0], command[1], command[2]
        #print(i,j,k)
        temp = arr[i-1:j]
        temp.sort()
        answer.append(temp[k-1])

    return answer

arr = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]


print(solution(arr, commands))