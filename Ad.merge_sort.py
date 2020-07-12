def merge(A, l, m, r):
    L = A[l:m+1]
    R = A[m+1:r+1]
    x ,y, k = 0, 0, l

    while x < len(L) and y < len(R):
        if L[x] < R[y]:
            A[k] = L[x]
            x += 1
            k += 1
        else:
            A[k] = R[y]
            k += 1
            y += 1

    while x < len(L):
        A[k] = L[x]
        k += 1
        x += 1

    while y < len(R):
        A[k] = R[y]
        k += 1
        y += 1


def merge_sort(A, l, r):
    if l >= r:
        return
    mid = (l+r)//2
    merge_sort(A, l, mid)
    merge_sort(A, mid+1, r)
    merge(A, l, mid, r)


if __name__ == "__main__":
    array = [33, 42, 9, 37, 8, 47, 5, 29, 49, 31, 4, 48, 16, 22, 26]
    merge_sort(array, 0, len(array) - 1)
    print(array)
