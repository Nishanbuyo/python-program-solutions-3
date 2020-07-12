def interpolationSearch(arr, n, key):
    l = 0
    h = (n - 1)

    while l <= h and key >= arr[l] and key <= arr[h]:
        if l == h:
            if arr[l] == key:
                return l
            return -1

        pos = l + int(((float(h - l) /
                         (arr[h] - arr[l])) * (key - arr[l])))

        if arr[pos] == key:
            return pos

        if arr[pos] < key:
            l = pos + 1

        else:
            h = pos - 1

    return -1


arr = [10, 12, 13, 16, 18, 19, 20, 21,
       22, 23, 24, 33, 35, 42, 47]
n = len(arr)

key = 18
index = interpolationSearch(arr, n, key)

if index != -1:
    print ("Element found at index", index)
else:
    print ("Element not found")
