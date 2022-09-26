from itertools import combinations as combi




nums = [1,3,5,8]

total = []

for i in range(len(nums)-1,1,-1):
    for j in list(combi(nums,i)):
        sum = 0
        for k in nums:
            if k in j:
                sum = sum + k
            else:
                sum = sum - k
        total.append(sum)


abstotal = []

for i in total:
    abstotal.append(abs(i))

count = 0

for i in abstotal:
    if min(abstotal) == i :
        count = count + 1

print(count)
    