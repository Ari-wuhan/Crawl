import re
# 声明待爬取的字符串

html = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>实验楼Python爬虫实战课程</title>
</head>
<body>
    <h2>梦想橡皮擦老师的课程</h2>
</body>
</html>
"""

# 通过 search 匹配数据
# 注意在h2的后面存在一个空格，
# 之后是.*表示匹配任意字符，在之后是一个>，用于和后面的内容做一下区分
result = re.search('<h2.*>(.*)</h2>',html)
print(result)
print(result.group(1))