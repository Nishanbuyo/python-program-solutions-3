def partition(arr, l, r):
    p = arr[l]
    x = l + 1
    y = r

    while True:
        while x <= y and arr[y] >= p:
            y = y - 1

        while x <= y and arr[x] <= p:
            x = x + 1

        if x <= y:
            arr[x], arr[y] = arr[y], arr[x]
        else:
            break

    arr[l], arr[y] = arr[y], arr[l]

    return y


def quick_sort(arr, l, r):
    if l > r:
        return
    p = partition(arr, l, r)
    quick_sort(arr, l, p-1)
    quick_sort(arr, p+1, r)


data_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort(data_list, 0, len(data_list)-1)
print(data_list)
