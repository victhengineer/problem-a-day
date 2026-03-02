class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        current_index = 0
        search_index= 0
        length = len(numbers)

        for i in range(length):
            current_index = i
            search_value = target - numbers[i]
            lower_bound = i + 1
            upper_bound = length - 1

            while lower_bound <= upper_bound:
                midpoint = (lower_bound + upper_bound) // 2
                value_at_midpoint = numbers[midpoint]
                if value_at_midpoint == search_value:
                    search_index = midpoint
                    break
                elif value_at_midpoint > search_value:
                    upper_bound = midpoint - 1
                elif value_at_midpoint < search_value:
                    lower_bound = midpoint + 1
            if search_index > 0:
                break
        return [current_index + 1, search_index + 1]
             