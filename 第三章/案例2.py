# 案例：猜数字游戏
#
# 1.系统随机生成一个随机数
# 2.用户根据提示猜数字，并将所猜的数字输入系统
# 3.如果猜错，系统给出提示是猜大了，还是猜小了，然后继续输入猜的数字
# 4.如果猜对，系统自动退出，游戏结束
import random
num=random.randint(-999999,999999999)
print(num)
while True:
    number = int(input("请输入一个随机数字："))
    if number==num:
        print("猜对了！！！")
        break
    elif number > num:
        print("猜大了！！！")
        continue
    else:print("猜小了！！！")
