# -*- coding:utf_8 -*-

class Solution(object):
    def bubble_sort(self,nums):
        count = len(nums)
        if count <= 1:
            return nums
        for i in range(0,count):
            for j in range(i+1,count):
                if nums[i] > nums[j]:
                    nums[i],nums[j] = nums[j],nums[i]
        return nums

    def merge(self,left,right):
        result = []
        while left and right:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        if left:
            result += left
        if right:
            result += right
        return result

    def merge_sort(self,nums):
        if len(nums) <=1:
            return nums
        mid = len(nums)/2
        left = nums[:mid]
        right = nums[mid:]

        left = self.merge_sort(left)
        right = self.merge_sort(right)
        return self.merge(left,right)

    def quick_sort(self,nums):
        if len(nums) <= 1:
            return nums
        left = []
        mid = [nums[-1]]
        right = []
        for i in range(0,len(nums)-1):
            if nums[i] < nums[-1]:
                left.append(nums[i])
            elif nums[i] > nums[-1]:
                right.append(nums[i])
            else:
                mid.append(nums[-1])
        lefta = self.quick_sort(left)

        righta = self.quick_sort(right)
        return lefta+mid+righta

if __name__ == '__main__':
    l = [3,5,2,3,6,1,7,9]
    l1 = [3]
    a = Solution()
    print a.quick_sort(l)
    print a.quick_sort(l1)
    print a.merge_sort(l)
