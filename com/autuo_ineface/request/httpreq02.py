#请求地址 http://edu.csdn.net/lecturer/course_list
import requests
#通过Cookie越过登录
#加个请求头,这个请求头会报错，因为有省略号
#header={"Cookie":"uuid_tt_dd=10_6112018900-15355…d-4b31-809a-97d8-7b2a1f6b0156"}
#result=requests.post("http://edu.csdn.net/lecturer/course_list",headers=header)
#print(result.text.decode()

header={"Cookie":"uuid_tt_dd=10_6112018900-1535533891813-637051; dc_session_id=10_1535533891813.229701; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1535535002,1535535032,1535535074,1535535081; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1535535100; dc_tos=pe7ugr; smidV2=2018082917113278c4126739ad81b9729e2bceb7c39c9400749f482cc0f11c0; UN=humrLiu; BT=1535534360330; UserName=humrLiu; UserInfo=zWDZCkR%2BfVDOP%2Blif%2BVH8aI2GiReshO92PC%2B6OkE93M3h49MVy4mVhHflsFCBWglQsinPrNWEmsKgpyosJajPVmqhU9BRE9uhlt%2Fc5WD%2FQjddZ9vm2z1tQ1FaXTtjmmL; UserNick=humorLiu; AU=671; UserToken=zWDZCkR%2BfVDOP%2Blif%2BVH8aI2GiReshO92PC%2B6OkE93M3h49MVy4mVhHflsFCBWglQsinPrNWEmsKgpyosJajPVmqhU9BRE9uhlt%2Fc5WD%2FQiLl5iXtIJoRb9BYsJ3nTE8HkVJdKNDHVqxeCSJCtbAx3WUevGidCQcw%2BaZN7pYP2s%3D; TY_SESSION_ID=96dabbe3-bb90-4837-bbd2-675af1c9b71d; __yadk_uid=Ujr2eAUpegAQg8R4hBNqtNBCazZrrSFw"}
result=requests.post("https://blog.csdn.net/humrLiu",headers=header)
print(result.text)