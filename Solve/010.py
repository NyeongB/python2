def solution(survey, choices):
    answer = ''
    d = {'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    for i in range(len(survey)):
        a,b = survey[i], choices[i]
        f,e = a[0], a[1]
        if b != 4:
            if b <= 4:
                d[f] = 4 - b + d.get(f,0)
            else:
                d[e] = b - 4 + d.get(e,0)
    
    
    if d['R'] >= d['T']:
        answer = answer + 'R'
    else:
        answer = answer + 'T'
        
    if d['C'] >= d['F']:
        answer = answer + 'C'
    else:
        answer = answer + 'F'
        
    if d['J'] >= d['M']:
        answer = answer + 'J'
    else:
        answer = answer + 'M'
        
    if d['A'] >= d['N']:
        answer = answer + 'A'
    else:
        answer = answer + 'N'        
            
            
    
    
    return answer