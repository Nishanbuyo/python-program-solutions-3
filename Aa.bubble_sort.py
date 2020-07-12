def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if (arr[j] > arr[j+1]):
                temp = arr[j]
                arr[j]= arr[j+1]
                arr[j+1] = temp
    return arr


arr = [2,8,4,8,6,3,5,1]

print(bubble_sort(arr))
