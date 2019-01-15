from bs4 import BeautifulSoup
from lxml import html
import requests
####################################################################################
#  在这先准备好请求头，需要爬的URL，表单参数生成函数，以及建立会话
############################# 1 #################################################
header={
    "Accept": "text/html, application/xhtml+xml, image/jxr, */*",
    "Referer": "http://uia.hnist.cn/sso/login?service=http%3A%2F%2Fportal.hnist.\
                cn%2Fuser%2FsimpleSSOLogin",    
    "Accept-Language": "zh-Hans-CN,zh-Hans;q=0.8,en-US;q=0.5,en;q=0.3",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "Keep-Alive",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36",
    "Accept-Encoding": "gzip, deflate",
    "Origin": "http://uia.hnist.cn",
    "Upgrade-Insecure-Requests": "1",
    
   #Cookie由Session管理，这里不用传递过去,千万不要乱改头，我因为改了头的HOST坑了我两天
}  

School_login_url = 'http://uia.hnist.cn/sso/login? \
service=http%3A%2F%2Fportal.hnist.cn%2Fuser%2FsimpleSSOLogin'#学校登录的URL

page = requests.Session()     #用Session发出请求能自动处理Cookie等问题
page.headers = header         #为所有请求设置头
page.get(School_login_url)    #Get该地址建立连接(通常GET该网址后，服务器会发送一些用于\
                                # 验证的参数用于识别用户，这些参数在这就全由requests.Session处理了)


def Get_lt():    #获取参数 lt 的函数
    f = requests.get(School_login_url,headers = header)
    soup = BeautifulSoup(f.content, "lxml")  
    once = soup.find('input', {'name': 'lt'})['value']
    return once

lt = Get_lt()  #获取lt

From_Data = {   #表单
    'username': 'your username',
    'password': 'Base64 encoded password',   
    #之前说过密码是通过base64加密过的,这里得输入加密后的值，或者像lt一样写个函数
    'lt': lt,
    '_eventId': 'submit',
}
############################# 1 end #############################

################################################################
#  在这一段向登录网站发送POST请求，并判断是否成功返回正确的内容
############################# 2 #################################

q = page.post(School_login_url,data=From_Data,headers=header) 
#发送登陆请求

#######判断是否成功##############
#print(q.url)    #这句可以查看请求的URL
#print(q.status_code)  #这句可以查看请求状态
#for (i,j) in q.headers.items():
#    print(i,':',j)        #这里可以查看响应头
#print('\n\n')
#for (i,j) in q.request.headers.items():
#    print(i,':',j)        #这里可以查看请求头
####上面的内容用于判断爬取情况，也可以用fiddle抓包查看 ####

f = page.get('http://uia.hnist.cn')    #GET需要登录后才能查看的网站
print("body:",f.text)

######## 进入查成绩网站，找到地址，请求并接收内容 #############

proxies = {  #代理地址，这里代理被注释了，对后面没影响，这里也不需要使用代理....
#"http": "http://x.x.x.x:x",
#"https": "http://x.x.x.x:x",
}
########  查成绩网站的text格式表单,其中我省略了很多...######
str = """callCount=1
httpSessionId=DA0080E0317A1AD0FDD3E09E095CB4B7.portal254
scriptSessionId=4383521D7E8882CB2F7AB18F62EED380
page=/web/guest/788
c0-scriptName=ShowTableAction
c0-methodName=showContent
c0-id=1424_1522286671427
c0-param3=string:2                  #页码
c0-param4=string:10
c0-param5=string:0
c0-param6=string:
c0-param7=string:%20
c0-param8=string:
c0-param9=string:IA%3D%3D
c0-param10=string:XH
c0-param11=string:24152400500%20   #必要的参数，学号
c0-param12=string:_portal_bg_ext_WAR_portal_bg_ext_INSTANCE_ei4Z_
c0-param13=string:
c0-param14=string:
c0-param22=string:
c0-param23=string:
c0-param24=string:
c0-param25=number:-1
c0-param26=string:
"""
#

f = page.post('http://portal.hnist.cn/portal_bg_ext/dwr/plainjs/
ShowTableAction.showContent.dwr',\data=str,proxies=proxies)
 #查成绩的地址，表单参数为上面的str
  
######  查看地址，返回状态，以及原始内容#######"""
print("f:",f.url)
print(f.status_code)
text = f.content.decode('unicode_escape')
print(text.encode().decode()) #因为原始内容中有\uxxx形式的编码，所以使用这句解码
###########################################"""
################################### 2 end #########################

###################################################################
#  解析获得的内容，并清洗数据，格式化输出...
############################# 3 ####################################
--------------------- 
作者：跬步至以千里 
来源：CSDN 
原文：https://blog.csdn.net/qq_32740675/article/details/79720367 
版权声明：本文为博主原创文章，转载请附上博文链接！