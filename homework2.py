import urllib.request
import urllib.parse
def search(parameters):
    pars={
        "wd":parameters
    }
    data =urllib.parse.urlencode(pars)
    url=urllib.request.Request("http://www.baidu.com/s?"+data,method="GET")
    response = urllib.request.urlopen(url)
    #print(response.read().decode('utf8'))
    with open('/home/ubuntu/Desktop/out1.txt','w',encoding='utf-8') as f:
        f.write(response.read().decode('utf8'))
def main():
    searchstring='胡旺是个好人'
    search(searchstring)
main()

