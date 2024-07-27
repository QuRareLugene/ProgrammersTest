def gcd(a, b):
    if a>b:
        a, b = b, a
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b / gcd(a, b)
    
def solution(numer1, denom1, numer2, denom2):
    denom = lcm(denom1, denom2)
    numer = (denom/denom1)*numer1 + (denom/denom2)*numer2
    
    ngcd = gcd(numer, denom)
    n_denom = int(denom/ngcd)
    n_numer = int(numer/ngcd)
    answer = [n_numer, n_denom]
    return answer