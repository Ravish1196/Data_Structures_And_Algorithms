class Solution:
    def sort012(self, arr, n):
        # code here
        count1 = 0
        count2 = 0
        for ele in arr:
            if (ele == 0):
                count1 += 1
            elif (ele == 1):
                count2 += 1
        for i in range(0, count1):
            arr[i] = 0
        for i in range(count1, count2 + count1):
            arr[i] = 1
        for i in range(count2 + count1, n):
            arr[i] = 2
        return arr


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        ob.sort012(arr, n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends