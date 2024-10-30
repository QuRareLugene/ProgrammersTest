def solution(my_string):
    stringList = list(my_string)
    answerList = []
    for item in stringList:
        if item.isupper():
            answerList.append(item.lower())
        else:
            answerList.append(item.upper())
    return "".join(answerList)