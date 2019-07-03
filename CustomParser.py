from RomanNum import RomanNum
from constant import WordDic, CoinDic, Type

class CustomParser(object):

    def __init__(self, romanArr):
        self.RomanArray = romanArr
        self.RomanNum = RomanNum()

    def updateWordDic(self, InputLine):
        if InputLine[-1] in self.RomanArray:
            InputLine_array = InputLine.split(' ')
            WordDic[InputLine_array[0]] = InputLine_array[2]
            return

    def convertCredit(self, InputLine):
            InputLine_array = InputLine.split(' ')
            TempStr = ''
            for i in range(len(InputLine_array)-4):
                TempStr += WordDic[InputLine_array[i]]
            TempNum = self.RomanNum.get_roman_num(TempStr)
            CoinDic[InputLine_array[-4]] = \
            int(InputLine_array[-2])/int(TempNum)
            return

    def convertAndAnswer(self, InputLine):
        InputLine_array = InputLine.split(' ')
        #quantify  much, many and ??
        if InputLine_array[1] == 'much':
            romStr = ''
            interGal = ''
            for i in range(3, len(InputLine_array) - 1):
                interGal += InputLine_array[i] + ' '
                romStr += WordDic[InputLine_array[i]]
            return interGal + "is " + str(self.RomanNum.get_roman_num(romStr))

        elif InputLine_array[1] == 'many':
            romanStr = ''
            intGalactic = ''
            for i in range(4, len(InputLine_array) - 2):
                intGalactic += InputLine_array[i] + ' '
                romanStr += WordDic[InputLine_array[i]]
            return intGalactic + InputLine_array[-2] + ' is ' \
                   + str(CoinDic[InputLine_array[-2]] * \
                         self.RomanNum.get_roman_num(romanStr)) + ' Credits'

    def str_resolve(self, InputLine):
        '''
        Custom Parser : Based on Type : Parse it and convert it and displays output
        :param InputLine:
        :return:
        '''
        if Type(InputLine[-1]) == "in":
            return self.updateWordDic(InputLine)
        elif Type(InputLine[-1]) == "out":
            return self.convertAndAnswer(InputLine)
        else:
            return self.convertCredit(InputLine)
