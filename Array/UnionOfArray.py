#method1
# def Union(arr1, arr2, m, n):
#     i, j = 0, 0
#     count = 0
#     while (i < m and j < n):
#         if (arr1[i] < arr2[j]):
#             i = i + 1
#         elif (arr1[i] > arr2[j]):
#             j = j + 1
#         else:
#             i = i + 1
#             j = j + 1
#         count = count + 1
#
#     while (i < m):
#         count = count + 1
#         i = i + 1
#     while (j < n):
#         count = count + 1
#         j = j + 1
#     return count
#
#
arr1 = [1, 2, 4, 5, 6]
arr2 = [2, 3, 5, 7]
# m = len(arr1)
# n = len(arr2)
# print(Union(arr1, arr2, m, n))



#method 2
# newarr = []
# for ele1 in arr1:
#     if (ele1 not in newarr):
#         newarr.append(ele1)
# for ele2 in arr2:
#     if (ele2 not in newarr):
#         newarr.append(ele2)
# print(len(newarr))

# method3
# c=set(arr1+arr2)
# print(len(c))


#meyhod 4
# dic={}
# for ele1 in arr1:
#     if ele1 not in dic:
#         dic[ele1]=1
# for ele2 in arr2:
#     if ele2 not in dic:
#         dic[ele2]=1
# count=0
# for ele in dic:
#     count=count+1
# print(count)
