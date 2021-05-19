# 导入模块
import requests
import re

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"
}
url = "https://lanqiao-horuikidi.vercel.app/"
# 发送数据请求
res = requests.get(url=url, headers=headers)
html_data = res.text
# 通过正则匹配数据解析
result = re.search("<title>(.*)</title>", html_data)
print(result.group(1))