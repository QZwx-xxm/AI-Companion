# 案例 N的阶乘
# 定义一个函数，根据传入的数字，计算该数字阶乘的结果。
# def factorial(n):
#     num=1
#     for i in range(1,n+1):
#         num=num*i
#     return num
# number=int(input("请输入您想要算其阶乘的数字："))
# num=factorial(number)
# print(f"{number}的阶乘为：{num}")

def factorial(n):
    if n == 1 :
        return 1
    else:
        return n*factorial(n-1)

number=int(input("请输入您想要算其阶乘的数字："))
num=factorial(number)
print(f"{number}的阶乘为：{num}")