import requests

# 声明一个变量 url ,并将其赋值为 https://xxx (图片地址)
url = 'https://dn-simplecloud.shiyanlou.com/courses/uid214893-20200325-1585103411810?imageView2/2/h/150/q/100'

# 请求网络地址
'''requests.get 是 requests 内置的一个方法，
get 方法会发起一个 GET 请求，去请求网络上的一个地址，即我们要获取的图片地址'''
res = requests.get(url)

# 获取请求到的二进制数据流
'''res.content 中，res 是一个新变量，用于保存 requests 请求到的数据，
你可以通过 print(res) 对其进行直接打印，
 res.content 表示获取二进制文件流，主要用于图片，视频，音频等富文本载体的文件。'''
# 打开并写入文件
img = res.content

'''with... as ... with 上下文代码段，后续会有详细说明，该关键字可以保证文件一定会被关闭。'''
with open('./image.png','wb') as f:
    f.write(img)