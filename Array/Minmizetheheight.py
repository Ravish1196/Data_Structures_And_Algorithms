# Make an array of all possible heights with the tower number, i.e. if height of any tower is h then we will insert h+k in the array and h-k(we will insert h-k in the array only if h-k ≥ 0).
# Sort the array.
# Find the index upto which height of every tower is included from the starting. Initialise the answer to the difference between height at this index and starting index.
# Then with the help of two pointer technique increment the left pointer which was initially at 0 such that one of the tower is not included.
# Similarly increment right pointer to make all towers included and update the answer. Do this until end of the array.


# User function Template for python3

class Solution:
    def getMinDiff(self, arr, n, k):
        # code here
        mini = 0
        maxi = 0
        r = 0
        arr.sort()
        r = arr[n - 1] - arr[0]
        for i in range(1, n):
            if (arr[i] >= k):
                maxi = max(arr[i - 1] + k, arr[n - 1] - k)
                mini = min(arr[i] - k, arr[0] + k)
                r = min(r, maxi - mini)
            else:
                continue
        return r


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends