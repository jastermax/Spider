import requests
from lxml import etree
import pymongo
import threading
import time

def spider(listurl):
    start = time.time()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    }
    try:
        for url in listurl:
            print("开始爬取:"+url.split('_')[-1])
            response = requests.get(url,headers=headers)
            response.encoding = 'gbk'
            tree = etree.HTML(response.text)
            res = tree.xpath('//div[@class="result_right_list"]/ul/li/div/a')
            listtext=[]
            for res_ in res:
                href='http://v.7192.com'+res_.xpath('./@href')[0]
                response_=requests.get(href)
                response_.encoding='gbk'
                tree_=etree.HTML(response_.text)
                movieadd=tree_.xpath('//table[@id="mv_play_list"]/tr/th/a/@rel')[0]                    
                #print(movieadd)
                title=res_.xpath('./@title')[0]
                img=res_.xpath('./img/@data-original')[0]
                listtext.append({'movieadd':movieadd,'title':title,"imgadd":img})
                #print(movieadd,title,img)
            #lock.acquire()  # 锁住mongo
            writedb(listtext)
            #lock.release() # 打开mongo
    except Exception as e:
        print(e)
    end = time.time()
    print("爬虫完毕",end - start)
def writedb(listtext):
    myclient = pymongo.MongoClient('mongodb://localhost:27017/')
    mydb = myclient['local']
    mycol = mydb["movie"]
    mycol.insert_many(listtext)
    myclient.close()
    

if __name__ == "__main__":
    # lock = threading.Lock() # 创建线程锁
    baseurl='http://v.7192.com/movie_0_0_0_0_'
    listurl=[]
    for i in range(1,200):
        listurl.append(baseurl+str(i))
        spider(listurl)
    # lock = threading.Lock() # 创建线程锁
    # thread_1 = threading.Thread(target=spider,args=(listurl[:650],))
    # thread_2 = threading.Thread(target=spider,args=(listurl[650:1300],))
    # thread_3 = threading.Thread(target=spider,args=(listurl[1300:],))
    # thread_1.start()
    # thread_2.start()
    # thread_3.start()
    # thread_1.join()
    # thread_2.join()
    # thread_3.join()
    # spider(baseurl)
