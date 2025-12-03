import time

def bubble_sort(arr) :
    k = len(arr)
    for i in range(k) :
        for j in range(k-i-1) :
            if arr[j] > arr[j+1] :
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
    return arr

def do_sort(arr) :
    p = sorted(arr)
    return p

def measure(func, arr) :
    start_time = time.time()
    list_result = func(arr)
    end_time = time.time()
    return list_result, end_time - start_time

arr_ex = list(range(10000))

bubble_time, bubble_result = measure(bubble_sort, arr_ex)
print(bubble_result)

sort_time, sort_result = measure(do_sort, arr_ex)
print(sort_result)