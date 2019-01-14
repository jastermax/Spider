import requests
import re
import threading


def spider(listadd):
    for j in listadd:
        response = requests.get(j)
        response.encoding = 'utf-8'
        title = re.findall('<h1>\n(.*)</h1>', response.text, re.S)
        content = re.findall('&#12288;&#12288;(.*?)<br /><br />', response.text)
        temp=title+content
        temp_new=[]
        for q in temp:
            temp_new.append(q+'\r\n')
        with open('/home/ubuntu/Desktop/out1/qqq'+j.split('/')[-1][0:7]+'.txt', 'w',) as f:
            f.writelines(temp_new)
        # print(title)
        # print(content)


def part(url):
    baseurl = 'http://www.17k.com'
    res1 = re.compile('<dd>.*</dd>', re.S)
    res2 = res1.findall(url)
    res = re.findall('href="(.*.html)', res2[0])
    ls = [baseurl+i for i in res]
    ls1 = []
    ls2 = []
    flag = 1
    for i in ls:
        if flag == 1:
            ls1.append(i)
        else:
            ls2.append(i)
        flag = -flag
        # print(i)

    thread_1 = threading.Thread(target=spider, args=(ls1,))
    thread_2 = threading.Thread(target=spider, args=(ls2,))
    thread_1.start()
    thread_2.start()
    thread_1.join()
    thread_2.join()


def wenjian():
    str1 = 'http://www.17k.com/list/2933095.html'
    str2 = requests.get(str1)
    str2.encoding = 'utf-8'
    part(str2.text)


if __name__ == "__main__":
    wenjian()
