def solution(arr) :
    arr2 = []
    k = len(arr)
    for i in range(k) :
        for j in range(i+1, k) :
            arr2.append(arr[i] + arr[j])
    arr2 = sorted(set(arr2))
    return arr2

ex = [5,0,2,7]
print(solution(ex))