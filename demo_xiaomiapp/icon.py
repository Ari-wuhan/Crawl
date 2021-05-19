import requests

img_url = ("http://t5.market.xiaomi.com/thumbnail/jpeg/l750/AppStore"
           "/08636408ad50fc7396a2dcac92ac1b18b6842ddbc")
res = requests.get(img_url)

if res.status_code == requests.codes.ok:
    print(res.content)