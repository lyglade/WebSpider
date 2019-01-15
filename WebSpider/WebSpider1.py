from bs4 import BeautifulSoup
from lxml import html
import requests
####################################################################################
#  ������׼��������ͷ����Ҫ����URL�����������ɺ������Լ������Ự
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
    
   #Cookie��Session�������ﲻ�ô��ݹ�ȥ,ǧ��Ҫ�Ҹ�ͷ������Ϊ����ͷ��HOST����������
}  

School_login_url = 'http://uia.hnist.cn/sso/login? \
service=http%3A%2F%2Fportal.hnist.cn%2Fuser%2FsimpleSSOLogin'#ѧУ��¼��URL

page = requests.Session()     #��Session�����������Զ�����Cookie������
page.headers = header         #Ϊ������������ͷ
page.get(School_login_url)    #Get�õ�ַ��������(ͨ��GET����ַ�󣬷������ᷢ��һЩ����\
                                # ��֤�Ĳ�������ʶ���û�����Щ���������ȫ��requests.Session������)


def Get_lt():    #��ȡ���� lt �ĺ���
    f = requests.get(School_login_url,headers = header)
    soup = BeautifulSoup(f.content, "lxml")  
    once = soup.find('input', {'name': 'lt'})['value']
    return once

lt = Get_lt()  #��ȡlt

From_Data = {   #��
    'username': 'your username',
    'password': 'Base64 encoded password',   
    #֮ǰ˵��������ͨ��base64���ܹ���,�����������ܺ��ֵ��������ltһ��д������
    'lt': lt,
    '_eventId': 'submit',
}
############################# 1 end #############################

################################################################
#  ����һ�����¼��վ����POST���󣬲��ж��Ƿ�ɹ�������ȷ������
############################# 2 #################################

q = page.post(School_login_url,data=From_Data,headers=header) 
#���͵�½����

#######�ж��Ƿ�ɹ�##############
#print(q.url)    #�����Բ鿴�����URL
#print(q.status_code)  #�����Բ鿴����״̬
#for (i,j) in q.headers.items():
#    print(i,':',j)        #������Բ鿴��Ӧͷ
#print('\n\n')
#for (i,j) in q.request.headers.items():
#    print(i,':',j)        #������Բ鿴����ͷ
####��������������ж���ȡ�����Ҳ������fiddleץ���鿴 ####

f = page.get('http://uia.hnist.cn')    #GET��Ҫ��¼����ܲ鿴����վ
print("body:",f.text)

######## �����ɼ���վ���ҵ���ַ�����󲢽������� #############

proxies = {  #�����ַ���������ע���ˣ��Ժ���ûӰ�죬����Ҳ����Ҫʹ�ô���....
#"http": "http://x.x.x.x:x",
#"https": "http://x.x.x.x:x",
}
########  ��ɼ���վ��text��ʽ��,������ʡ���˺ܶ�...######
str = """callCount=1
httpSessionId=DA0080E0317A1AD0FDD3E09E095CB4B7.portal254
scriptSessionId=4383521D7E8882CB2F7AB18F62EED380
page=/web/guest/788
c0-scriptName=ShowTableAction
c0-methodName=showContent
c0-id=1424_1522286671427
c0-param3=string:2                  #ҳ��
c0-param4=string:10
c0-param5=string:0
c0-param6=string:
c0-param7=string:%20
c0-param8=string:
c0-param9=string:IA%3D%3D
c0-param10=string:XH
c0-param11=string:24152400500%20   #��Ҫ�Ĳ�����ѧ��
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
 #��ɼ��ĵ�ַ��������Ϊ�����str
  
######  �鿴��ַ������״̬���Լ�ԭʼ����#######"""
print("f:",f.url)
print(f.status_code)
text = f.content.decode('unicode_escape')
print(text.encode().decode()) #��Ϊԭʼ��������\uxxx��ʽ�ı��룬����ʹ��������
###########################################"""
################################### 2 end #########################

###################################################################
#  ������õ����ݣ�����ϴ���ݣ���ʽ�����...
############################# 3 ####################################
--------------------- 
���ߣ��Ͳ�����ǧ�� 
��Դ��CSDN 
ԭ�ģ�https://blog.csdn.net/qq_32740675/article/details/79720367 
��Ȩ����������Ϊ����ԭ�����£�ת���븽�ϲ������ӣ�