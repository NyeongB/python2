from collections import deque

def solution(maps):
    answer = 0
    
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    
    q = deque()
    q.append((0,0))
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] == 1:
                q.append((nx,ny))
                maps[nx][ny] = maps[x][y] + 1
    
    answer = maps[len(maps)-1][len(maps[0])-1]
    
    return answer if answer > 1 else -1