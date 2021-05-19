import requests
import re

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"
}
url = "https://lanqiao-horuikidi.vercel.app/"
res = requests.get(url=url, headers=headers)
html_data = res.text
# 匹配数据，获取所有的课程标题
results = re.findall('<h6 title="(.*)" class="course-name"', html_data)

for item in results:
    # 格式化字符串
    new_str = "课程名：{item}\n".format(item=item)
    # 将格式化之后的数据写入文件
    with open("./data.txt", "a", encoding="utf-8") as f:
        f.write(new_str)