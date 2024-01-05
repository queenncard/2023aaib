class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums) #問題的長度
        ans = 1
        table = [0]*N #放小答案的表格
        table[0] = 1 #最簡單的問題的答案，就是我自己1個數字
        for i in range(1,N):
            table[i] = 1
            for k in range(i):
                if nums[i]>nums[k] and table[k]+1>table[i]:
                    table[i] = table[k]+1

            if table[i] > ans: ans = table[i]
        return ans