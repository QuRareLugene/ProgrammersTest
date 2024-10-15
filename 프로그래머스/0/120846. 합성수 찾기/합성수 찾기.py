def isprime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(n):
    count = 0
    for i in range(2, n + 1):  # 1은 합성수도 소수도 아님
        if not isprime(i):
            count += 1
    return count
