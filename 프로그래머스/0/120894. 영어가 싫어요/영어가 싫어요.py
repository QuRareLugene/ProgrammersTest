def solution(numbers):
    numberList = list(numbers)
    answerList = []
    count = 0
    while len(numberList) > 0:
        count += 1
        if(numberList[0]) == "z":
            answerList.append("0")
            numberList = numberList[4:]
        elif(numberList[0]) == "o":
            answerList.append("1")
            numberList = numberList[3:]
        elif(numberList[0] == "t"):
            if(numberList[1] == "w"):
                answerList.append("2")
                numberList = numberList[3:]
            elif(numberList[1] == "h"):
                answerList.append("3")
                numberList = numberList[5:]
        elif(numberList[0] == "f"):
            if(numberList[1] == "o"):
                answerList.append("4")
                numberList = numberList[4:]
            elif(numberList[1] == "i"):
                answerList.append("5")
                numberList = numberList[4:]
        elif(numberList[0] == "s"):
            if(numberList[1] == "i"):
                answerList.append("6")
                numberList = numberList[3:]
            elif(numberList[1] == "e"):
                answerList.append("7")
                numberList = numberList[5:]
        elif(numberList[0] == "e"):
            answerList.append("8")
            numberList = numberList[5:]
        elif(numberList[0] == "n"):
            answerList.append("9")
            numberList = numberList[4:]
            
    return int("".join(answerList))