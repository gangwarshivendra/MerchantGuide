#Global store/variables
WordDic = {}
CoinDic = {}
romanArr = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
romanDict ={'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#Utility Function
Type = lambda x : "in" if x in romanArr else ("out" if x == '?' else "convert")
