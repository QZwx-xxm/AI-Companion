#将用户输入的10个数字，存储到一个列表中，并将列表中的数字进行排序，输出其中的最小值、最大值和平均值
print("请输入10个数字")
sum = 1
s=[]
while sum<=10:
    num=int(input(f"请输入第{sum}个数字:"))
    s.append(num)
    sum+=1
print (s)
s.sort()
print(s)
age=0
for i in s:
    age+=i
avage=age/10
print(f"s列表中最小值为：{s[0]}")
print(f"s列表中最小值为：{s[9]}")
print(f"s列表中平均值为：{avage}")