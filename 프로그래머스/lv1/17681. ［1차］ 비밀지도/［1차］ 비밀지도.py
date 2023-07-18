# 해설을 참조한 풀이.

def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        answer.append(str(bin(arr1[i]|arr2[i]))[2:].rjust(n,'0').replace('0',' ').replace('1','#'))
    return answer