def solution(arr) :
    to_set = list(set(arr))
    to_set.sort(reverse=True)
    return to_set

ex_list = [2,45,6,1,2,1]

print(solution(ex_list))
