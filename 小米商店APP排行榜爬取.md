# 实验介绍
本实验将从 HTTP 协议开始为你讲述爬虫的底层原理，之后将 HTTP 协议与 requests 库进行知识关联，为你解释 requests 库是如何实现 HTTP 协议中的相关内容。在实验后半节将为大家讲解 re 模块与正则表达式的泛应用技巧，该技巧可以极大地提高正则表达式编写速度与 Python 爬虫编写效率。

* 知识点
* HTTP 协议介绍
* requests 库响应体
* re 模块与正则表达式泛应用
* 批量图片存储

# HTTP 协议介绍
学习爬虫需要对 HTTP 协议有一些了解，这样对于爬虫原理的理解会更加清晰，本实验开始部分将对 HTTP 协议做一些简单的介绍，由于课程核心为爬虫知识，HTTP 协议部分知识会以与爬虫关联度高的部分入手讲解，例如请求头、响应头、状态码以及内容类型。

## HTTP 消息结构
HTTP 协议（HyperText Transfer Protocol，超文本传输协议）是目前互联网使用最广泛的一种协议，例如你经常看到的网址 http://www.baidu.com，当访问百度网站的时候，其实就是使用 HTTP 协议，将数据从百度服务器传输到本地浏览器。

写爬虫就是通过 Python 程序去模拟这一过程，通过使用各种编程上的技巧，让网站服务器将数据通过 HTTP 协议返回给写好的解析程序，在将数据存储到本地。

对于 HTTP 消息结构，简单理解只有两部分构成：

* 客户端请求消息
* 服务器响应消息
客户端请求消息包括请求行、请求头、空行、请求数据四个部分，它们一般叫做请求报文。

服务器响应消息也是四个部分构成：状态行、消息报头、空行和响应正文。

以上内容在本系列实验中涉及的知识点包括：请求头、请求数据、响应正文，其它内容爬虫课程不做展开讲解。

学习到这里，相信大家已经对一个 HTTP 协议有了一个模糊的概念。接下来为了更好地掌握爬虫相关知识，还需要进行一个转换，将请求与响应切换成英文模式。请求对应的为 request，响应对应为 response，完成这一步之后，在打开谷歌浏览器的开发者工具，你可以快速定位到一个 HTTP 的请求消息与响应消息，具体参照下图右半部分：

图片描述

上图绿色框部分，包含了一些重要的请求头和响应头信息，我们依次进行解读。

首先是概括性部分：

图片描述

具体参数说明（只说明重要参数）：

    Request URL：请求地址；
    Request Method：请求方法；
    Status Code：状态码；
    Remote Address：当前 HTTP 请求的远程地址；
    Referrer Policy：用于设置 Referrer 策略，本系列实验不涉及。
概括性部分说明完毕，继续下翻找到 Request Headers 部分：

图片描述

该部分的参数将重点介绍，其中有很多参数都会对爬虫程序产生比较大的影响，甚至可以说所有的爬虫都是在不断的伪造一个相对真实的请求头，然后让网站或者 APP 服务器发送正确的数据到我们本地。

具体参数说明（只说明重要参数）：

* Accept：客户端（浏览器）期望接收的内容类型（有文档会解释成浏览器支持的 MIME 类型，由于会引出更多的概念，故省略），大意为服务器要给我返回什么格式的数据，可以是 HTML 网页文件，也可以是 PNG 图片，更可以是各种音视频；
* Accept-Encoding：客户端（浏览器）可以支持的内容压缩编码类型（一般不需要设置）；
* Accept-Language：客户端（浏览器）接受的语言格式；
* Cookie：服务端给客户端传的 HTTP 请求状态，原因是因为 HTTP 协议是无状态的（有兴趣的同学可以检索下何为无状态协议），所以需要存储一些信息带客户端（浏览器）用于下次 HTTP 发起请求时，将数据传回服务器，该参数非常重要，后续实验会有所涉及；
* Content-Length：请求内容的长度，一般用于请求音频或者视频等文件，需要借助文件大小实现；
* HOST：请求的服务器的域名和端口号；
* Referer：请求的上一个页面，该参数比较重要，爬虫程序经常需要借助该参数去访问一个网站的二级页面；
* User-Agent：浏览器 UA，包含了一个特征字符串，用来让服务器对客户端（浏览器）发来的请求进行应用类型、操作系统、软件开发商以及版本号的相关判断，非常重要的参数，上一实验已经进行介绍。
* 以上为请求头相关参数说明，对于响应头将在后续实验中进行补充说明，本实验只介绍响应体内容。

在开发者工具中，除了 Headers 选项卡以外，还有一个 Response 选项卡，该部分即为响应体内容，具体位置如下图所示：

图片描述

切换到 Response 选项卡下，你将看到源码内容，如果想查看源码效果，切换到 Response 之前的 Preview 即可。

HTTP 请求方法
在上一实验中，通过 get 方法你获取到实验楼的课程数据，我们也曾提及跟 get 方法像类似的操作在 requests 库中存在几个， post、 put、 delete、 head、 options，学习了 HTTP 协议之后，你将明白这些其实对应的是 HTTP 协议中的请求方法。

HTTP 目前有两种标准，分别是 HTTP1.0，HTTP1.1。具体标准有何差异依旧为大家的扩展学习知识。

HTTP1.0 定义了三种请求方法，这三种也是爬虫中最常见的三种，分别是 GET，POST，HEAD。

HTTP1.1 除了上述三种请求外，扩展了六种新的请求方法，分别是 OPTIONS、PUT、PATCH、DELETE、TRACE 和 CONNECT。

以上内容在有的教材上也被称作 HTTP 动词，requests 库提供了几乎所有 HTTP 动词的功能，鉴于本系列实验的定位，我们将把精力更多的放在 get 方法与 post 方法上。

## HTTP 状态码
编写爬虫你需要了解常见的 HTTP 状态码，很多时候可以直接借助状态码完成爬虫的基本操作，状态码非常多，你只需要记住 3 个常见的即可，分别是：

* 200 - 请求成功
* 404 - 请求的资源（网页等）不存在
* 500 - 内部服务器错误
在 Python 代码中展示一下如何获取状态码：

        import requests

        res = requests.get("http://app.mi.com/")
        # 输出请求到的响应状态码
        print(res.status_code)

上述代码最终输出的为 200，表示请求成功。在 requests 中内置了一个枚举可以直接用于判断是否请求成功：

    import requests

    res = requests.get("http://app.mi.com/")
    # 输出请求到的响应状态码
    if res.status_code == requests.codes.ok:
        print("请求成功")

对于 requests.codes.{具体的值} 在 requests 中提供了非常多的枚举，由于值非常多，我单独给大家准备了一个页面，可以查阅这个[地址](https://lanqiao-horuikidi.vercel.app/requests_code.html)。

# requests 库响应体

上文中通过一个很大的篇幅给大家介绍了 HTTP 协议，目的就是为了编写爬虫的过程中，你可以带上 HTTP 协议视角去解决问题，最常见的就是通过设定特定的请求头获取到理想的数据返回，这部分内容在本系列实验后续会逐步展开，本实验也会涉及其中上述 HTTP 协议参数中部分内容。

接下来要学习的内容是 requests 库响应内容，在 requests 中包含如下几种获取响应内容的方法：

r.text 以文本的方式访问响应体

r.content 以字节的方式访问响应体

r.json() 将响应体直接进行 json 序列化操作

r.raw 获取来自服务器的原始套接字响应（注意本部分内容不再本系列实验讲授范围）
## 以文本的方式访问响应体

直接获取 requests 请求发出后，服务器返回的文本数据是爬虫程序最常使用的技术，该方式一般用于网页源码的直接读取，例如下述代码，你将直接获取到百度服务器返回的网站源码。

将如下代码写入 /home/project/index.py 文件中：

    import requests

    res = requests.get("http://www.baidu.com/")

    if res.status_code == requests.codes.ok:
        print(res.text)

执行结果如下：

图片描述

对于代码中的 res.text 额外介绍一下，通过调用 response 对象的 text 属性，可以直接通过文本方式获取到响应体内容。这里还存在一个问题，数据虽然获取到了，但是编码并不正确，错误如下图所示：

图片描述

注意到红色箭头所指位置为乱码，绿色框中显示编码为 utf-8，表示获取到数据格式是 utf-8，但是并没有给响应体内容设置格式，下面用到的依旧是 response 对象的属性，通过 encoding 设置响应体编码。

将如下代码覆盖写入 /home/project/index.py 文件中：

    import requests

    res = requests.get("https://www.baidu.com/")
    # 设置响应体编码
    res.encoding = "utf-8"

    if res.status_code == requests.codes.ok:
        print(res.text)

再次执行代码，获取到的结果中文正常显示：

图片描述

以字节的方式访问响应体
通过字节的方式获取响应体主要场景应用在图片获取，文件获取，音频视频获取等内容获取上，例如实验一中获取一张图片，就是以该方式去获取响应体。

获取方式是通过调用 response 对象的 content 属性实现，例如下述代码将通过 res.content 获取一张图片的字节流。将如下代码写入 /home/project/icon.py 文件：

    import requests

    img_url = ("http://t5.market.xiaomi.com/thumbnail/jpeg/l750/AppStore"
            "/08636408ad50fc7396a2dcac92ac1b18b6842ddbc")
    res = requests.get(img_url)

    if res.status_code == requests.codes.ok:
        print(res.content)

执行程序的结果如下：

图片描述

代码中的 re.content 即为图片数据的十六进制编码，在下文我们将通过该方式去爬取 APP 的 ICON 图片。

## re 模块与正则表达式泛应用
爬虫程序对于某个技术点需要反复练习，尤其是一些比较基础的技术，re 模块与正则表达式在爬虫中所处的地位非常重要，所以本实验依旧采用它们二者来完成实验。

本实验要爬取的网站为 小米应用商店榜单 在这里案例中，你将使用到 requests 库对请求头的配置，你将通过文本与字节两种方式去获取待爬取数据。

先定义一下待爬取数据内容与格式。

图片描述

待爬取内容：

上述中各 APP 的标题与分类
各 APP 的图标图片，图片存储在本地电脑上的命名格式为【APP 名称.JPG】
## 获取单页面一项标题，分类，图片地址
为了达成目标，将任务进行拆解。第一步需要通过 re 模块获取目标页面第一项的元素标题，分类，图片地址，然后在进行扩展，在正式编码之前教给大家一个快速编写正则表达式的技巧，在大多数一般爬虫编写环境下，可以极大的提高你编写爬虫代码的速度。

打开浏览器开发者工具，通过抓手工具快速定位到你想要获取的元素区域。

图片描述

在选中的标签上（本案例中选中的为 li 标签）点击鼠标右键出现如下弹窗，选择 Edit as HTML。

图片描述

该标签会进入到快速编辑状态，将代码复制到 WebIDE 或者任意编辑器中，代码如下：

    <li>
    <a href="/details?id=com.tencent.tmgp.sgame"
        ><img
        data-src="http://file.market.xiaomi.com/thumbnail/PNG/l62/AppStore/00194c54cbc874fc23a30e1379f6b8a57ff08b6f5"
        src="http://file.market.xiaomi.com/thumbnail/PNG/l62/AppStore/00194c54cbc874fc23a30e1379f6b8a57ff08b6f5"
        alt="王者荣耀"
        width="72"
        height="72"
    /></a>
    <h5><a href="/details?id=com.tencent.tmgp.sgame">王者荣耀</a></h5>
    <p class="app-desc"><a href="/category/19">网游RPG</a></p>
    </li>

对上述内容开始着手改造，修改成目标正则表达式。

第一步，所有引号中的内容，修改为 (.*?)，修改完毕如下：

    <li>
    <a href="(.*?)"
        ><img data-src="(.*?)" src="(.*?)" alt="(.*?)" width="(.*?)" height="(.*?)"
    /></a>
    <h5><a href="(.*?)">王者荣耀</a></h5>
    <p class="(.*?)"><a href="(.*?)">网游RPG</a></p>
    </li>

这里，你可以通过 Python 进行一下验证，查看正则表达式是否正确。将如下代码覆盖写入 /home/project/index.py 文件：

    import requests
    import re
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1464.0 Safari/537.36"
    }

    def get_item():
        url = "http://app.mi.com/topList?page=1"
        res = requests.get(url=url, headers=headers)
        # 比对返回的状态码
        if res.status_code == requests.codes.ok:
            html = res.text
            # 编译正则表达式，生成一个正则表达式（ Pattern ）对象
            pattern = re.compile(
                r'<li><a href="(.*?)"><img data-src="(.*?)" src="(.*?)" alt="(.*?)" width="(.*?)" height="(.*?)"></a><h5><a href="(.*?)">王者荣耀</a></h5><p class="(.*?)"><a href="(.*?)">网游RPG</a></p></li>')
            m = pattern.search(html)
            # m.group(0) 返回整个匹配的字符串
            print(m.group(0))

    if __name__ == "__main__":
        get_item()

略微停一下正则部分，上述代码先补充一下 3 个知识点。

* 第 1 个为 re.compile 方法，该方法将一个正则表达式编译成一个对象，一般用变量 pattern 接收，之后即可通过 pattern 调用 search，findall 等方法，相当于编译一次正则表达式，在多次使用编译好的对象。

* 第 2 个知识点是 re.compile 方法中的字符串前面有个前缀 r，该符号防止字符转义，假设路径中出现 \n ， 不加 r 的话 \n 就会被转义，而加了 r 之后 \n 能保留原有的样子进行输出。

* 第 3 个知识点是 m.group(0) 将返回匹配成功的整个子字符串。

当上述代码运行完毕，发现成功匹配到了数据，但是存在问题，具体看下图：

图片描述

发现正则表达式和目标匹配结构出现差异，该情况即为正则表达式未达到预期效果，继续调整，在第 1 个 href 后面增加 /details 提高匹配精准度。

    <li>
    <a href="/details(.*?)"
        ><img data-src="(.*?)" src="(.*?)" alt="(.*?)" width="(.*?)" height="(.*?)"
    /></a>
    <h5><a href="(.*?)">王者荣耀</a></h5>
    <p class="(.*?)"><a href="(.*?)">网游RPG</a></p>
    </li>

这一次运行成功得到了 王者荣耀 这条数据。

图片描述

继续修改，让正则表达式变的更加通用，可以匹配整页数据，将所有 HTML 双标签中的文字替换为 (.*?)，也就是上图 王者荣耀 和 网游RPG 位置。

    <li>
    <a href="/details(.*?)"
        ><img data-src="(.*?)" src="(.*?)" alt="(.*?)" width="(.*?)" height="(.*?)"
    /></a>
    <h5><a href="(.*?)">(.*?)</a></h5>
    <p class="(.*?)"><a href="(.*?)">(.*?)</a></p>
    </li>

测试一下最新修改的正则表达式是否可用。这里我直接将代码调整到整页数据匹配，具体如下：

    import requests
    import re
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1464.0 Safari/537.36"
    }

    def get_item():
        url = "http://app.mi.com/topList?page=1"
        res = requests.get(url=url, headers=headers)
        # 比对返回的状态码
        if res.status_code == requests.codes.ok:
            html = res.text
            # 编译正则表达式，生成一个正则表达式（ Pattern ）对象
            pattern = re.compile(
                r'<li><a href="/details(.*?)"><img data-src="(.*?)" src="(.*?)" alt="(.*?)" width="(.*?)" height="(.*?)"></a><h5><a href="(.*?)">(.*?)</a></h5><p class="(.*?)"><a href="(.*?)">(.*?)</a></p></li>')
            items = pattern.findall(html)
            # m.group(0) 返回整个匹配的字符串
            print(items)

    if __name__ == "__main__":
        get_item()

运行代码，结果已经成功将本页所有数据匹配成功，具体内容如下：

图片描述

匹配成功的单条数据如下所示，其中会发现比预期的数据要多，要进行字段的解释与删减。

单条数据如下：

    ('?id=com.tencent.tmgp.sgame', 'http://file.market.xiaomi.com/thumbnail/PNG/l62/AppStore/00194c54cbc874fc23a30e1379f6b8a57ff08b6f5', 'http://resource.xiaomi.net/miuimarket/app/lazyload.gif', '王者荣耀', '/details?id=com.tencent.tmgp.sgame', '王者荣耀', 'app-desc', '/category/19', '网游RPG')
    copy
元组数据解释为：

    ('二级页面', 'ICON图标地址', '懒加载等待图标', 'APP名称', '二级页面', 'APP名称', 'class名称', '分类页面地址', '分类名称')
    copy
本实验目标为 APP 名称、分类名称、APP 图标图片，其余信息舍弃，重新调整正则表达式中的括号即可，修改如下：

    <li>
    <a href="/details.*?"
        ><img data-src="(.*?)" src=".*?" alt=".*?" width=".*?" height=".*?"
    /></a>
    <h5><a href=".*?">(.*?)</a></h5>
    <p class=".*?"><a href=".*?">(.*?)</a></p>
    </li>

截止到此，正则表达式快速编写已经完毕，并且已经获得了想要的数据，最终获取到的数据格式为：

    ('http://file.market.xiaomi.com/thumbnail/PNG/l62/AppStore/0d81fa52e5cae4e2f2b180d9f2058cb741cfa16e0', 'QQ浏览器', '实用工具')

上述正则表达式存在优化空间，大家可以自行扩展学习。

## 全部页面数据获取
单页页面数据匹配完毕之后，就可以对本实验中涉及的所有页面数据进行获取了，只需要通过一个循环即可实现，为方便代码编写，不在补充获取总页面部分代码，直接固定总页码数。

注意，学习过程中为防止对目标网站造成高频率访问，请通过 time 库设置延迟访问时间。

    import requests
    import re
    import time
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1464.0 Safari/537.36"
    }

    def get_item(page):
        url = "http://app.mi.com/topList?page={page}".format(page=page)
        res = requests.get(url=url, headers=headers)
        # 比对返回的状态码
        if res.status_code == requests.codes.ok:
            html = res.text
            # 编译正则表达式，生成一个正则表达式（ Pattern ）对象
            pattern = re.compile(
                r'<li><a href="/details.*?"><img data-src="(.*?)" src=".*?" alt=".*?" width=".*?" height=".*?"></a><h5><a href=".*?">(.*?)</a></h5><p class=".*?"><a href=".*?">(.*?)</a></p></li>')
            items = pattern.findall(html)
            # m.group(0) 返回整个匹配的字符串
            print(items)

    if __name__ == "__main__":
        for page in range(1, 43):
            print("正在爬取第{page}页".format(page=page))
            get_item(page)
            time.sleep(2)

至此，所有数据已经实现了爬取，本实验只缺少最后一环节，将爬取到的图片地址指定的图片保存到本地。

# 批量图片存储
在上述内容中已经将数据抓取到本地，只需进行格式化就可存储到本地文件中，接下来补充图片抓取函数。

首先创建一个存储图片的目录：

    mkdir -p ~/../project/icons

在图片下载的过程中，先屏蔽掉数据输出部分，还有需要提前在 project 目录中新建一个 icons 目录，用于存储下载的图片。

    import requests
    import re
    import time
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1464.0 Safari/537.36"
    }

    def save_img(img_url, name):
        img_res = requests.get(url=img_url, headers=headers)
        # 比对返回的状态码
        if img_res.status_code == requests.codes.ok:
            data = img_res.content
            with open("./icons/{name}.png".format(name=name), "wb") as f:
                f.write(data)
            print("{name} - 图片存储完毕".format(name=name))

    def get_item(page):
        url = "http://app.mi.com/topList?page={page}".format(page=page)
        res = requests.get(url=url, headers=headers)
        # 比对返回的状态码
        if res.status_code == requests.codes.ok:
            html = res.text
            # 编译正则表达式，生成一个正则表达式（ Pattern ）对象
            pattern = re.compile(
                r'<li><a href="/details.*?"><img data-src="(.*?)" src=".*?" alt=".*?" width=".*?" height=".*?"></a><h5><a href=".*?">(.*?)</a></h5><p class=".*?"><a href=".*?">(.*?)</a></p></li>')
            items = pattern.findall(html)
            # m.group(0) 返回整个匹配的字符串
            # print(items)
            for item in items:
                # item 数据为 ('图片地址', '我的世界夏季版', '休闲创意')
                save_img(item[0], item[1])

    if __name__ == "__main__":
        for page in range(1, 43):
            print("正在爬取第{page}页".format(page=page))
            get_item(page)
            time.sleep(2)

运行代码之后，你将在控制台看到如下内容输出，左侧文件导航中图片也会对应生成：

图片描述