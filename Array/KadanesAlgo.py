import sys
def maxSumSubArray(arr, size):
    maxSum = -sys.maxsize-1
    curSum = 0
    for i in range(0, size):
        curSum = curSum + arr[i]
        if (curSum > maxSum):
            maxSum = curSum
        if (curSum < 0):
            curSum = 0
    return maxSum

a = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
print("Maximum contiguous sum is", maxSumSubArray(a,len(a)))


# def maxSubArraySum(a, size):
#     max_so_far = a[0]
#     max_ending_here = 0
#
#     for i in range(0, size):
#         max_ending_here = max_ending_here + a[i]
#         if max_ending_here < 0:
#             max_ending_here = 0
#
#         # Do not compare for all elements. Compare only
#         # when  max_ending_here > 0
#         elif (max_so_far < max_ending_here):
#             max_so_far = max_ending_here
#
#     return max_so_far


# def maxSubArraySum(a, size):
#     max_so_far = a[0]
#     curr_max = a[0]
#
#     for i in range(1, size):
#         curr_max = max(a[i], curr_max + a[i])
#         max_so_far = max(max_so_far, curr_max)
#
#     return max_so_far
#
#
# # Driver function to check the above function
# a = [-2, -3, 4, -1, -2, 1, 5, -3]
# print
# "Maximum contiguous sum is", maxSubArraySum(a, len(a))