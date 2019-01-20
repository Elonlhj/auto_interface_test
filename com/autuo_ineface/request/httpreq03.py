#==========接口之间依赖================
#登陆接口：https://passport.58v5.cn/gsso/login =======http://t.agent.union.58.com/bsp/agent/login



import requests

#requpar={"service":"http://te.union.vip.58.com/"}
#reqresult=requests.post("https://passport.58v5.cn/gsso/login?",data=requpar)
#requestparams={"username":"liuhongjian-wb","password":"cQX5tstEn+uNnsWvcPcYrW9bYpX3npm9mt43wjpLBifO4XR3yN0AtJqWR8236LNYAS6wIY8x9lvBrx4dv5SSMA=="}
#print(reqresult.text)

#获取登录地址的请求头信息
reqcanshu={"key":"value"}
dresult=requests.get("请求地址",params=reqcanshu)
print(dresult.text)
#获取响应头信息
print(dresult.headers)



#================响应中获取Cookie=====================
#响应头获取cookie
cookie=dresult.cookies
for cookie in dresult.cookies:
    print(cookie)

#根据上面接口信息作为参数访问下面接口
requests.get("访问路径",params=cookie)



#=================cookie存储在url中=====================
#获取到cookie
print(dresult.url)
index=str(dresult.url.find(":"))
cookie1=dresult.url[index+1:]
headers={"Cookie":cookie1}
#cookie在url中放在headers里是访问不了的
#result=requests.get("url",headers=headers)
#print(result.text)

#解决办法：把cookie拼接在地址里
result=requests.get("url:"+cookie1)
print(result.text)