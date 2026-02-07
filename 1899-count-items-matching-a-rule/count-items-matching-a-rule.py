class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        count = 0
        if ruleKey == 'type':
            for item in items:
                if item[0] == ruleValue:
                    count += 1
        
        if ruleKey == 'color':
            for item in items:
                if item[1] == ruleValue:
                    count += 1
        
        if ruleKey == 'name':
            for item in items:
                if item[2] == ruleValue:
                    count += 1
        return count

        