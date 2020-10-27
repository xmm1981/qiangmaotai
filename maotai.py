#京东秒杀
#加入购物车 再结算
from splinter.browser import Browser
from selenium import webdriver
import time
import datetime

#登录页面
def login(b):  #登录京东
    b.click_link_by_text("你好，请登录")
    b.click_link_by_text("账户登录")
    time.sleep(1)
    b.fill("loginname","xxxxxxxx")  #填写账户密码
    b.fill("nloginpwd","xxxxxx")
    b.find_by_id("loginsubmit").click()
    # time.sleep(0.1)
    return b

#订单页面
def loop(b):  #循环点击
    try:
        if b.title=="填写订单":
            b.find_by_text("submit").click() # 提交订单
            return b
        else:               #多次抢购操作后，有可能会被转到京东首页，所以要再打开手机主页
            b.visit("https://item.jd.com/100012043978.html") 
            #https://item.jd.com/100012043978.html 飞天 1499
            b.find_by_id("btn-reservation-mini").click()  # 抢购
            b.find_by_text("submit").click() # 提交订单
            #time.sleep(10)
            loop(b)     #递归  操作
    except Exception as e: #异常情况处理，以免中断程序
        b.reload()  #重新刷新当前页面，此页面为订单提交页
        #time.sleep(2)
        loop(b)  #重新调用自己

def buy_time(buytime):
    while True:
        now = datetime.datetime.now()
        #print(now.strftime('%Y-%m-%d %H:%m:%S'))
        if now.strftime('%Y-%m-%d %H:%M:%S') == buytime:
            while True:
                print("现在开始预约~~~~~~~~~~~~~~~~~~~~~~")
                #print(b.find_by_id("btn-reservation-mini"))  # 找到抢购按钮，输出 
                b.find_by_id("btn-reservation-mini").click()  # 抢购
                b.find_by_text("submit").click() # 提交订单

                loop(b)
                if b.title == "填写订单":  # 如果还在订单结算页
                    #time.sleep(3)
                    b.find_by_text("submit").click() # 提交订单
                else:
                    print('恭喜你，抢购成功')
                    print(now.strftime('%Y-%m-%d %H:%M:%S'))
                    break

# path = "/..../chromedriver"   Linux 目录
# driver = webdriver.Chrome(path)
b=Browser(driver_name="chrome") #打开浏览器
b.visit("https://item.jd.com/100012043978.html")
login(b)
#获取现在时间
now = datetime.datetime.now()
print("现在时间是：")
print(now.strftime('%Y-%m-%d %H:%M:%S'))
#设置抢购的时间
buy_time('2020-10-28 9:59:58')