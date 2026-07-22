#需求：用户名密码登录，正确的用户名和密码为admin/666888 、zhangsan/123456、taoge/888666，5次登录机会，输入错误五次，不允许再操作了。
count = 0
while count<5:
    name = input("请输入你的用户名：")
    password = input("请输入你的密码：")
    if name == "" or password == "":
        print("密码和用户名不可以为空")
        count+=1
        continue
    elif name == "admin" and password=="666888":
        print("登录成功，进入B站首页~")
        break
    elif name == "zhangsan" and password == "123456":
        print("登录成功，进入B站首页~")
        break
    elif name == "taoge" and password=="888666":
        print("登录成功，进入B站首页~")
        break
    else:
        print("用户名或密码错误，请重新输入！")
        count+=1
if count==5:
    print("输入错误五次，不允许操作了")