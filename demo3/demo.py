import requests
from lxml import etree

def get_pokemons_fromfile():
    try:
        with open("./target.html", "r", encoding="utf-8") as f:
            data = f.read()
            return data
    except Exception as e:
        return None

def analysis_byxpath(data):
    html = etree.HTML(data)
    all_li = html.xpath("//div[@class='mf-section-1']//li")
    print(len(all_li))
    for li in all_li:
        pid = li.xpath('./text()')[1]
        name = li.xpath('./a/text()')[0]
        print(pid,name)
    '''print(html)
    # 选取页面中 title 标签
    title = html.xpath("//title")
    print(title)
    # 选取页面中所有的 a 标签
    all_a = html.xpath("//a")
    # 输出所有 a 标签的文本
    all_a_text = html.xpath("//a/text()")
    print(all_a_text)
    # 输出 id="firstHeading" 的 h1 标签的文本内容
    h1_text = html.xpath("//h1[@id='firstHeading']/text()")
    print(h1_text)'''

if __name__ == "__main__":
    data = get_pokemons_fromfile()
    analysis_byxpath(data)