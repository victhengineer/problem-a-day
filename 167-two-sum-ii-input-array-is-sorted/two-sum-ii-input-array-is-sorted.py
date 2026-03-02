class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(numbers)

        for i in range(length):
            search_value = target - numbers[i]
            lower_bound = i + 1
            upper_bound = length - 1

            while lower_bound <= upper_bound:
                midpoint = (lower_bound + upper_bound) // 2
                value_at_midpoint = numbers[midpoint]
                if value_at_midpoint == search_value:
                    return [i + 1, midpoint + 1]
                elif value_at_midpoint > search_value:
                    upper_bound = midpoint - 1
                elif value_at_midpoint < search_value:
                    lower_bound = midpoint + 1
             