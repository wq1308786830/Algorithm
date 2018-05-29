# -*- coding: utf-8 -*-
# !/usr/bin/python


class Solution:

    @staticmethod
    def removeDuplicates(nums):
        """
        remove duplicated items in an array.
        :param nums:
        :return:
        """
        i = 0
        j = 1
        for r in range(len(nums)):
            if j >= len(nums):
                print(i + 1, nums)
                return i + 1
            if nums[i] != nums[j]:
                i = i + 1
                nums[i] = nums[j]
            j = j + 1

    @staticmethod
    def maxProfit(prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        if not prices:
            return profit
        for i in range(len(prices)):
            if i + 1 >= len(prices):
                print(profit)
                return profit
            if prices[i] < prices[i + 1]:
                profit += prices[i + 1] - prices[i]

    @staticmethod
    def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(1 + i, len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    print([nums[i], nums[j]])
                    return [i, j]


Solution.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
Solution.maxProfit([7, 6, 4, 3, 1])
Solution.twoSum([2, 7, 11, 15], 9)
