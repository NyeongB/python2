'''
출제 : 프로그래머스
난이도 : 레벨 2
문제 : 방문길이
날짜 : 22.05.21
유형 : 구현
'''

def solution(dirs):
    answer = 0
    visited = set()
    d = {'U':(-1,0), 'L':(0,-1), 'D':(1,0), 'R':(0,1) }
    x, y = 0, 0
    for dir in dirs:
        nx, ny = x + d[dir][0], y + d[dir][1]
        
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            visited.add((x,y,nx,ny))
            visited.add((nx,ny,x,y))
            x,y = nx,ny
    
    return len(visited)/2


print(solution("LULLLLLLU"))