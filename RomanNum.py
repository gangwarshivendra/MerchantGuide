from constant import romanDict

class RomanNum(object):
    def __init__(self):
        self.RomanDict = romanDict

    def get_roman_num(self,RomanStr):
        '''
            convert roman string to number.
        :param RomanStr:
        :return:
        '''
        res = 0
        for i in range(0, len(RomanStr)):
            if i == 0 or self.RomanDict[RomanStr[i]] <= self.RomanDict[RomanStr[i - 1]]:
                res += self.RomanDict[RomanStr[i]]
            else:
                res += self.RomanDict[RomanStr[i]] - 2 * self.RomanDict[RomanStr[i - 1]]
        return res
