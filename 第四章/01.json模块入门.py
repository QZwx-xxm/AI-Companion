import json

#写入接送数据文件
# user={
#     "name":"小甜甜",
#     "age":18,
#     "gender":"女",
#     "hobby":["看电影","听音乐","看小说"]
# }
# with open("resources/user.json","w",encoding="utf-8") as f:
#     json.dump(user,f,ensure_ascii=False,indent=4)
#
with open("resources/user.json","r",encoding="utf-8") as f:
    user=json.load(f)
    print(user)
    print(type( user))