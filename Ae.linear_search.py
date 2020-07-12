def linear_search(arr, key):
    for i in range(len(arr)):
        if key == arr[i]:
            return i+1
    return -1


array = [33, 42, 9, 37, 8, 47, 5, 29, 49, 31, 4, 48, 16, 22, 26]

position = linear_search(array, 29)

if position == -1:
    print("Search Failure")
else:
    print("Search Successful")
    print("Element is present at {}th position".format(position))
