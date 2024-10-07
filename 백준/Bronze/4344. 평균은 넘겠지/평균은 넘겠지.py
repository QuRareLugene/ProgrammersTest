#=-=-=-=-= 문제 =-=-=-=-=#
# 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.

#=-=-=-=-= 입력 =-=-=-=-=#
# 첫째 줄에는 테스트 케이스의 개수 C가 주어진다.
# 둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고,
# 이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

#=-=-=-=-= 출력 =-=-=-=-=#
# 각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.

# 테스트 케이스의 개수 C
TotalCase = int(input())

# 각 테스트 케이스마다 학생의 수 N이 주어진다. 
for tc in range(TotalCase):
    
    # 테스트 케이스가 일괄입력되기 때문에 스플릿으로 나눠야 한다.
    TestCase = input().split(' ')
    
    # 첫 입력은 학생의 수이다.
    StudentNumber = int(TestCase[0])
    TotalSum = 0
    OverCount = 0
    Score = []

    # 학생의 점수를 입력받아 리스트에 집어넣는다.
    for i in range(1,StudentNumber+1):
        Score.append(TestCase[i])
        TotalSum = TotalSum + int(Score[i-1])

    # 평균보다 더 큰 학생 수를 카운트한다.
    for i in range(StudentNumber):
        if int(Score[i]) > int(TotalSum/StudentNumber):
            OverCount += 1

    # 결과 출력
    print("{:.3f}%".format(OverCount/StudentNumber*100))
