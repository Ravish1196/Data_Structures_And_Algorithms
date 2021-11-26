# # Method Using Two Pointers
# def reverseList(A, start, end):
#     while (start < end):
#         # temp = A[start]
#         # A[start] = A[end]
#         # A[end] = temp
#         A[start], A[end] = A[end], A[start]
#         start = start + 1
#         end = end - 1
#     return A
#
#
# A = [1, 2, 3, 4, 5, 6]
# print(A)
# reverseList(A, 0, 5)
# print("ReversedList")
# print(A)


# method using recursion

# def reverseList(A, start, end):
#     if (start < end):
#         # temp = A[start]
#         # A[start] = A[end]
#         # A[end] = temp
#         A[start], A[end] = A[end], A[start]
#         reverseList(A, start + 1, end - 1)
#     return A
#
#
# A = [1, 2, 3, 4, 5, 6]
# print(A)
# reverseList(A, 0, 5)
# print("ReversedList")
# print(A)


#slicing
# print(A[::-1])