class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        str_digits = map(str, digits)
        joined_str = "".join(str_digits)

        num = int(joined_str) + 1

        new_list = [int(digit) for digit in str(num)]
        return new_list
        