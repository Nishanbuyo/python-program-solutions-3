def binary_search(items, key):
    l, h = 0, len(items)-1
    while(l<=h):
        mid = (l+h)//2
        if key == items[mid]:
            return mid
        elif( key < items[mid]):
            h= mid-1
        else:
            l=mid+1
    return -1

items = [2,3,4,6,7,8,12,14,23,45,67]
print(binary_search(items, 6))
print(binary_search(items, 2))
print(binary_search(items, 1))
print(binary_search(items, 67))
print(binary_search(items, 12))
print(binary_search(items, 9))