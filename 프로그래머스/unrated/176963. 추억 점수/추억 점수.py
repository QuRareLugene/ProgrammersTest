def solution(name, yearning, photo):
    answer = []
    for item in photo:
        sum = 0
        for person in item:
            if person in name:
                sum += yearning[name.index(person)]
        answer.append(sum)
    return answer