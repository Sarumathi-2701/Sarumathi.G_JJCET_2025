"""Product of Array Except Self
Companies
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer."""




class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
                res = [1]
                for num in nums:
                    
                    res.append(res[-1]*num)
                    b = 1   
                for i in range(len(nums)):
                    res[len(nums)-i-1] = res[len(nums)-i-1] * b
                    b = b* nums[len(nums)-i-1]
            
                return res[0:-1]
