# def rearrange(arr, n):
#     j = 0
#     for i in range(len(arr)):
#         if (arr[i] < 0):
#             temp = arr[i]
#             arr[i] = arr[j]
#             arr[j] = temp
#             j = j + 1
#     return arr
#
# arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
# n = len(arr)
# res=rearrange(arr, n)
# print(res)


# two pointer approach
def rearrange(arr, left, right):
    while (left <= right):
        if (arr[left] < 0 and arr[right] < 0):
            left = left + 1
        elif (arr[left] < 0 and arr[right] > 0):
            left = left + 1
            right = right - 1
        elif (arr[left] > 0 and arr[right] < 0):
            arr[left], arr[right] = arr[right], arr[left]
            left = left + 1
            right = right - 1
        else:
            right=right-1
    return arr


arr = [-12, 11, -13, -5,
       6, -7, 5, -3, 11]
n = len(arr)
res = rearrange(arr, 0, n - 1)
print(res)
