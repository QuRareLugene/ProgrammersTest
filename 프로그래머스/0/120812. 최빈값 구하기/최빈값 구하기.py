def solution(array):
    distinct_numbers = set(array)
    
    count_dict = {}
    for d_nums in distinct_numbers:
        count_dict[d_nums] = 0
    
    for item in array:
        count_dict[item] += 1
        
    max_count = list(count_dict.values()).count(max(count_dict.values()))
    if max_count > 1:
        return -1
    else:
        return max(count_dict, key=count_dict.get)