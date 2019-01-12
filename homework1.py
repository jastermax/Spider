def spider1(urladd):
    import urllib.request   
    response=urllib.request.urlopen(urladd)
    with open('/home/ubuntu/Desktop/out.txt','w',encoding='utf-8') as f:
        f.write(response.read().decode('utf8'))
def main():
    url="http://www.17k.com/chapter/2933095/36699279.html"
    spider1(url)
main()
