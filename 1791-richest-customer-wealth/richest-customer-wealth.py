class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        highest_wealth = 0

        for i in range(len(accounts)):
            wealth = 0
            for num in accounts[i]:
                wealth += num
            if wealth > highest_wealth:
                highest_wealth = wealth

        return highest_wealth