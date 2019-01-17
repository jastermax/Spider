#利用selenium 抓取淘宝美食
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pymongo
def spider():
    driver = webdriver.Chrome()
    driver.get('http://www.taobao.com')
    input=driver.find_element_by_id('q') # 找到元素id为kw 实际上kw就是百度的输入框id
    input.send_keys('美食')  # 输入python
    input.send_keys(Keys.ENTER) # 模拟按下回车
    time.sleep(2)
    for i in range(1,101):
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        #屏幕滚动到页面底部
        prices = driver.find_elements_by_xpath('//*[@id="mainsrp-itemlist"]/div/div/div[1]/div/div[2]/div[1]/div[1]/strong')
        #抓取价格存如下边列表，为写入数据库做准备
        list_price=[]
        for price in prices:
            list_price.append(price.text)
        titles = driver.find_elements_by_xpath('//*[@id="mainsrp-itemlist"]/div/div/div[1]/div/div[2]/div[2]/a')
        #抓取名称
        list_title=[]
        for title in titles:
            list_title.append(title.text)
        input1=driver.find_element_by_class_name('J_Submit') #找到页码的确定按钮
        input1.send_keys(Keys.ENTER) # 模拟按下回车
        time.sleep(2)  #延时2秒
        list_vale=[]
        for price,title in zip(list_price,list_title):    
            list_vale.append({'Name':title,'Price':price})   #将内容对应以字典的形式存入列表
        writedb(list_vale)

def writedb(listtext):  #数据库写入函数
    myclient = pymongo.MongoClient('mongodb://localhost:27017/')
    mydb = myclient['local']
    mycol = mydb["taobaomeishi"]
    mycol.insert_many(listtext)
    myclient.close()

if __name__ == "__main__":
    spider()