def solution(N, stages):
    Survivor = len(stages)
    Result = []
    Answer = []
    for i in range(1, N+1):
        Survivor = Survivor - stages.count(i-1)
        if Survivor !=0:
            Failrate = float(stages.count(i))/float(Survivor)
        else:
            Failrate = 0.0
        Result.append((i, Failrate))
    Result.sort(key=lambda x:x[1], reverse=True)
    for i in range(len(Result)):
        Answer.append(Result[i][0])
    return Answer