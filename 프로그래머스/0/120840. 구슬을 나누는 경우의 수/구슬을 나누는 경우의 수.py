def factorial(number):
    answer = 1
    for i in range(number):
        answer *= (i+1)
    return answer

def solution(balls, share):
    count = 0
    total = 1
    while(count < share):
        count += 1
        total *= balls
        balls -= 1
    return total/factorial(share)