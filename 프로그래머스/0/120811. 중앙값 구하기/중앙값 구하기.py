def solution(array):
    
    array.sort()
    idx = int(len(array)/2)
    return array[idx]