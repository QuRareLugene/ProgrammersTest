def solution(num_list, n):
    answer = []
    chunk_count = len(num_list)//n
    i=0
    for count in range(chunk_count):
        answer.append([])
        for itemcount in range(n):
            answer[count].append(num_list[i])
            i+=1
    return answer