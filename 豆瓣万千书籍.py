import requests
import time
import random
from lxml import etree
import sys

num = 0
hots = []
book_names = []
fp = open('豆瓣万千书籍.txt','a',encoding='utf-8')

url_front = 'http://e.dangdang.com/media/api.go?action=mediaCategoryLeaf&promotionType=1&deviceSerialNo=html5&macAddr=html5&channelType=html5&permanentId=20201118212149386182782987171462841&returnType=json&channelId=70000&clientVersionNo=5.8.4&platformSource=DDDS-P&fromPlatform=106&deviceType=pconline&token=&'
url_back = '&category=XS2&dimension=dd_sale'
headers_1 = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0',
}
headers_2 = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3775.400 QQBrowser/10.6.4209.400',
}

headers_3 = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763',
}
headers_4 = {
    'user-agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
}
headers_5 = {
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36',
}
headers_6 = {
    'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0',
}
headers_7 = {
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14',
}
headers_8 = {
    'user-agent':'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)',
}
headers_9 = {
    'user-agent':'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
}
headers_10 = {
    'user-agent':'Opera/9.25 (Windows NT 5.1; U; en)',
}
headers_11 = {
    'user-agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
}
headers_12 = {
    'user-agent':'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
}
headers_13 = {
    'user-agent':'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
}
headers_14 = {
    'user-agent':'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
}
headers_15 = {
    'user-agent':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7',
}
headers_16 = {
    'user-agent':'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 ',
}
headers_17 = {
    'user-agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
}
headers_18 = {
    'user-agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
}
headers_19 = {
    'user-agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
}
headers_20 = {
    'user-agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
}
headers_21 = {
    'user-agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
}
headers_22 = {
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
}
headers_23 = {
    'user-agent':'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
}
headers_24 = {
    'user-agent':'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
}
headers_25 = {
    'user-agent':'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
}
headers_26 = {
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
}
headers_27 = {
    'user-agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)',
}
headers_28 = {
    'user-agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)',
}
headers_29 = {
    'user-agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
}
headers_30 = {
    'user-agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)',
}
headers_31 = {
    'user-agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
}
headers_32 = {
    'user-agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
}
headers_33 = {
    'user-agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)',
}
headers_34 = {
    'user-agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
}
headers_35 = {
    'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
}
headers_35 = {
    'user-agent':'Mozilla/5.0 (X11; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0',
}

headers = [headers_1,headers_2,headers_3,headers_4,headers_5,headers_6,headers_7,headers_8,headers_9,headers_10,
           headers_11,headers_12,headers_13,headers_14,headers_15,headers_16,headers_17,headers_18,headers_19,
           headers_20,headers_21,headers_22,headers_23,headers_24,headers_25,headers_26,headers_27,headers_28,
           headers_29,headers_30,headers_31,headers_32,headers_33,headers_34,headers_35]
def pa_page(i,j,num,fp):
    def re_link(i,j):
        try:
            ret = requests.get(url=url_front + 'start=' + str(i) + '&end=' + str(j) + url_back,headers=headers[random.randint(0, 34)], timeout=5)
            return ret
        except requests.exceptions.ConnectionError:
            print('连接错误,现在正在重新尝试(大页)')
            return re_link(i,j)
        except Exception as e:
            print('其他错误(大页位置) : '+repr(e))
            ret = -1
            return ret
    ret = re_link(i,j)
    if ret == -1:
        num = ret
        return num
    else:
        r = ret

    for i in r.json()['data']['saleList']:
        book = (i['mediaList'])[0]
        try:
            book_name = book['title']
            book_type = book['categorys']
            author_name = book['authorPenname']
            book_price = book['lowestPrice']
            book_image = book['coverPic']
            book_content = book['descs']
            nextweb_url = 'http://e.dangdang.com/products/'+str(book['mediaId'])+'.html'
        except:
            print(book)
        def re_link2(nextweb_url,headers):
            try:
                r2 = requests.get(url=nextweb_url, headers=headers[random.randint(0, 34)],timeout=5)
                return r2
            except requests.exceptions.ConnectionError: # 如果与服务器连接发生错误
                print('连接错误,现在正重新尝试(小页)')
                return re_link2(nextweb_url,headers)
            except Exception as e:
                print('其他错误(小页位置) : '+repr(e))
                return re_link2(nextweb_url,headers)

        r2 = re_link2(nextweb_url,headers)
        html = etree.HTML(r2.content)
        num += 1
        fp.write(str(num))
        fp.write('\n')
        fp.write('书名     ： '+book_name)
        fp.write('\n')
        fp.write('书籍类型 ： '+book_type)
        fp.write('\n')
        fp.write('作者     ： ' + author_name)
        fp.write('\n')
        fp.write('价格     ： ' + str(book_price)+'元')
        fp.write('\n')
        fp.write('封面网址 ： ' + book_image)
        fp.write('\n')
        fp.write('简介     ： ' + book_content)
        fp.write('\n')

# 这个try是为了解决num(大页)=207时hot无法获取的一个问题
        try:
            hot = str(html.xpath('//*[@id="productBookDetail"]/div[2]/div[1]/div[2]/text()')[0])
        except:
            print('《东方》书籍热度无法获取问题-已解决(默认热度为0)')
            hots.append(0)
            book_names.append(book_name)
            fp.write('热度     ： ' + str(0))
            fp.write('\n')
            fp.write('\n')
            return num

        hot_mid = hot
        state = False
        state_10000 = False
        for i in range(len(hot)):
            if hot_mid[i] == '万':
                state = True
                state_10000 = True
            if hot_mid[i] == '人':
                state = True
            if state or hot_mid[i] not in '0123456789':
                hot_mid = hot_mid.replace(str(hot_mid[i]),' ')
        hot = int(hot_mid.replace(' ',''))
        if state_10000:
            hot = hot*10000
        hots.append(hot)
        book_names.append(book_name)
        fp.write('热度     ： ' + str(hot))
        fp.write('\n')
        fp.write('\n')
        r2.close()
    r.close()
    return num

for i in range(1000):
    print(i)
    number = i*21
    num = pa_page(number,number+20,num,fp)
    if num == -1:
        break
    time.sleep(5)

max_1 = 0
max_2 = 0
max_3 = 0
max_4 = 0
max_5 = 0
max_6 = 0
max_7 = 0
max_8 = 0
max_9 = 0
max_10 = 0
state_2 = True
state_3 = True
state_4 = True
state_5 = True
state_6 = True
state_7 = True
state_8 = True
state_9 = True
state_10 = True

hots_sort = sorted(hots,reverse=True)
for i in range(len(hots)):
    if hots[i] >= hots_sort[9]:
        if hots[i] == hots_sort[9] and state_10:
            max_10 = i
            state_10 = False
        elif hots[i] == hots_sort[8] and state_9:
            max_9 = i
            state_9 = False
        elif hots[i] == hots_sort[7] and state_8:
            max_8 = i
            state_8 = False
        elif hots[i] == hots_sort[6] and state_7:
            max_7 = i
            state_7 = False
        elif hots[i] == hots_sort[5] and state_6:
            max_6 = i
            state_6 = False
        elif hots[i] == hots_sort[4] and state_5:
            max_5 = i
            state_5 = False
        elif hots[i] == hots_sort[3] and state_4:
            max_4 = i
            state_4 = False
        elif hots[i] == hots_sort[2] and state_3:
            max_3 = i
            state_3 = False
        elif hots[i] == hots_sort[1] and state_2:
            max_2 = i
            state_2 = False
        elif hots[i] == hots_sort[0]:
            max_1 = i

fp.write('####################################################################################')
fp.write('\n')
fp.write('####################################################################################')
fp.write('\n')
fp.write('\n')
fp.write('！豆瓣王者排行榜！'+'\n'+'\n')

fp.write('人气第一 ：'+book_names[max_1]+'\n'+'序号     ：'+str(int(max_1+1))+'\n'+'热度     ：'+str(hots[max_1])+'\n')
fp.write('\n')
fp.write('人气第二 ：'+book_names[max_2]+'\n'+'序号     ：'+str(int(max_2+1))+'\n'+'热度     ：'+str(hots[max_2])+'\n')
fp.write('\n')
fp.write('人气第三 ：'+book_names[max_3]+'\n'+'序号     ：'+str(int(max_3+1))+'\n'+'热度     ：'+str(hots[max_3])+'\n')
fp.write('\n')
fp.write('人气第四 ：'+book_names[max_4]+'\n'+'序号     ：'+str(int(max_4+1))+'\n'+'热度     ：'+str(hots[max_4])+'\n')
fp.write('\n')
fp.write('人气第五 ：'+book_names[max_5]+'\n'+'序号     ：'+str(int(max_5+1))+'\n'+'热度     ：'+str(hots[max_5])+'\n')
fp.write('\n')
fp.write('人气第六 ：'+book_names[max_6]+'\n'+'序号     ：'+str(int(max_6+1))+'\n'+'热度     ：'+str(hots[max_6])+'\n')
fp.write('\n')
fp.write('人气第七 ：'+book_names[max_7]+'\n'+'序号     ：'+str(int(max_7+1))+'\n'+'热度     ：'+str(hots[max_7])+'\n')
fp.write('\n')
fp.write('人气第八 ：'+book_names[max_8]+'\n'+'序号     ：'+str(int(max_8+1))+'\n'+'热度     ：'+str(hots[max_8])+'\n')
fp.write('\n')
fp.write('人气第九 ：'+book_names[max_9]+'\n'+'序号     ：'+str(int(max_9+1))+'\n'+'热度     ：'+str(hots[max_9])+'\n')
fp.write('\n')
fp.write('人气第十 ：'+book_names[max_10]+'\n'+'序号     ：'+str(int(max_10+1))+'\n'+'热度     ：'+str(hots[max_10])+'\n')
fp.write('\n')

