def solution(numbers, direction):
    
    answer = numbers*2
    
    if direction == "left":
        return answer[1:len(numbers)+1]
    else:
        return answer[len(numbers)-1:-1]