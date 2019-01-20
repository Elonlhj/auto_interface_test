import requests

#接口测试：首先测试接口通不通，根据状态码可判断
#接口对不对：参数，响应，安全

#请求地址,设置请求超时时间timeout,超过时间就会请求异常
result=requests.get("http://www.baidu.com",timeout=0.00001)
#查看请求内容
print(result.text)
#请求状态码
print(result.status_code)

#============get请求===========
param={"wd":"测试"}
result=requests.get("http://www.baidu.com",params=param)
#获取状态码
print(result.status_code)
#获取响应头
print(result.headers)
#获取json格式数据
#print(result.json())
#失败请求,
print(result.raise_for_status())

#捕获异常
#try:
#    result.raise_for_status()
#except Exception as r:
#    print(r)
#else:
#    print(result.json())


#============post请求===========
datas={"wd":"测试"}
result1=requests.post("http://www.baidu.com",data=datas)
#获取状态码
print(result1.status_code)
#获取响应头
print(result1.headers)
#失败请求,
print(result1.raise_for_status())


#============文件上传接口==================
#mode打开方式rb
files1={"pic":open("文件地址",mode="rb")}
data1={"username":"zhangsan"}
result2=requests.post("url:接口地址",data=data1,files=files1)
print(result2.text)


#============超时异常：给此次请求设一个时间值===========
#============get请求===========
param={"wd":"测试"}
result=requests.get("http://www.baidu.com",timeout=0.0001,params=param)
#获取状态码
print(result.status_code)

