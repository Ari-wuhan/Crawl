import requests
import re

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"
}
url = "https://lanqiao-horuikidi.vercel.app/"
res = requests.get(url=url, headers=headers)
html_data = res.text
results = re.findall('<h6 title="(.*)" class="course-name"', html_data)
print(results)