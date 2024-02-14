import requests
import re
def get_price(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/'
                             '537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'}
    resp = requests.get(url, headers=headers)
    pageSource = resp.text
    obj=re.compile(r'<a href="javascript:;" class="nostyle">.*?<span>(?P<name>.*?)元/㎡</span>',re.S)
    obj.finditer(pageSource)
    result = obj.finditer(pageSource)
    list1 = []
    for item in result:
        list1.append(int(item.group("name")))
    list1.reverse()
    for i in range(0,len(list1)):
        print(list1[i])

for i in range(14, 24):
        url = f"https://www.anjuke.com/fangjia/guangzhou20{i}"
        get_price(url)

