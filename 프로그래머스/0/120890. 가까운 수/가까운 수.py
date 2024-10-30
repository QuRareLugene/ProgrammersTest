def solution(array, n):
    array.append(n)
    sortedArr = sorted(array)
    for index in range(len(sortedArr)):
            
        if sortedArr[index] == n:
            if index == len(sortedArr) -1:
                return sortedArr[index-1]
            elif index == 0:
                return sortedArr[1]
            else:
                lower = sortedArr[index-1]
                higher = sortedArr[index+1]
                if(n - lower) > (higher - n):
                    return higher
                else:
                    return lower