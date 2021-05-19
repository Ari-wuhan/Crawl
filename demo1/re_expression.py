import re

# re.match('要匹配的正则表达式'，'待匹配的字符串')
result1 = re.match('实','实验楼Pyhon')
result2 = re.match('验','实验楼PYTHON')
print(result1)
print(result2)

result3 = re.match('实\w','实验楼Pyhon')
result4 = re.match('\w验','实验楼PYTHON')
print(result3)
print(result4)