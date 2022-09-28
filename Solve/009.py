def solution(id_list, report, k):
    
    report = (list(set(report)))
    total = []
    for i in report:
        total.append(tuple(i.split(" ")))
    
    
    d = {}
    # k가 넘는 애들 색출
    for i in total:
        d[i[1]] = d.get(i[1],0) + 1
    
    singo = []
    for i in d :
        if(d.get(i)>=k):
            singo.append(i)
    
    last = {}
    
    for i in total:
        a,b = i
        if b in singo:
            last[a] = last.get(a,0) + 1
    answer = []
    for i in id_list:
        answer.append(last.get(i,0))
    
    
    return answer