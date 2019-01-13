import requests
count = 1
def spider(url):
    global count
    for i in url:
        if 'baidu' in i :
            print(i)
            try:
                response = requests.get(i, timeout=1, allow_redirects=False)
                if response.status_code==200:
                    with open('/home/ubuntu/Desktop/out1/out{}.jpg'.format(count), 'wb',) as f:
                        f.write(response.content)
                        f.flush()
                    count += 1
            except Exception as e:
                print(e)
def wenjian():
    str1 = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02127808'
    str2 = requests.get(str1)
    ls = str2.text.split('\r\n')
    spider(ls)
wenjian()
