def solution(n):
    CMList = []
    for i in range(2,10001):
        while(n%i == 0):
            CMList.append(i)
            n = n//i
        if n == 1:
            break
    answer = list(set(CMList))
    return sorted(answer)