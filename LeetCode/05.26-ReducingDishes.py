"""
https://leetcode.com/problems/reducing-dishes/submissions/
"""
class Solution(object):
    def maxSatisfaction(self, dishes):
        dishes.sort(reverse=True) 
        max_sum = 0
        sum_dish = 0
        current_sum = 0

        for i in range(len(dishes)):
            current_sum += sum_dish + dishes[i]
            if current_sum > max_sum:
                max_sum = current_sum
                sum_dish += dishes[i] 
            else: 
                break
        return max_sum

Solution.maxSatisfaction([-9,-8,5,-1,0])
#return 14