def solution(absolutes, signs):

    sum = 0
    for i in range(len(absolutes)):
        if (signs[i]):
            sum = sum + absolutes[i]
        else:
            sum = sum - absolutes[i]
    answer = sum
    return answer